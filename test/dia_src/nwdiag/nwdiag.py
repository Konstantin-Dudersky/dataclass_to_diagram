"""Диаграммы nwdiag."""

from dataclass_to_diagram.dia.nwdiag import (
    Diagram,
    Group,
    Network,
    Node,
    PeerNetwork,
)


# simple diagram ----------------------------------------------------------
# nodes
web01 = Node("web01")
web02 = Node("web02")
db1 = Node("db1")
db2 = Node("db2")
# networks
dmz = Network(name="dmz", address="210.x.x.x/24")
dmz.add_node(web01, ["210.x.x.1"])
dmz.add_node(web02, ["210.x.x.2"])
interal = Network(name="internal", address="172.x.x.x/24")
interal.add_node(web01, ["172.x.x.1"])
interal.add_node(web02, ["172.x.x.2"])
interal.add_node(db1, [])
interal.add_node(db2, [])
dia1 = Diagram(filename="nwdiag1", networks=(dmz, interal))

# define multiple addresses -----------------------------------------------
# nodes
web01 = Node("web01")
web02 = Node("web02")
db1 = Node("db1")
db2 = Node("db2")
# networks
dmz = Network(name="dmz", address="210.x.x.x/24")
dmz.add_node(web01, ["210.x.x.1", "210.x.x.20"])
dmz.add_node(web02, ["210.x.x.2"])
interal = Network(name="internal", address="172.x.x.x/24")
interal.add_node(web01, ["172.x.x.1"])
interal.add_node(web02, ["172.x.x.2"])
interal.add_node(db1, [])
interal.add_node(db2, [])
dia2 = Diagram(filename="nwdiag2", networks=(dmz, interal))

# grouping nodes 1 --------------------------------------------------------
# nodes
web01 = Node("web01")
web02 = Node("web02")
db01 = Node("db01")
db02 = Node("db02")
# networks
sample_front = Network(name="Sample_front", address="192.168.10.0/24")
sample_front.add_node(web01, [".1"])
sample_front.add_node(web02, [".2"])
sample_back = Network(name="Sample_back", address="192.168.20.0/24")
sample_back.add_node(web01, [".1"])
sample_back.add_node(web02, [".2"])
sample_back.add_node(db01, [".101"])
sample_back.add_node(db02, [".102"])
# groups
web = Group(name="web", nodes=(web01, web02))
db = Group(name="db", nodes=(db01, db02))
dia3 = Diagram(
    filename="nwdiag3",
    networks=(sample_front, sample_back),
    groups=(web, db),
)

# grouping nodes 2 --------------------------------------------------------
# nodes
web01 = Node("web01")
web02 = Node("web02")
db01 = Node("db01")
# networks
dmz = Network(name="dmz")
dmz.add_node(web01)
dmz.add_node(web02)
internal = Network(name="internal")
internal.add_node(web01)
internal.add_node(web02)
internal.add_node(db01)
# groups
web = Group(name="", nodes=(web01, web02, db01), color="#FF7777")
dia4 = Diagram(
    filename="nwdiag4",
    networks=(dmz, internal),
    groups=(web,),
)

# peer networks -----------------------------------------------------------
# nodes
inet = Node("inet")
router = Node("router")
web01 = Node("web01")
web02 = Node("web02")
# networks
nw = Network()
nw.add_node(router)
nw.add_node(web01)
nw.add_node(web02)
peer_net = PeerNetwork(inet, router)
dia5 = Diagram(
    filename="nwdiag5",
    networks=(nw,),
    peer_networks=(peer_net,),
)
