"""
    Use built-in abc to implement Abstract classes and methods
    used for the Command Pattern
"""
from abc import ABC

""" Class Dedicated to Command"""
class Command(ABC):

    """constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver
    
    """process method"""
    def process(self):
        pass

""" Class dedicated to Command Implementation"""
class CommandImplementation(Command):

    """ constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver
    
    """process method"""
    def process(self):
        self.receiver.perform_action()

"""Class dedicated to Receiver"""
class Receiver:
    """consturctor method"""
    def __init__(self, data):
        self.data = data
    
    """perform action"""
    def perform_action(self):
        num1_hex = hex(self.data.num1)
        num2_hex = hex(self.data.num2)
        sum_hex = hex(int(num1_hex, 16) + int(num2_hex, 16))
        print('sum = ' + str(int(sum_hex, 16)))

"""Class dedicated to Invoker"""
class Invoker:

    """command method"""
    def command(self, cmd):
        self.cmd = cmd
    
    """execute method"""
    def execute(self):
        self.cmd.process()

"""
    Data Transfer Object for the Commands.
    Setters use Builder to return self
"""
class AdditionData:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
    
    # make the getter method
    def get_num1(self):
        return self.num1
    
    # make the setter method
    def set_num1(self, num1):
        self.num1 = num1
        return self
    
    # make the getter method
    def get_num2(self):
        return self.num1
    
    # make the setter method
    def set_num2(self, num2):
        self.num2 = num2
        return self

"""main method"""
if __name__ == '__main__':

    """Create Receiver object"""
    data = AdditionData()
    data.set_num1(1).set_num2(1)
    receiver = Receiver(data)
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
