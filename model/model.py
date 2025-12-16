import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.cromosomi_dict = {}


    def costruisci_grafo(self):
        cromosomi = DAO.read_cromosoma()
        self.cromosomi_dict = {cromosoma.id: cromosoma for cromosoma in cromosomi}
        interazioni = DAO.read_interazione()
        for interazione in interazioni:
            self.G.add_edge(self.cromosomi_dict[interazione.gene_1], self.cromosomi_dict[interazione.gene_2], peso=interazione.correlazione)

    def conta_nodi(self):
        return self.G.number_of_nodes()

    def conta_archi(self):
        return self.G.number_of_edges()

    def min_peso(self):
        min_peso = 0
        for u, v in self.G.edges():
            peso = self.G[u][v]['peso']
            if int(peso) < min_peso:
                min_peso = peso
        return min_peso

    def max_peso(self):
        max_peso = 0
        for u, v in self.G.edges():
            peso = self.G[u][v]['peso']
            if int(peso) > max_peso:
                max_peso = peso
        return max_peso

    def conta_inferiori(self, soglia):
        pass

    def conta_superiori(self, soglia):
        pass