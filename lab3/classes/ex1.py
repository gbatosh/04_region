class string:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string = input()
    def printstring(self):
        print(self.string.upper())
string1 = string()
string1.getString()
string1.printstring()
        