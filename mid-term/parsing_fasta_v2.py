def parse_organism(line):
    l1 = line.split("OS=")
    l2 = l1[1].split()
    species_list = [l2[0], l2[1]]
    org = " ".join(species_list)
    return org


f = open("sprot_prot.fasta")    
output = open("output.fasta", 'w')   
seq_list = []       
head_list = []

for line in f:
    if line.startswith('>'):          
        head_list.append(line.rstrip())
        seq_list.append(" ")
    else:                       
        seq_list.append(line.rstrip())

seq_string = "".join(seq_list)  
sequences = seq_string.split()  


for head in head_list:
    organism = parse_organism(head)
    if organism != "Homo sapiens":
        i = head_list.index(head)
        output.write("{0}\n{1}\n".format(head_list[i], sequences[i])) 
        print(organism)
        print(len(sequences[i]))

f.close()
output.close()
