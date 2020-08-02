# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:21:46 2020

@author: Kenneth
"""

"""
Import modules.
"""
import sys as sys
import collections as collect

"""
How many records are there in the multi-FASTA file?
Answer: records_count.
"""
#file = open('dna.example.fasta', 'r')
file = open('dna2.fasta', 'r')
seqdata = file.read()
records_count = seqdata.count('>')
file.close

"""
Process the multi-FASTA file.

Build a dictionary pairing the ID of a sequence with its length.
How long are the sequences in the multi-FASTA file?
Answer: seqIDlength.

Build a dictionary pairing the ID of a sequence with the sequence.
Answer: seqIDstring.

Build a dictionary pairing the ID of a sequence with the length of its longest open reading frame.
Parameter: readingframe.
Answer: seqIDorf.
"""
#file = open('dna.example.fasta', 'r')
file = open('dna2.fasta', 'r')
seqdata = file.readlines()
seqID = []
seqlength = []
seqIDlength = {}
seqstring = []
seqIDstring = {}
switch = 0
ID = 'empty'
length = 0
string = ''
for i in seqdata:
    if i.startswith('>') == 1:
        if switch == 0:
            pass
        else:
            seqID.append(ID)
            seqlength.append(length)
            seqIDlength[ID] = length
            seqstring.append(string)
            seqIDstring[ID] = string
        switch = 1
        i = i.replace(">", "")
        i = i.replace(" ", "")
        i = i.replace("\n", "")
        ID = i
        length = 0
        string = ''
    else:
        i = i.replace(" ", "")
        i = i.replace("\n", "")        
        length += len(i)
        string += i
seqID.append(ID)
seqlength.append(length)
seqIDlength[ID] = length
seqstring.append(string)
seqIDstring[ID] = string
file.close()

seqIDorf = {}
readingframe = 3
if readingframe == 1:
    start_index = 0
elif readingframe == 2:
    start_index = 1
elif readingframe == 3:
    start_index =2
for ID, string in seqIDstring.items():
    inorf = 0
    orflength = 0
    maxorflength = 0
    for i in range(start_index, len(string), 3):
        if string[i:i+3] == 'ATG':
           if inorf == 0:
               inorf = 1
               orflength += 3
           else:
               orflength += 3
        elif inorf == 0:
            pass
        elif (string[i:i+3] == 'TAA') or (string[i:i+3] == 'TAG') or (string[i:i+3] == 'TGA'):
            orflength += 3
            if orflength > maxorflength:
                maxorflength = orflength
            inorf = 0
            orflength = 0
        else:
            orflength += 3
    seqIDorf[ID] = maxorflength
    
"""
What is the longest sequence? What is the shortest sequence?
Is there more than one longest or shortest sequence? What are their identifiers?

Answers (longest): maxlength, maxlengthID.
Answers (shortest): minlength, minlengthID. 
"""
minlength = sorted(seqIDlength.values())[0]
minlengthID = []
for ID, length in seqIDlength.items():
    if length == minlength:
        print(ID)
        minlengthID.append(ID)
        
maxlength = sorted(seqIDlength.values(), reverse=True)[0]
maxlengthID = []
for ID, length in seqIDlength.items():
    if length == maxlength:
        print(ID)
        maxlengthID.append(ID)
        
"""
How long is the longest open reading frame in a specific sequence?
Input: The identifier or at least a substring of it.
Answer: specificorf.

How long is the longest open reading frame in the multi-FASTA file? What is the identifier of the sequence containing it?
Answers: maxorflength_overall, maxorfID.

What is the starting position of the longest open reading frame in the sequence that contains it?
Answer: maxorfstart.
"""
specificID = [dummy_ID for dummy_ID in seqID if 'gi|142022655|gb|EQ086233.1|16' in dummy_ID]    
if len(specificID) == 1:        
    specificID = specificID[0]
else:
    sys.exit('The identifier is either wrong or too general.')
specificorf = seqIDorf[specificID]

maxorflength_overall = sorted(seqIDorf.values(), reverse=True)[0]
maxorfID = []
for ID, maxorflength in seqIDorf.items():
    if maxorflength == maxorflength_overall:
        print(ID)
        maxorfID.append(ID)

if len(maxorfID) == 1:        
    dummy_seq = seqIDstring[maxorfID[0]]
else:
    sys.exit('Multiple longest open reading frames in the file.')
inorf = 0
orflength = 0
orfstart = 0
maxorflength = 0
maxorfstart = 0
for i in range(start_index, len(dummy_seq), 3):
    if dummy_seq[i:i+3] == 'ATG':
       if inorf == 0:
           inorf = 1
           orflength += 3
           orfstart = i+1
       else:
           orflength += 3
    elif inorf == 0:
        pass
    elif (dummy_seq[i:i+3] == 'TAA') or (dummy_seq[i:i+3] == 'TAG') or (dummy_seq[i:i+3] == 'TGA'):
        orflength += 3
        if orflength > maxorflength:
            maxorflength = orflength
            maxorfstart = orfstart
        inorf = 0
        orflength = 0
        orfstart = 0
    else:
        orflength += 3
        
"""
What are the repeats of length 'length_repeat' in all sequences in the multi-FASTA file? How many times does each repeat occur in the file?
Parameter: length_repeat.
Answer: repeats.

Which repeat is the most frequent?
Answers: MostRepeat_count, MostRepeat_ID.
"""
length_repeat = 7
motifs = []
for seq in seqstring:
    for i in range(0, len(seq)):
        if (i+length_repeat)<=len(seq):
            motifs.append(seq[i:i+length_repeat])
repeats = collect.Counter(motifs)

MostRepeat_count = sorted(repeats.values(), reverse=True)[0]
MostRepeat_ID = []
for ID, count in repeats.items():
    if count == MostRepeat_count:
        print(ID)
        MostRepeat_ID.append(ID)