
import os
from Bio import SeqIO

def write_fasta_elements(file, species):

	records = SeqIO.parse(file, "fasta")

	id = open(species + '_id.txt', 'w')
	name = open(species + '_name.txt', 'w')
	description = open(species + '_description.txt', 'w')
	num_feats = open(species + '_num_feats.txt', 'w')
	seq = open(species + '_seq.txt', 'w')

	for record in records:
		id.writelines(record.id + ' \n')
		name.writelines(record.name + '\n')
		description.writelines(record.description + '\n')
		num_feats.writelines(record.features)
		seq.writelines(record.seq + '\n')

	id.close()
	name.close()
	description.close()
	num_feats.close()
	seq.close()

	print("done parsing", species)

write_fasta_elements(file = "Repeats_AeAlbo.fa.txt", species = "AeAlbo")
write_fasta_elements(file = "Repeats_AeAeg.fa.txt", species = "AeAeg")
write_fasta_elements(file = "Repeats_AnGam.fa.txt", species = "AnGam")
write_fasta_elements(file = "Repeats_CuQuin.fa.txt", species = "CuQuin")
