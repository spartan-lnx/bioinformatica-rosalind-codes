dna_sequence = "ACGCCTAGGTTTCAGACGCAAGCACATCGGGAACATACCGGCCACGGAGCCGGACCGTTGCAGTCACCGTCGTGACGTACGGGATTATGGCACTTCGATTCTCTCGACCGCTACCACTCGGATGATGTATACTTGAATCTATACGGCTATTAGCGTAGACGGTTTGCTGGTTTTGCTACCCGCGTCTCTTAATAGATATTTGGCCGGTTCTGAGGAAGCTCGTTGAACGAATCTTTCGGAGCGATGTCGCACCTGCCACTACAGTATCTAGCGACAGCTTGATTCAGGAAGGAACCATCAGAACTAGAAGTTCAGTGAACCAATCCTTCAGCCGTGTAGGGCCACTGGCACTCGCGAATCCAAGTGAGGCATGCGGGCTTGCGCGGTTTTATAAGAAGGACAAGTTAGGTCAGTATAGGTATGAAATAAATCCTGCACTGGGTCACTAAGTTCGCGGCAACGCGCTGCAGGAGGTGTGATTACGGCGACAAAGTTAACGCCTATTTCTACGTAGTTGTGAACGAACCTAGGGGAACAAGACCTCCGAGTCGGAGGTGGTTTCAAAGTATTCGTTTACGAGCCTTTCGCCCCTTCCTGGGCATCGCATGGTTAGACACCGTCTTGGCCTGACGGGAAACCGGGCATATACTCTCAGAAACTACCTGGTTACCCAGTCAATTGCCTCGCGTGTTGTTTAAACGAGGTATCCACGACACTAGGCGAGGGAGGTAAGCTTTGCTCATGACCGGATTGCACGTCGTTGAATTAGCATTTGAGAGGTCTCGTCCCCAAGCCACTGACCATTTGGGCTATAGGGACAGCATGTGCGCCATAAAAAACGACTACTAGGAAGACTGTGGGAGTCCTCCACGTCCCAGAAAGAAGTGATATTTGCGCTTGCTATTAAGTACCGCACTAGTTTAAGGCTGGATCACTGGCCAACGTGCAGATCCTTCCTGACGATCAGGGTATGGTTAACTCAAAGCCGCTATCCGCAACT"
rna_sequence = ""

for nucleotide in dna_sequence:
    if nucleotide == 'T':
        rna_sequence += 'U'
    else:
        rna_sequence += nucleotide

print(rna_sequence)

