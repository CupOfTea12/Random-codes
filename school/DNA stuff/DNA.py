"""
------------------------------------------------------------------------------------
Code by Rebeca Martinakkova
II.IT 2021
DNA comparing
-Added two small features:
 >input the two DNA sequences
 >delay so it looks a bit more realistic
-SOMETHING ABOUT DNA SEQUENCES > https://en.wikipedia.org/wiki/Nucleic_acid_sequence
                               > https://en.wikipedia.org/wiki/DNA_sequencing
Examples to try>
1 a} TGGAGGCAATGGCGGCCAGCA
  b} GACTCCTCCTCCTCCTGCTCA

2 a} AATCCGCTAG
  b} AAACCCTTAG

3 a} AGGUCT
  b} CGCGUT
------------------------------------------------------------------------------------
"""
#---LIBRARIES---
import time

#---Variabiles---
#DNA sequences
sequence_a = input(str("Enter the first DNA sequence>>"))
sequence_b = input(str("Enter the second DNA sequence>>>"))
print("Calculating the lenght of the first sequence...")
time.sleep(3)
print("Calculating the lenght of the second sequence...")
time.sleep(3)
#lenghts of DNA sequences
len_a = len(sequence_a)
len_b = len(sequence_b)

#---PRINTS---
#printing out the lenght
print("-----LENGHT-OF-DNA-SEQUENCES-----")
time.sleep(2)
print("Length of Sequence A: " + str(len_a))
time.sleep(2)
print() #empty line
print("Length of Sequence B: " + str(len_b))
time.sleep(2)
print() #empty line
print("Comparing the DNA sequences....")
time.sleep(5)
print("-----COMPARING-SUCCESSFUL-----")
time.sleep(3)
#---FUNCTIONS-AND-METHODS---
#function for comparing the DNA mutation
#to look like a specialist, i added the mismatches so it looks like code from the biolab
def sequence_compare(seq_a, seq_b):
        len1 = len(seq_a)
        len2 = len(seq_b)
        mismatches = []
        for pos in range (0, min(len1, len2)) :
              if seq_a[pos] != seq_b[pos]:
                  #if mutation -> append |
                  mismatches.append('|')
              else:
                  #no mutation-> just go ahead
                  mismatches.append(' ')
        print (seq_a)
        print ("".join(mismatches))
        print (seq_b)

sequence_compare(sequence_a,sequence_b)
