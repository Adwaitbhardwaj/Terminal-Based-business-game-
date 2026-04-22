import random

user = input("do you want to play game (yes/no)").upper()

if user == "YES":
    print("\033[38;2;220;220;0mLETS PLAY!\033[0m")
print('''\033[38;2;255;0;0m
+------------+------------+------------+------------+------------+
|  JAKARTA   |   BERLIN   |   MOSCOW   |  TORONTO   |   SEOUL    |
|   ₹170     |   ₹20      |   ₹60      |   ₹30      |   ₹60      |
|            |            |            |            |            |
+------------+------------+------------+------------+------------+\033[0m''')


print('''\033[38;2;0;200;200m+------------+                                        +------------+
|  MADRID    |                                        |  ZURICH    |
|  ₹105      |                                        |  ₹320      |
|            |                                        |            |
+------------+                                        +------------+
|  CAIRO     |                                        |  RIYADH    |
|  ₹45       |                                        |  ₹320      |
|            |                                        |            |
+------------+                                        +------------+
|  BANGKOK   |            🎲 GAME AREA                |  SYDNEY    |
|  ₹45       |                                        |  ₹40       |
|            |                                        |            |
+------------+                                        +------------+
|  DELHI     |                                        |  BEIJING   |
|  ₹200      |                                        |  ₹300      |
|            |                                        |            |
+------------+------------+------------+------------+------------+-- \033[0m''')
     
       
print('''\033[38;2;255;0;0m+------------+------------+------------+------------+------------+
|   START    |   TOKYO    |   LONDON   | HONG KONG  |   PARIS    |
|            |   ₹70      |   ₹420     |   ₹350     |   ₹350     |
|            |            |            |            |            |
+------------+------------+------------+------------+------------+


      \033[0m''')

cities = [
    {"name": "Start", "rate": 0, "owner": None},
    {"name": "Tokyo", "rate": 70, "owner": None},
    {"name": "London", "rate": 420, "owner": None},
    {"name": "Hong Kong", "rate": 350, "owner": None},
    {"name": "Paris", "rate": 350, "owner": None},
    {"name": "Beijing", "rate": 300, "owner": None},
    {"name": "Sydney", "rate": 40, "owner": None},
    {"name": "Riyadh", "rate": 320, "owner": None},
    {"name": "Zurich", "rate": 320, "owner": None},
    {"name": "Seoul", "rate": 60, "owner": None},
    {"name": "Toronto", "rate": 30, "owner": None},
    {"name": "Moscow", "rate": 60, "owner": None},
    {"name": "Berlin", "rate": 20, "owner": None},
    {"name": "Jakarta", "rate": 170, "owner": None},
    {"name": "Madrid", "rate": 105, "owner": None},
    {"name": "Cairo", "rate": 45, "owner": None},
    {"name": "Bangkok", "rate": 45, "owner": None},
    {"name": "Delhi", "rate": 200, "owner": None}
]

list1 = []
user2 = int(input("how many player: "))

for i in range(user2):
    name = input(f"enter name of {i+1} person: ")
    players = {
        "name": name,
        "position": 0,
        "amount": 1000
    }
    list1.append(players)

game_running = True

while game_running:
    for players in list1:

        print(f"\n{players['name']} turn")

        dice = random.randint(1, 6)
        print("Dice:", dice)

        players["position"] = (players["position"] + dice) % len(cities)

        a = cities[players["position"]]
        print("You landed on:", a["name"], "Price:", a["rate"])


        if a["owner"] is None:
            if players["amount"] >= a["rate"]:
                person = input("Do you want to buy? (yes/no): ").upper()

                if person == "YES":
                    players["amount"] -= a["rate"]
                    a["owner"] = players["name"]
                    print(" Bought!")
            else:
                print(" Not enough money")

    
        elif a["owner"] != players["name"]:
            print(f" Pay rent to {a['owner']}")
            rent = a["rate"] // 2
            players["amount"] -= rent

        
            for p in list1:
                if p["name"] == a["owner"]:
                    p["amount"] += rent

        else:
            print("Your own city")

        print("Your money:", players["amount"])

        if players["amount"] <= 0:
            print(f"\n {players['name']} is bankrupt!")
            print("GAME OVER")
            game_running = False
            break