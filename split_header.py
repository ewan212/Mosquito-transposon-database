

# for AnGam
file = open('AnGam_id.txt', 'r')
out = open('AnGam_transposon.txt', 'w')
# for each of the IDs that we pulled out before
for line in file:
    # split by @ and save 'transposon name'
    out.writelines(((line.strip()).split('@')[1]) + '\n')
out.close()
