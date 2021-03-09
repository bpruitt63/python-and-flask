"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        '''sets start number and generator number'''
        self.start = start
        self.num = start - 1

    def generate(self):
        '''increments generator number and returns it'''
        self.num = self.num + 1
        return self.num

    def reset(self):
        '''sets generator number back to start number'''
        self.num = self.start - 1

