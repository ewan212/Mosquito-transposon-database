# Mosquito Transposon Database
# Contributors:
- Simran Makwana simranmakw@gmail.com makwana@bu.edu
- Daisy Han daisyhan@bu.edu
- Evie Wan ewan212@bu.edu
- Nick Mosca njmosca@bu.edu

## Project Overview
This project aims to create a website that will serve as a search tool for mosquito transposable elements(transposons) for scientists in Dr. Nelson Lau's Lab at Boston University Medical School. Users will be able to search for transposons based on different classification criteria and compare them within four closely related mosquito species.  

## Workflow 
1) Meet with Dr.Lau and team to discuss project objectives, use cases, and transposon research. Brainstorm website interface and database structure. 
2) Parse FASTA sequencing files and extract the following information: species, accession number, type of transposon (class, order, superfamily), description (if applicable), length of sequence, and number of copies. 
3) 



# Repository Contents:
parse_fasta.py: given fasta files, use SeqIO to parse fasta files and save elements in separate files
create_transposon_input.py: given fasta files, create csv file used to populate "transposon" table 
