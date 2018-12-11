# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght
# Use separate functions for the input and the output


''' Create a new file where the records that are not from Homo sapiens will be written.
Read the file and create a dictionary that associates the header and its sequence. Read headers, if string
'OS = Homo sapiens' appears delete this header and its sequence from the dictionary.
Copy the resulting dictionary on the new file.
Print source organism ('SO = ...') from remaining headers and length of the sequences.'''

#First, create the new file.
end_file = open("not-Homo-sapiens.fasta", "w+")

#Read sprot_prot.fasta
f = open("sprot_prot.fasta")


