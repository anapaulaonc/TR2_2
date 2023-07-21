from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(topo = None, controller=Controller)

    # Adicione um controlador
    c0 = net.addController('c0', controller=Controller)

    # Adicione quatro switches OpenFlow habilitados
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Adicione dez hosts
    h1 = net.addHost('h1', ip="10.0.0.1")
    h2 = net.addHost('h2', ip="10.0.0.2")
    h3 = net.addHost('h3', ip="10.0.0.3")
    h4 = net.addHost('h4', ip="10.0.0.4")
    h5 = net.addHost('h5', ip="10.0.0.5")
    h6 = net.addHost('h6', ip="10.0.0.6")
    h7 = net.addHost('h7', ip="10.0.0.7")
    h8 = net.addHost('h8', ip="10.0.0.8")
    h9 = net.addHost('h9', ip="10.0.0.9")
    h10 = net.addHost('h10', ip="10.0.0.10")
    # Adicione mais oito hosts aqui...

    # Conecte hosts aos switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s2)
    net.addLink(h5, s2)
    net.addLink(h6, s2)
    net.addLink(h7, s3)
    net.addLink(h8, s3)
    net.addLink(h9, s4)
    net.addLink(h10, s4)
    # Adicione mais links entre hosts e switches aqui...

    # Conecte os switches ao controlador
    # net.addLink(s1, c0)
    # net.addLink(s2, c0)
    # net.addLink(s3, c0)
    # net.addLink(s4, c0)

    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])
    net.pingAll()
    CLI(net)
    net.stop()


setLogLevel('info')
create_topology()
