

# Instance Attributes
class Human:
    def __init__(self, name, age, gender, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby

    def display_info(self):
        return f"{self.name} is a {self.age} year old {self.gender} who enjoys {self.hobby}"
Nathan = Human("Nathan", 60, "Male", "reading")

print(Nathan.display_info()) 
