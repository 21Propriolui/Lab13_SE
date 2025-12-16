from dataclasses import dataclass

@dataclass
class Cromosoma:
    id : str
    funzione : str
    cromosoma : int

    def __str__(self):
        return f'{self.id} {self.funzione} {self.cromosoma}'

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id