from ability import Ability
from armor import Armor
import random

class Hero:

  def __init__(self, name, starting_health=100):
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  # ADD ABILITIES METHOD
  def add_ability(self, ability):
    self.abilities.append(ability)

  # ATTACK METHOD
  def attack(self):
    total_damage = 0 

    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  # ADD ARMOR METHOD
  def add_armor(self, armor):

    self.armors.append(armor)

  # DEFEND METHOD
  def defend(self, damage):
    total_block = 0

    for armor in self.armors:
      total_block += armor.block()
    return total_block

  # TAKE DAMAGE METHOD

  def take_damage(self, damage):
    total_damage = damage - self.defend(damage)
    self.current_health -= total_damage

  # FIGHT METHOD
  def fight(self, opponent):
    heroList = [self.name, opponent.name]
    winner = random.choice(heroList)
    print(winner + " wins!")


# TESTING
''' if __name__ == "__main__":
  hero1 = Hero("Grace Hopper")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2) '''

''' if __name__ == "__main__":
  ability = Ability("Great Debugging", 50)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  print(hero.abilities) '''

''' if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack()) '''

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)