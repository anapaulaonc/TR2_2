from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


#* creating test
class SingleSwichTopo(Topo):
    #* a switch connected no n hosts"
    def __init__(self, n=2, **opts):
        #* creating topology and default options
        Topo.__init__(self, **opts)
        swich = self.addSwitch('swich1')

        for h in range(n):
            host = self.addHost('host%s', (n + 1))
            self.addLink(host, swich)


def simpleTest():
    #* here we´re creating a topology with 4 hosts
    topo = SingleSwichTopo(n = 4)
    net = Mininet(topo)
    net.start()
    print("Testing our topology")
    net.pingAll()
    net.stop()


if __name__ == "__main__":
    setLogLevel('info')
    simpleTest()
