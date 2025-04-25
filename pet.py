class Pet:
    """
    A simple Pet class that tracks name, hunger, energy, and happiness levels.
    Bonus methods for training and showing tricks.
    """
    def __init__(self, name):
        self.name = name
        self.hunger = 5       # 0 = full, 10 = very hungry
        self.energy = 5       # 0 = tired, 10 = fully rested
        self.happiness = 5    # 0 = unhappy, 10 = very happy
        self.tricks = []      # List to store learned tricks

    def eat(self):
        """
        Reduces hunger by 3 (not below 0) and increases happiness by 1.
        """
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} ate and now has hunger {self.hunger} and happiness {self.happiness}.")

    def sleep(self):
        """
        Increases energy by 5 (not above 10).
        """
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} slept and now has energy {self.energy}.")

    def play(self):
        """
        Decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        """
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)
        print(f"{self.name} played and now has energy {self.energy}, happiness {self.happiness}, and hunger {self.hunger}.")

    def get_status(self):
        """
        Prints the current state of the pet.
        """
        status = (
            f"Name: {self.name}\n"
            f"Hunger: {self.hunger}/10\n"
            f"Energy: {self.energy}/10\n"
            f"Happiness: {self.happiness}/10\n"
        )
        print(status)

    def train(self, trick):
        """
        Teaches the pet a new trick and stores it.
        """
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """
        Prints all learned tricks.
        """
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")


if __name__ == "__main__":
    # Example usage
    pet = Pet("Buddy")
    pet.get_status()
    pet.eat()
    pet.play()
    pet.sleep()
    pet.train("roll over")
    pet.train("fetch")
    pet.show_tricks()
    pet.get_status()
