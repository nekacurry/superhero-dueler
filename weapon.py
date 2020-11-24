import random
from ability import Ability

class Weapon(Ability):
  def attack(self):
    half_max_damage = int(self.max_damage) // 2
    random_value = random.randint(half_max_damage, int(self.max_damage))
    return random_value