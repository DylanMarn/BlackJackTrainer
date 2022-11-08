# Dylan Marn
import random
import sys
import csv
import os

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = None
        self.cards = []
        self.faces = None
        self.faces = []

    def __str__(self):
        for card in self.cards:
            if card <= 4:
                self.faces.append("2")
            elif card <= 8:
                self.faces.append("3")
            elif card <= 12:
                self.faces.append("4")
            elif card <= 16:
                self.faces.append("5")
            elif card <= 20:
                self.faces.append("6")
            elif card <= 24:
                self.faces.append("7")
            elif card <= 28:
                self.faces.append("8")
            elif card <= 32:
                self.faces.append("9")
            elif card <= 36:
                self.faces.append("10")
            elif card <= 40:
                self.faces.append("J")
            elif card <= 44:
                self.faces.append("Q")
            elif card <= 48:
                self.faces.append("K")
            elif card <= 52:
                self.faces.append("A")
        if self.name == "Dealer" and len(self.faces) == 2:
            return f"Dealer is showing {self.faces[1]}"
        else:        
            return f"{self.name}'s hand: {(' '.join(self.faces))}"

    def add_card(self, card):
        self.cards.append(card)
        self.value = 0
        for card in sorted(self.cards):
            if card <= 4:
                self.value += 2
            elif card <= 8:
                self.value += 3
            elif card <= 12:
                self.value += 4
            elif card <= 16:
                self.value += 5
            elif card <= 20:
                self.value += 6
            elif card <= 24:
                self.value += 7
            elif card <= 28:
                self.value += 8
            elif card <= 32:
                self.value += 9
            elif card <= 48:
                self.value += 10
            elif card <= 52:
                if self.value <= 10:
                    self.value += 11
                else:
                    self.value += 1
        

# # Create a local .txt data base that saves a users login and cash amount

# # Create a dictionary of 52 cards in deck and a list of random numbers between 1 and 52 that can only appear once
def main():
    if len(sys.argv) < 2:
        while True:
            username = input("Enter username: ").strip().title()
            if username != "Dealer":
                break
            else:
                print("Username Taken")
    elif len(sys.argv) == 2:
        username = sys.argv[1].strip().title()
        if username == "Dealer":
            print("Username Taken")
            while True:
                username = input("Enter username: ").strip().title()
                if username != "Dealer":
                    break
                else:
                    print("Username Taken")
    else:
        sys.exit("Too many command-line arguments")

    usernames = []
    balances = []
    if os.path.exists("bank.csv"):
        print("Accessing bank database...")
        with open("bank.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                usernames.append(row["username"])
                balances.append(row["balance"])
    else:
        print("Creating bank database...")
        dirname = os.path.dirname(os.path.abspath(__file__))
        csvfilename = os.path.join(dirname, "bank.csv")
        with open(csvfilename, "w", newline='') as create_file:
            writer = csv.DictWriter(create_file, fieldnames=["username", "balance"])
            writer.writerow({"username": "username", "balance": "balance"})

    if username not in usernames:
        balance = 100
        with open("bank.csv", "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["username", "balance"])
            writer.writerow({"username": username, "balance": balance})
    else: 
        balance = balances[usernames.index(username)]

    used_cards = []

    dealer = Hand("Dealer")
    player = Hand(username)
    card, used_cards = get_card(used_cards)
    dealer.add_card(card)
    card, used_cards = get_card(used_cards)
    player.add_card(card)
    card, used_cards = get_card(used_cards)
    dealer.add_card(card)
    card, used_cards = get_card(used_cards)
    player.add_card(card)

    print(dealer)
    print(player)
    print(player.value)
    
    
def get_card(used_cards):
    while True:
        card = random.randint(1,52)
        if card not in used_cards:
            used_cards.append(card)
            return [card, used_cards]

                

    




# # Create a function that lets users decide next move
# def move():
#     choice = input("What would you like to do? ").strip().lower()
#     if len(playerhand) == 2:
#         while True:
#             if choice == "hit" or choice == "h":
#                 hit()
#                 break
#             elif choice == "stand" or choice == "st":
#                 stand()
#                 break
#             elif choice == "doubledown" or choice == "dd":
#                 doubledown()
#                 break
#             elif choice == "split" or choice == "sp":
#                 split()
#                 break
#     else:
#         if choice == "hit" or choice == "h":
#             hit()
#         elif choice == "stand" or choice == "s":
#             stand()
    

# # Create a "bet" function
# def bet():

# # Create a "hit" function
# def hit(playerhand, used_cards):

# # Create a "stand" function
# def stand():

# # Create a "double down" function
# def doubledown():

# # Create a "split" function
# def split():


if __name__ == "__main__":
    main()