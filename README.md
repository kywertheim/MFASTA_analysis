# MFASTA_analysis
This program extracts insights from multi-FASTA files.

How can it do?
1. Count the number of FASTA records in the file.
2. Find out how long the sequences in the file are.
3. Characterise the longest and shortest sequences in the file, including the lengths and identifiers.
4. Find out the length of the longest open reading frame in a specific sequence.
5. Characterise the longest open reading frame in the file, including its length, the identifier of the containing sequence, and its starting position in the sequence.
6. Identify the repeats of a specified length in the file and count how many times each repeat occurs in the file.
7. Identify the most frequent repeat.

Software:
1. Python 3.7.
2. Python module sys is needed to terminate the program when there is an error.
3. Python module collections is needed to count repeats in the sequences.

Input file: A multi-FASTA file containing multiple DNA sequences in the FASTA format. Two examples (dna2.fasta and dna.example.fasta) are provided.

Configurations:
1. readingframe.
2. length_repeat.
3. If the user wants to find out the length of the longest open reading frame in a specific sequence, they must provide the identifier or at least a substring of it.
