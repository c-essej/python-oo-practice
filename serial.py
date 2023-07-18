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
        """create a generator with a start number and a resetpoint"""
        self.lastnumber = start -1
        self.nextnumber = start
        self.startingpoint = start

    def __repr__(self):
        return f"<SerialGenerator resetpoint={self.startingpoint} number={self.lastnumber}>"

    def generate(self):
        """increments start number by 1 and returns"""
        self.lastnumber += 1
        self.nextnumber += 1
        return self.lastnumber

    def reset(self):
        """resets the number back to start point"""
        self.lastnumber = self.startingpoint - 1