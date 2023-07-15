import unittest
from temp.GraphModule import GraphModule, GraphModuleState, GraphModulePort, GraphModulePortType, GraphModulePortTarget

class TestGraphModule(unittest.TestCase):
    def test_init_with_values(self):
        port1 = GraphModulePort(0, GraphModulePortType.INPUT_NET, GraphModulePortTarget(0))
        port2 = GraphModulePort(1, GraphModulePortType.OUTPUT_NET, GraphModulePortTarget(1))
        gm = GraphModule(1, ports=[port1, port2], vars=["var1", "var2"])
        self.assertEqual(gm.state, GraphModuleState.UNINITIALIZED)
        self.assertEqual(gm.id, 1)
        self.assertEqual(gm.graph, None)
        self.assertEqual(gm.vars, ["var1", "var2"])
        self.assertEqual(gm.ports, [port1, port2])

    def test_mark_dirty(self):
        gm = GraphModule(1)
        gm.mark_dirty()
        self.assertEqual(gm.state, GraphModuleState.DIRTY)

    def test_numbering_ports_with_different_base(self):
        port1 = GraphModulePort(0, GraphModulePortType.INPUT_NET, GraphModulePortTarget(0))
        port2 = GraphModulePort(1, GraphModulePortType.OUTPUT_NET, GraphModulePortTarget(1))
        gm = GraphModule(1, ports=[port1, port2])
        gm.numbering_ports(100)
        self.assertEqual(gm.ports[0].id, 100)
        self.assertEqual(gm.ports[1].id, 101)
        self.assertEqual(gm.state, GraphModuleState.INITIALIZED)
    def test_init(self):
        gm = GraphModule(id=1)
        self.assertEqual(gm.state, GraphModuleState.UNINITIALIZED)
        self.assertEqual(gm.id, 1)
        self.assertEqual(gm.graph, None)
        self.assertEqual(gm.instances, [])
        self.assertEqual(gm.vars, [])
        self.assertEqual(gm.ports, [])

    def test_from_instances(self):
        gm1 = GraphModule(1)
        gm2 = GraphModule(2)
        gm = GraphModule.from_instances(id=3, instances=[gm1, gm2])
        self.assertEqual(gm.id, 3)
        self.assertEqual(gm.instances, [gm1, gm2])

    def test_check_init(self):
        gm = GraphModule(0)
        with self.assertRaises(Exception):
            gm.check_init()

    def test_numbering_ports(self):
        port1 = GraphModulePort(0, GraphModulePortType.INPUT_NET, GraphModulePortTarget(0))
        port2 = GraphModulePort(0, GraphModulePortType.OUTPUT_NET, GraphModulePortTarget(1))
        gm = GraphModule(0, ports=[port1, port2])
        gm.numbering_ports(10)
        self.assertEqual(gm.ports[0].id, 10)
        self.assertEqual(gm.ports[1].id, 11)
        self.assertEqual(gm.state, GraphModuleState.INITIALIZED)

if __name__ == "__main__":
    unittest.main()
