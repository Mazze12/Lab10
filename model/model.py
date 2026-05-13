import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, anno):
        self._grafo.clear()
        nodes = DAO.getAllNodes(anno)
        self._idMap = {n.CCode: n for n in nodes}
        self._grafo.add_nodes_from(nodes)

        edges = DAO.getAllEdges(anno)
        for e in edges:
            u = self._idMap.get(e.Country1)
            v = self._idMap.get(e.Country2)
            if u and v:
                self._grafo.add_edge(u, v)

    def getDatiGrafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getSortedNodes(self):
        return sorted(self._grafo.nodes, key=lambda x: x.StateNme)

    def getGrado(self, n):
        return self._grafo.degree(n)

    def getCompConnesse(self):
        return nx.number_connected_components(self._grafo)