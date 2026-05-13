import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._nodes = DAO.getAllCountry()
        #Definisco la mia idMap per risalire all'oggetto dal codice del paese
        self._idMap={}
        for n in self._nodes:
            self._idMap[n.CCode] = n

    def getAllCountry(self):
        return DAO.getAllCountry()

    def getAllNodes(self, annoMax):
        return DAO.getAllNodes(annoMax)

    def addEdges(self, annoMax):
        allConfini = DAO.getAllEdges(annoMax, self._idMap)
        for c in allConfini:
            if c.Country1 in self._grafo and c.Country2 in self._grafo:
                if self._grafo.has_edge(c.Country1, c.Country2) or self._grafo.has_edge(c.Country2, c.Country1):
                    continue
                else:
                    self._grafo.add_edge(c.Country1, c.Country2)

    def buildGraph(self, annoMax):
        allNodes = self.getAllNodes(annoMax)
        self._grafo.add_nodes_from(allNodes)
        self.addEdges(annoMax)
        print(f"Il grafo presenta {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} archi")

    def getGraphDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)

    def get_num_confinanti(self, nodo):
        return self._grafo.degree(nodo)

    def getInfoCompConnessa(self, nodo):
        #Cerco la componente connessa che contiene il nostr stato
        conn = nx.node_connected_component(self._grafo, nodo)
        print(f"Size componente connessa: {len(conn)}")
        return len(conn)


