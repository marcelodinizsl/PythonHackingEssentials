from MyHero import MyHero

def main():
    i = 0
    query_skill = input("Select weapon:")
    for each_item in  MyHero.skill:
        if each_item == query_skill:
            my_hero = MyHero(query_skill, MyHero.power, i)
            my_hero.print_hero()
            my_hero.print_skill()
        i += 1
        
        print("__________________________")
        print("\n")
        
if __name__=="__main__":
    main()