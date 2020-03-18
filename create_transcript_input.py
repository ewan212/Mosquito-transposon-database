
import os
from Bio import SeqIO

t = open("transcript_input.csv", 'w')

def parse_record(records):
	for record in records:
		sequence = record.seq
		length = len(sequence)
		t.writelines(sequence + ',' + str(length) + '\n')
	print("done parsing")

parse_record(records = SeqIO.parse("Repeats_AeAlbo.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_AeAeg.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_CuQuin.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_AnGam.fa.txt", "fasta"))

t.close()
