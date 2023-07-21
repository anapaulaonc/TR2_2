from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


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
            switch_name = f's{i}'
            switch = self.net.addSwitch(switch_name)
            #armazenando os switches em um dicionario
            self.switches[switch_name] = switch

        #adicionando dez hosts
        for i in range(1, 11):
            host_name = f'h{i}'
            host_ip = f'10.0.0.{i}'
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
        self.net.start()
        #executando um teste de ping para garantir que todos hosts estao alcancaveis
        self.net.pingAll()
        #iniciando a interface da linha de comando do Mininet
        CLI(self.net)
        #parando a rede do Mininet
        self.net.stop()

if __name__ == '__main__':

    setLogLevel('info')
    #criando uma instancia da classe CustomTopology
    topology = CustomTopology()
    #chamando o metodo create_topology para criar a topologia e interagir com a rede
    topology.create_topology()
