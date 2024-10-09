import os, time

os.system("clear")

title = "MakeBEast"


beast = {}

def prettyPrint():
    print(f"NAME\tTYPE\tHP\tMP")
    for key, value in beast.items():
      print(f"""{key: ^5}|{value["Type"]: ^8}|{value["HP"]: ^6}|{value["HP"]: ^6}""")

print("----MOKEBEAST----")
while True:
    name = input("Name > ")
    type = input("Type > ")
    hp = input("HP > ")
    mp = input("MP > ") 

    beast[name] = {"Type": type, "HP": hp, "MP": mp}
    

    prettyPrint()
    time.sleep(3)
    os.system("clear")
    print("----MOKEBEAST----")





