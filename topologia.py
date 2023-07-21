from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Adicione um controlador
    c0 = net.addController('c0')

    # Adicione quatro switches OpenFlow habilitados
    s1 = net.addSwitch('s1', protocols='OpenFlow13')
    s2 = net.addSwitch('s2', protocols='OpenFlow13')
    s3 = net.addSwitch('s3', protocols='OpenFlow13')
    s4 = net.addSwitch('s4', protocols='OpenFlow13')

    # Adicione dez hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    # Adicione mais oito hosts aqui...

    # Conecte hosts aos switches
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    # Adicione mais links entre hosts e switches aqui...

    # Conecte os switches ao controlador
    net.addLink(s1, c0)
    net.addLink(s2, c0)
    net.addLink(s3, c0)
    net.addLink(s4, c0)

    net.start()
    CLI(net)
    net.stop()


setLogLevel('info')
create_topology()
