class Character:
    def __init__(self, name, classtype, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.__name = name
        self.__classtype = classtype
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constitution = constitution
        self.__intelligence = intelligence
        self.__wisdom = wisdom
        self.__charisma = charisma


    def get_name(self):
        self.__name

    def __str__(self) -> str:
        return f"{get_name()}"
