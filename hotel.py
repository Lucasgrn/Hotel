class Hotel:
  def __init__(self, nome, capacidade, piscina) -> None:
    self.name = nome
    self.capacity = capacidade
    self.occupancy = 0
    self.pool = piscina
    self.guests = ['']