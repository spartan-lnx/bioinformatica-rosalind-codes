dna_strings = {}
label = ''

with open('data.txt') as f:
    lines = f.readlines()
    last = lines[-1]
    for line in lines[:-1]:
        if line[:9] == '>Rosalind':
            label = line[1:-1]
            dna_strings[label] = ''
        else:
            dna_strings[label] += line[:-1]
    dna_strings[label] += last

best_label = ''
best_score = 0

for key,value in dna_strings.items():
    cg_count = 0
    total_nucleotides = len(value)
    for nucleotide in value:
        if nucleotide == 'C' or nucleotide == 'G':
            cg_count += 1
    if (cg_count/total_nucleotides) * 100 > best_score:
        best_label = key
        best_score = (cg_count/total_nucleotides) * 100

print(best_label)
print(best_score)
