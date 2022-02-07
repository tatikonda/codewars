def DNA_strand(dna):
    key = "ATGC"
    val = "TACG"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in dna)

print(DNA_strand("AAAA"))