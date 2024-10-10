# Author: Abdou Diakite
# Date: 10/10/2024
# Description: This code defines a Flower class and creates instances of the Flower Class, demonstrating object-oriented programming concepts, such as define a class, creating objects and using methods.

class Flower:
    # Method to initialize the flower's name
    def __init__(self, name):
        self.name = name  # Attribute to store the name of the flower

    # Method to simulate the flower growing
    def grow(self):
        print("The " + self.name + " is growing.")  # Prints a message indicating the flower is growing

    # Method to simulate the flower blooming
    def bloom(self):
        print("The " + self.name + " is blooming.")  # Prints a message indicating the flower is blooming

def main():
    # Creating an instance of Flower with the name "Rose"
    flower1 = Flower("Rose")
    flower1.grow()  # Calling the grow method for flower1
    flower1.bloom()  # Calling the bloom method for flower1

    # Creating another instance of Flower with the name "Daisy"
    flower2 = Flower("Daisy")
    flower2.grow()  # Calling the grow method for flower2
    flower2.bloom()  # Calling the bloom method for flower2

 # Creating another instance of Flower with the name "Jasmine"
    flower3 = Flower("Jasmine")
    flower3.grow()  # Calling the grow method for flower3
    flower3.bloom()  # Calling the bloom method for flower3


# The entry point of the program
if __name__ == "__main__":
    main()  # Calling the main function to execute the program
