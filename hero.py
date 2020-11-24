from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:

  def __init__(self, name, starting_health=100):
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.deaths = 0
    self.kills = 0
  
  # ADD KILL METHOD 
  def add_kill(self, num_kills):
    self.kills += num_kills
  
  # ADD DEATH METHOD
  def add_death(self, num_deaths):
    self.deaths += num_deaths

  # ADD WEAPON METHOD
  def add_weapon(self, weapon):
    self.abilities.append(weapon)

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

  # IS ALIVE METHOD

  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True

  # FIGHT METHOD
  def fight(self, opponent):
    if len(self.abilities) <= 0 and len(opponent.abilities) <= 0:
      print("It's a Draw!")
    else:
      while self.is_alive() and opponent.is_alive():
        opponent.take_damage(self.attack())
        self.take_damage(opponent.attack())
      if self.is_alive() == False:
        self.deaths += 1
        opponent.kills += 1
        print(f"{opponent.name} wins!")
      else:
        opponent.deaths += 1
        self.kills += 1
        print(f"{self.name} wins!")

        
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

''' if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health) '''

''' if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive()) '''

''' if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 80)
  ability4 = Ability("Wizard Beard", 20)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  hero1.fight(hero2) '''

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
  hero = Hero("Wonder Woman")
  weapon = Weapon("Lasso of Truth", 90)
  hero.add_weapon(weapon)
  print(hero.attack())