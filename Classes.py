import sys
import random


class Player:
    name = ""
    hero = ""
    combo = 0
    type = ""

    def __init__(self, x, y, z, w):
        self.name = x
        self.hero = y
        self.combo = z
        self.type = w


class Righteous:
    points = 0

    def heal(self):
        self.points += 20
        return self.points


class Villains:
    strength = 0

    def punch(self):
        self.strength += 10
        return self.strength


class Hero(Righteous, Villains):
    myattack = 0
    mydefense = 0
    mymovement = 0

    def __init__(self, x, y, z):
        self.myattack = x
        self.mydefense = y
        self.mymovement = z


def resolve_fight(x, y):
    p1_extra_points = 0
    p2_extra_points = 0

    if str(player1.combo) == str(player1.combo)[::-1]:
        p1_extra_points += 30
    if str(player2.combo) == str(player2.combo)[::-1]:
        p2_extra_points += 30
    if is_prime(player1.combo) == 0:
        p1_extra_points += 40
    if is_prime(player2.combo) == 0:
        p2_extra_points += 40

    if player1.type == 1:
        p1_extra_points += player1.hero.punch()
    else:
        p1_extra_points += player1.hero.heal()

    if player2.type == 1:
        p2_extra_points += player2.hero.punch()
    else:
        p2_extra_points += player2.hero.heal()

    p1_score = player1.combo//100 * player1.hero.myattack + player1.combo//10%10 * player1.hero.mydefense + player1.combo%10 * player1.hero.mymovement + p1_extra_points
    p2_score = player2.combo // 100 * player2.hero.myattack + player2.combo // 10 % 10 * player2.hero.mydefense + player2.combo % 10 * player2.hero.mymovement + p2_extra_points
    if p1_score >= p2_score:
        winner = player1.name
    else:
        winner = player2.name

    print("The result \n-----------------------------------")
    print("Name\tExtra Points\tTotal Score")
    print(player1.name, "\t\t", p1_extra_points, "\t\t\t", p1_score)
    if player2.name != "computer":
        print(player2.name, "\t\t", p2_extra_points, "\t\t\t", p2_score)
    else:
        print(player2.name, "\t", p2_extra_points, "\t\t\t", p2_score)

    print("-----------------------------------")
    print("WINNER: " + winner)


def str_to_class(className):
    return getattr(sys.modules[__name__], className)


def is_prime(x):
    for num in range(2, x):
        if x % num != 0:
            return 0
        else:
            return 1


ninja = Hero(10, 20, 30)
samurai = Hero(30, 20, 5)
robot = Hero(15, 25, 5)
wrestler = Hero(14, 7, 8)


villain_list = ["ninja", "robot"]
righteous_list = ["samurai", "wrestler"]

print("Welcome to the Fighting Game")
p1_name = input("Please enter your name. Player 1: ")
p2_name = input("Please enter your name or type computer. Player 2: ")
print("Welcome " + p1_name + " and " + p2_name)
print("Here's the list of fighters: ")
print("Samurai: Strong kicks, average defense, slow movement")
print("Ninja: Average kicks, weak defense, fast movement")
print("Robot: Strong kicks, strong defense, very slow movement")
print("Wrestler: Strong kicks, average defense, average movement")
p1_hero = input("Player 1. Select hero: ").lower()
if p2_name != "computer":
    p2_hero = input("Player 2. Select hero: ").lower()
else:
    p2_hero = "samurai"

print("Enter your 3 digit combo (Attack-Defense-Movement)")
while True:
    try:
        p1_combo = int(input("Player 1 Combo: "))
        if p2_name != "computer":
            p2_combo = int(input("Player 2 Combo: "))
        else:
            p2_combo = random.randrange(150)
        break
    except ValueError:
        print("Bad input")

type1 = 0
type2 = 0
if villain_list.__contains__(p1_hero):
    type1 = 1  # villain
else:
    type1 = 0  # righteous

if p2_name != "computer":
    if villain_list.__contains__(p2_hero):
        type2 = 1  # villain
    else:
        type2 = 0  # righteous
else:
    type2 = 0

player1 = Player(p1_name, str_to_class(p1_hero), p1_combo, type1)
player2 = Player(p2_name, str_to_class(p2_hero), p1_combo, type2)

resolve_fight(player1, player2)
