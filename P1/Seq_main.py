#The main program is located in the file: Seq_main.py
#The main program should create 4 sequences. The first two are created directly my invoking the Seq method with their
# string sequence


from Seq import Seq


seq1 = Seq('ACGGGACGGTACGTTTAACCCT')
seq2 = Seq('TGCATCCGAGATAAAGGGTTTA')
seq3 = Seq.complement(seq1)
seq4 = Seq.reverse(seq3)

ls = [seq1, seq2, seq3, seq4]
number = 1

for sequence in ls:
    print('\n')
    print('Sequence {} : {}'.format(number, sequence.strbases))
    print(' Length: {}'.format(len(sequence.strbases)))
    print(' Bases count: A:{}, C :{}, G:{}, T:{} '.format(sequence.count('A'), sequence.count('C'),
        sequence.count('G'), sequence.count('T')))
    print(' Bases percentage: A:{}, C:{}, G:{}, T:{} '.format(sequence.perc('A'), sequence.perc('C'),
        sequence.perc('G'), sequence.perc('T')))
    number += 1



