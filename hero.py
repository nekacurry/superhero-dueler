import random

class Hero:

  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    heroList = [self.name, opponent.name]
    winner = random.choice(heroList)
    print(winner + " wins!")

if __name__ == "__main__":
  hero1 = Hero("Grace Hopper")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2)




