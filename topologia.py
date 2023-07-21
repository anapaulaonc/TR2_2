from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomTopology:
    def __init__(self):
        self.net = None
        self.controller = None
        self.switches = {}
        self.hosts = {}

    def create_topology(self):
        self.net = Mininet(topo=None, controller=Controller)
        self.controller = self.net.addController('c0', controller=Controller)

        # Adicione quatro switches OpenFlow habilitados
        for i in range(1, 5):
            switch_name = f's{i}'
            switch = self.net.addSwitch(switch_name)
            self.switches[switch_name] = switch

        # Adicione dez hosts
        for i in range(1, 11):
            host_name = f'h{i}'
            host_ip = f'10.0.0.{i}'
            host = self.net.addHost(host_name, ip=host_ip)
            self.hosts[host_name] = host

        # Conecte hosts aos switches
        host_list = list(self.hosts.values())
        for i, switch in enumerate(self.switches.values()):
            switch.linkTo(host_list[i % len(host_list)])

        # Conecte os switches ao controlador
        for switch in self.switches.values():
            switch.linkTo(self.controller)

        self.net.start()
        self.net.pingAll()
        CLI(self.net)
        self.net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology = CustomTopology()
    topology.create_topology()
