from character import Character
import random

CHOICES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

def ask_choice(prompt):
    """Asks the user to choose one of the provided choices.

    Parameters
    ----------
    prompt: str
        The question to ask the user.
    choices: list or set
        The options the user can choose from. Each choice can be a string, or any other type
        as long as it can be converted to a string (using an `__str__` method).

    Returns
    -------
    The selected item out of choices.
    """
    choices = CHOICES
    while True:
        print(prompt)
        if not len(choices):
            print("No options")
            return
        for index, choice in enumerate(choices):
            print(f"{index+1}. {str(choice).capitalize()}")
        index = ask_int("> ") - 1
        if 0 <= index < len(choices):
            return choices[index]

def ask_int(prompt="", min_value=None, max_value=None):
    """Like `input()`, but keeps repeating the question until the user enters a non-negative integer,
    that lies between the given boundaries.

    Parameters
    ----------
    prompt: str
        The question to ask the user.
    min_value: int or None
        An optional minimum allowed value (inclusive).
    max_value: int or None
        An optional maximum allowed value (inclusive).

    Returns
    -------
    int
        The value entered by the user.
    """
    while True:
        result = input(prompt)
        if result.isdigit():
            result = int(result)
            if (min_value==None or result >=min_value) and (max_value==None or result<=max_value):
                return result

def roll_dice(message:str) -> int:
    input(f"please roll the dice to determine your {message}")
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    dice_rolls.remove(min(dice_rolls))

    return sum(dice_rolls)

class Game:
    def __init__(self):
        name = input("What is your name? ")
        classtype = ask_choice("As what class do you want to play?")
        strength = roll_dice("strength")
        dexterity = roll_dice("dexterity")
        constitution = roll_dice("constitution")
        intelligence = roll_dice("intelligence")
        wisdom = roll_dice("wisdom")
        charisma = roll_dice("charisma")

        self.player = Character(name, classtype, strength, dexterity, constitution, intelligence, wisdom, charisma)
    
    def run(self):
        turn = 0


if __name__ == "__main__":
    game = Game()
    game.run()
