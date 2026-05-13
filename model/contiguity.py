from dataclasses import dataclass


@dataclass
class Contiguity:
    Country1:int
    Country2:int
    year: int
    dyad:int

    def __hash__(self):
        return hash(self.Country1, self.Country2, self.year)

    def __eq__(self, other):
        return self.Country1 == other.Country1 and self.Country2 == other.Country2 and self.year == other.year

    def __str__(self):
        return f"{self.Country1} - {self.Country2} ({self.year})"

