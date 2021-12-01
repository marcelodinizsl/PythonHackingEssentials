class Hero:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def print_hero(self):
        print("\n")
        print("__________________________")
        print("1.{}".format(self.name))
        print("2.{}".format(self.age))
        print("3.{}".format(self.weight))