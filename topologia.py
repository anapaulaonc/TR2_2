from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.controller.handler import set_ev_cls
import time

#criando a classe  do aplicativo Ryu que sera responsavel por manipular as regras OpenFlow
class SecurityApp(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SecurityApp, self).__init__(*args, **kwargs)

    def switch_features_handler(self, ev):
        #definindo o switch e o protocolo OpenFlow
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        #adicionando uma regra de fluxo para bloquear pacotes ICMP(ping) de h1 para h2 no switch s1
        if datapath.id == 1:
            match = parser.OFPMatch(eth_type=0x0800, ip_proto=1, ipv4_src='10.0.0.1', ipv4_dst='10.0.0.2')
            actions = [] #sem acoes, ou seja, bloquear
            self.add_flow(datapath, 1, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority, match=match, instructions=inst)
        datapath.send_msg(mod)



#criando uma classe chamada CustomTopology
class CustomTopology:
    def __init__(self):
        #definindo variaveis para rede, controlador, switches e hosts
        self.net = None
        self.controller = None
        self.switches = {}
        self.hosts = {}

    def create_topology(self):
        #inicializando a rede do Mininet sem uma topologia especifica
        self.net = Mininet(topo=None, controller=Controller)
        #adicionando um controlador a rede como nome c0
        self.controller = self.net.addController('c0', controller=Controller)

        # Adicione quatro switches OpenFlow habilitados
        for i in range(1, 5):
            switch_name =  's{}'.format(i)
            switch = self.net.addSwitch(switch_name)
            #armazenando os switches em um dicionario
            self.switches[switch_name] = switch

        #adicionando dez hosts
        for i in range(1, 11):
            host_name =  'h{}'.format(i)
            host_ip = '10.0.0.%d' % i
            host = self.net.addHost(host_name, ip=host_ip)
            #armazenando os hosts em um dicionario
            self.hosts[host_name] = host

        #conectando os hosts aos switches, garantindo que cada host esta em um switch diferente
        host_list = list(self.hosts.values())
        for i, switch in enumerate(self.switches.values()):
            switch.linkTo(host_list[i % len(host_list)])

        #conectando os switches ao controlador
        for switch in self.switches.values():
            switch.linkTo(self.controller)
        #iniciando a rede do Mininet
        self.net.build()
        self.net.start()

        time.sleep(3)
        #executando um teste de ping para garantir que todos hosts estao alcancaveis
        self.net.pingAll()

        ryu_app = SecurityApp()
        ryu_app.start()

        #iniciando a interface da linha de comando do Mininet
        CLI(self.net)
        #parando a rede do Mininet
        self.net.stop()






setLogLevel('info')
#criando uma instancia da classe CustomTopology
topology = CustomTopology()
#chamando o metodo create_topology para criar a topologia e interagir com a rede
topology.create_topology()
