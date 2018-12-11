# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght
# Use separate functions for the input and the output


''' Create a new file where the records that are not from Homo sapiens will be written.
Read the file. In fasta files headers are marked with "<". Read headers, if string
'Homo sapiens' does not appear copy the header and following sequence on the new file.
Print source organism ('SO = ...') from headers and length of the sequences.'''

#Read sprot_prot.fasta
fasta = open("sprot_prot.fasta")

#Create the new file
output = open("not_homo_sapiens.fasta", "w")

seq = ''
for line in fasta:
  if line[0]=='>':
    if seq:
      if "Homo sapiens" not in header:
        output.write(header + seq)
    header = line
    seq = ''
  else:
    seq = seq + line

output.close()



