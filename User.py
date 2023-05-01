class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.age = data["age"]

        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        else:
            print(f"Silly {self.first_name}, you are already a member!")

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"You have {self.gold_card_points} points left in your account")
        else: 
            print(f"Sorry you gotta spend money to make money. You only have {self.gold_card_points} points currently.")

luke_data = {
    "first_name": "Luke",
    "last_name": "Jech", 
    "email": "Luke@gmail.com",
    "age" : 30
}
jimmy_data = {
    "first_name": "Jimmy",
    "last_name": "Neutron", 
    "email": "BoyGenius@gmail.com",
    "age" : 26
}
rihana_data = {
    "first_name": "Robyn",
    "last_name": "Fenty", 
    "email": "Rihana@gmail.com",
    "age" : 35
}
luke = User(luke_data)

luke.display_info()

jimmy = User(jimmy_data)

jimmy.display_info()

rihana = User(rihana_data)

rihana.display_info()

print(luke.gold_card_points, luke.is_rewards_member)
luke.enroll()
print(luke.gold_card_points, luke.is_rewards_member)

luke.spend_points(50)
jimmy.enroll()
jimmy.spend_points(80)

luke.enroll()
rihana.spend_points(201)