#!usr/bin/python3

#To translate a GeneBank formatted file into FASTA formatted file biopython lib can be used
from Bio import SeqIO

#input
gbk_file = open("insulin.gbk")

#output
fasta_file = open("insulin.fasta", 'w')

#Parsing files with biopython
for record in SeqIO.parse(gbk_file, "genbank"):
	info_list = record.description.split()
	organism = str(info_list[0] + ' ' + info_list[1])
	fasta_file.write(">{0}|{1}\n{2}\n".format(record.id, organism, record.seq))

#Close files
gbk_file.close()
fasta_file.close()
