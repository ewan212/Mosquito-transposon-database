
#speciesid, tid (accession), transposon, count, coverage, frequency(?)
# AeAlbo = 1, AeAeg = 2, CuQuin = 3, AnGam = 4

# open file for writing
t = open('relationship_input.csv', 'w')

def match_counts(species, species_id):
    # load the transposon file
    transposon_input = open('transposon_input.csv', 'r')
    # load their count file
    c = open(species + '_TE_count.txt', 'r')
    # ignore header line
    c.readline()
    # for each transposon
    for tpn in c:
        count_info = tpn.split('\t')
        transposon = count_info[0]
        # for each entry in transposon file
        for entry in transposon_input:
            e = entry.split(',')
            header = e[3].strip()
            if transposon in header:
                species = str(species_id)
                tid = e[0]
                count = count_info[1]
                coverage = count_info[2]
                transposon_input.seek(0)
                #print(transposon, '\t', header, '\t', species)
                t.writelines(species + ',' + tid + ',' + count + ',' + coverage + '\n')
                break

    c.close()
    transposon_input.close()

match_counts('AeAlbo', 1)
match_counts('AeAeg', 2)
match_counts('CuQuin', 3)
match_counts('AnGam', 4)

t.close()
