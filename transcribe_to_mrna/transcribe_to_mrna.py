def dna_to_rna(dna):
    target = "ATGC"
    replace_with = "UACG"
    table = dna.maketrans(target, replace_with)

    return dna.translate(table)


def dna_to_rna(dna):
    return dna.translate(str.maketrans('ATGC', 'UACG'))


mapping = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}


def dna_to_rna(dna):
    return ''.join([mapping[c] for c in dna])


def dna_to_rna(dna):
    return (
        dna.replace('A', 'U')
        .replace('T', 'A')
        .replace('C', 'X')
        .replace('G', 'C')
        .replace('X', 'G'))
