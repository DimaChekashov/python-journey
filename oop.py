class Computer:
    """
    Class for computer
    
    Attributes:
        name (str): Name of the computer
        cpu (str): CPU of the computer
        ram (int): RAM of the computer
        turn_on (bool): Whether the computer is on or off
        
    Methods:
        turn_on(): Turn on the computer
        turn_off(): Turn off the computer
        check_status(): Check the status of the computer
        get_info(): Get information about the computer
    """
    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.is_turn_on = False
        
    @classmethod
    def from_string(cls, string):
        name, cpu, ram = string.split(",")
        return cls(name, cpu, int(ram))
        
    def turn_on(self):
        self.is_turn_on = True
        return "Computer turned on"
        
    def turn_off(self):
        self.is_turn_on = False
        return "Computer turned off"
    
    def check_status(self):
        if self.is_turn_on:
            return "Computer is on"
        else:
            return "Computer is off"
        
    def get_info(self):
        return f"Name: {self.name}\nCPU: {self.cpu}\nRAM: {self.ram}\nStatus: {self.check_status()}"
    
    @staticmethod
    def computer_greeting():
        return "Hello"
    
    def __str__(self):
        return f"Name: {self.name}, CPU: {self.cpu}, RAM: {self.ram}"
    
    def __add__(self, other):
        return Computer(self.name + other.name, self.cpu + other.cpu, self.ram + other.ram)
    
class GamingComputer(Computer):
    def __init__(self, name, cpu, ram, gpu):
        super().__init__(name, cpu, ram)
        self.gpu = gpu
        
    def get_info(self):
        return f"Name: {self.name}\nCPU: {self.cpu}\nRAM: {self.ram}\nGPU: {self.gpu}\nStatus: {self.check_status()}"
    
my_computer = Computer("My Computer", "Intel Core i5", 16)
print(my_computer.__doc__)
print(my_computer.turn_on())
print(my_computer.get_info())

my_computer_2 = Computer.from_string("My Computer 2,Intel Core i5,16")
print(my_computer_2.get_info())

print(Computer.computer_greeting())
print(my_computer)
print(my_computer + my_computer_2)

my_gaming_computer = GamingComputer("My Gaming Computer", "Intel Core i7", 32, "Nvidia RTX 3060")
my_gaming_computer.turn_on()
print(my_gaming_computer.get_info())