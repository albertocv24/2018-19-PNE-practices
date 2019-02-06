#Create a program for counting the number of bases presented in a DNA sequence.


seq= input('Please insert a DNA sequence: ')

def dna_count(seq):

    seq= seq.lower()
    number=len(seq)

    a=seq.count('a')
    c=seq.count('c')
    t=seq.count('t')
    g=seq.count('g')

    print('Total length: ', number)
    print('A:', a)
    print('C:', c)
    print('T:', t)
    print('G:', g)

    return

dna_count(seq)