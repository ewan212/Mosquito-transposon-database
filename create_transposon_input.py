
import os
from Bio import SeqIO

t = open("transposon_input.csv", 'w')

def classify_class(header):
	header = header.upper()
	if "DNA" in header:
		return "DNA"
	elif "RNA" in header:
		return "RNA"
	elif "RETROPOSON" in header:
		return "RETROPOSON"
	else:
		return "OTHER"

def classify_order(header):
	header = header.replace("ltr", '')
	header = header.upper()
	header = header.replace("MULTIPLE", '')
	if "CMC" in header:
		return "CMC"
	elif "DIRS" in header:
		return "DIRS"
	elif "PLE" in header:
		return "PLE"
	elif "SINE" in header:
		return "SINE"
	elif "LINE" in header:
		return "LINE"
	elif "MITE" in header:
		return "MITE"
	elif "TIR" in header:
		return "TIR"
	elif "CRYPTON" in header:
		return "CRYPTON"
	elif "HELITRON" in header:
		return "HELITRON"
	elif "MAV" in header:
		return "MAVERICK"
	elif "LTR" in header:
		return "LTR"
	else:
		return "OTHER"

def classify_superfamily(header):
	header = header.upper()
	if "COPIA" in header:
		return "COPIA"
	elif "GYPSY" in header:
		return "GYPSY"
	elif "PAO" in header or "BEL" in header:
		return "BEL-PAO"
	elif "RETROVIRUS" in header:
		return "RETROVIRUS"
	elif "ERV" in header:
		return "RETROVIRUS"
	elif "NGARO" in header:
		return "NGARO"
	elif "VIPER" in header:
		return "VIPER"
	elif "DIRS" in header:
		return "DIRS"
	elif "PENELOPE" in header:
		return "PENELOPE"
	elif "R2" in header:
		return "R2"
	elif "RTE" in header:
		return "RTE"
	elif "JOCKEY" in header:
		return "JOCKEY"
	elif "L1" in header:
		return "L1"
	elif "TRNA" in header:
		return "TRNA"
	elif "7SL" in header:
		return "7SL"
	elif "5S" in header:
		return "5S"
	elif "SVA" in header:
		return "SVA"
	elif "RETROGENES" in header:
		return "RETROGENES"
	elif "MARINER" in header:
		return "TC1-MARINER"
	elif "HAT" in header:
		return "HAT"
	elif "MUTATOR" in header:
		return "MUTATOR"
	elif "MERLIN" in header:
		return "MERLIN"
	elif "TRANSIB" in header:
		return "TRANSIB"
	elif "PIG" in header:
		return "PIGGYBAC"
	elif ("PIF" in header) or ("HARBINGER" in header):
		return "PIF-HARBINGER"
	elif "CACTA" in header:
		return "CACTA"
	elif "CRYPTON" in header:
		return "CRYPTON"
	elif "HELITRON" in header:
		return "HELITRON"
	elif "MAV" in header:
		return "MAVERICK"
	elif "CR1" in header:
		return "CR1"
	elif "CRACK" in header:
		return "CRACK"
	elif "DONG" in header:
		return "DONGR4"
	elif "NIMB" in header:
		return "NIMB"
	elif "ZENON" in header:
		return "ZENON"
	elif "KIRI" in header:
		return "KIRI"
	elif "KOLOBOK" in header:
		return "KOLOBOK"
	elif "OUTCAST" in header:
		return "OUTCAST"
	elif "BLASTOPIA" in header:
		return "BLASTOPIA"
	elif "CER" in header:
		return "CER"
	elif "DIVER" in header:
		return "DIVER"
	elif "DM412" in header:
		return "DM412"
	elif "DOC" in header:
		return "DOC"
	elif "EAL" in header:
		return "EAL"
	elif "ISL2EU" in header:
		return "ISL2EU"
	elif "J1" in header:
		return "J1"
	elif "R1" in header:
		return "R1"
	elif "SOLA" in header:
		return "SOLA"
	elif "STALKER" in header:
		return "STALKER"
	elif "ZAM" in header:
		return "ZAM"
	elif "ZATOR" in header:
		return "ZATOR"
	else:
		return "OTHER"

def reclassify_order(superfamily):
	if superfamily in ["COPIA", "GYPSY", "BEL-PAO", "RETROVIRUS", "ERV"]:
		return "LTR"
	elif superfamily in ["DIRS", "NGARO", "VIPER"]:
		return "DIRS"
	elif superfamily in ["PENELOPE"]:
		return "PLE"
	elif superfamily in ["R2", "RTE", "JOCKEY", "L1"]:
		return "LINE"
	elif superfamily in ["TRNA", "7SL", "5S", "SVA", "RETROGENES"]:
		return "SINE"
	elif superfamily in ["MARINER", "HAT", "MUTATOR", "MERLIN", "TRANSIB", "PIGGYBAC", "PIF-HARBINGER", "CACTA"]:
		return "TIR"
	elif superfamily in ["CRYPTON"]:
		return "CRYPTON"
	elif superfamily in ["HELITRON"]:
		return "HELITRON"
	elif superfamily in ["MAVERICK"]:
		return "MAVERICK"
	else:
		return "OTHER"

def reclassify_class(order):
	if order in ["LTR", "DIRS", "PLE", "LINE", "SINE"]:
		return "RNA"
	elif order in ["TIR", "CRYPTON", "HELITRON", "MAVERICK"]:
		return "DNA"
	else:
		return "OTHER"


def parse_record(records):
	for record in records:
		header = record.description
		# remove commas from header so they don't mess with csv format
		header = header.replace(',', '')
		myclass = classify_class(header)
		order = classify_order(header)
		superfamily = classify_superfamily(header)
		# if superfamily was found and order was not found, classify order
		if (superfamily != "OTHER" and order == "OTHER"):
			order = reclassify_order(superfamily)
		# if order was found and class was not found, classify class
		if (order != "OTHER" and myclass == "OTHER"):
			myclass = reclassify_class(order)
		sequence = record.seq
		length = str(len(sequence))
		t.writelines(myclass + ',' + order + ',' + superfamily + ',' + header + ',' + sequence + ',' + length + '\n')
	print("done parsing")


parse_record(records = SeqIO.parse("Repeats_AeAlbo.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_AeAeg.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_CuQuin.fa.txt", "fasta"))
parse_record(records = SeqIO.parse("Repeats_AnGam.fa.txt", "fasta"))

t.close()
