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
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        else:
            print(f"Silly {self.first_name}, you are already a member!")
        return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{self.first_name}, you have {self.gold_card_points} points left in your account")
        else: 
            print(f"Sorry you gotta spend money to make money. {self.first_name}, you only have {self.gold_card_points} points currently.")
        return self

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


jimmy = User(jimmy_data)


rihana = User(rihana_data)

luke.display_info().enroll().spend_points(101).display_info()

jimmy.spend_points(50).enroll().spend_points(199)

rihana.enroll().spend_points(50).spend_points(50).spend_points(101)