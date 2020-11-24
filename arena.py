from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    self.team_one = None
    self.team_two = None

  def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = input("What is the max damage of the ability?  ")

    return Ability(name, max_damage)

  def create_weapon(self):
    name = input("What is the weapon name?  ")
    max_damage = input("What is the max damage of the weapon?  ")

    return Weapon(name, max_damage)

  def create_armor(self):
    name = input("What is the armor name?  ")
    max_block = input("What is the max defense of the armor?  ")

    return Armor(name, max_block)

  def create_hero(self):
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None

    while add_item != "4":
        add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")

        if add_item == "1":
          new_ability = self.create_ability()
          hero.add_ability(new_ability)

        elif add_item == "2":
          new_weapon = self.create_weapon()
          hero.add_weapon(new_weapon)

        elif add_item == "3":
          new_armor = self.create_armor()
          hero.add_armor(new_armor)

    return hero

  def build_team_one(self):
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
        hero = self.create_hero()
        self.team_one.add_hero(hero)

  def build_team_two(self):
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
        hero = self.create_hero()
        self.team_two.add_hero(hero)

  def team_battle(self):
    self.team_one.attack(self.team_two)

  def show_stats(self):
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    team_kills = 0
    team_deaths = 0

    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))


    # Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived
    for hero in self.team_two.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_two.name + ": " + hero.name)