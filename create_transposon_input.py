
import os
from Bio import SeqIO

t = open("transposon_input.csv", 'w')

def classify_type(header):
	header = header.upper()
	if "DNA" in header:
		return "DNA"
	elif "RNA" in header:
		return "RNA"
	elif "UNKNOWN" in header:
		return "UNKNOWN"
	else:
		return "OTHER"

def classify_name(header):
	header = header.upper()
	if "LTR" in header:
		return "LTR"
	elif "SINE" in header:
		return "SINE"
	elif "LINE" in header:
		return "LINE"
	elif "MITE" in header:
		return "MITE"
	else:
		return "OTHER"


def parse_record(records):
	for record in records:
		accession = record.id
		header = record.description
		# remove commas from header so they don't mess with csv format
		header = header.replace(',', '')
		type = classify_type(header)
		name = classify_name(header)
		t.writelines(accession + ',' + type + ',' + name + ',' + header + '\n')
	print("done parsing")


parse_record(records = SeqIO.parse("Repeats_AeAlbo.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_AeAeg.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_CuQuin.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_AnGam.fa.txt", "fasta"))

t.close()
