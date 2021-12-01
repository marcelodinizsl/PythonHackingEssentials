from Hero import Hero

class MyHero(Hero):
    skill = ["sword","spear", "bow", "axe"]
    power = [98.5, 89.2, 100, 79.2]
    
    def __init__(self, in_skill, in_power, idx):
        super().__init__("hong gil dong", 18, 69.3)
        self.skill = in_skill
        self.power = in_power
        self.idx = idx
        
    def print_skill(self):
        print("4.armed weapon: {} [power:{}]".format(self.skill, self.power[self.idx]))
        
