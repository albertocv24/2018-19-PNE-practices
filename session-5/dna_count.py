class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New sequence is already created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq
       All the objects of class Gene will
       inheritance the methods from Seq Class"""


#this are the sequences
s1 = Gene("ATTCGATCC")
s2 = Seq("AAAGG")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("First sequence: {}".format(str1))
print("Length 1: {}".format(l1))
print("Second sequence: {}".format(str2))
print("Length 2: ·{}".format(l2))

print("the end")
