# Mosquito Transposon Database
https://laulab.bu.edu/MTD/ 

# Contributors:
- Simran Makwana simranmakw@gmail.com makwana@bu.edu
- Daisy Han daisyhan@bu.edu
- Evie Wan ewan212@bu.edu
- Nick Mosca njmosca@bu.edu

Search by Species Function: Simran Makwana <br/>
Search by Class Function: Evie Wan <br/>
Search by Transposon Order Function: Daisy Han <br/>
Browse Page: Simran Makwana <br/>
Help page: Evie Wan <br/>
About page: Nick Mosca <br/>

## Project Overview
This project aims to create a website that will serve as a search tool for mosquito transposable elements(transposons) for scientists in Dr. Nelson Lau's Lab at Boston University Medical School. Users will be able to search for transposons based on different classification criteria and compare them within four closely related mosquito species.  

## Workflow 
1) Meet with Dr.Lau and team to discuss project objectives and use cases. Brainstorm website interface and database structure. 
2) Parse FASTA sequencing files and extract the following information: species, accession number, type of transposon (class, order, superfamily), description (if applicable), length of sequence, and number of copies. 
3) Develop search functions (search by species/class/order) - Python CGI, SQL queries, Ajax, JavaScript
4) Develop visualization function - Google chart API
5) Web Development: finalize web interface using HTML, CSS, and Bootstrap. 



# Repository Contents:
parse_fasta.py: given fasta files, use SeqIO to parse fasta files and save elements in separate files
create_transposon_input.py: given fasta files, create csv file used to populate "transposon" table 
transposon_order_page_daisy.py: search by transposon order function
transposon_class_page_evie.py: search by transposon class function
webpage_copy_simran.py: search by species function
explore_page.py: Browse page 
DL_webpage_draft_1.py: download files function
help_page_evie.py: help page
