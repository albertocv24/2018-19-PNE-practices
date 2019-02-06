#Exercise 5 from session 5. Repeat the exercise 4, but now the sequences should be read from an exdternal file that
#can have sequences in separated lines


def ex5_dna():
    with open('DNA.txt', 'r') as f:
        seq=[]
        for row in f:
            seq.append(row)

        seq=''.join(seq)
        seq=seq.lower()
        seq.replace('\n', '')

        number=len(seq)

        a=seq.count('a')
        c=seq.count('c')
        t=seq.count('t')
        g=se.count('g')

        print('Total length: ', number)
        print('A:', a)
        print('C:', c)
        print('T:', t)
        print('G:', g)

        f.close()
    return

    ex5_dna()