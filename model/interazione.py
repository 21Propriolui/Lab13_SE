from dataclasses import dataclass

@dataclass
class Interazione:
    cromosoma_1 : int
    cromosoma_2 : int
    gene_1 : str
    gene_2 : str
    correlazione : float

    def __hash__(self):
        return hash(self.cromosoma_1) and hash(self.cromosoma_2) and hash(self.correlazione)

    def __str__(self):
        return f'{self.cromosoma_1} {self.cromosoma_2} {self.gene_1} {self.gene_2} {self.correlazione}'
