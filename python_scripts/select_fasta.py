"""Extract sequences from a .fasta file according to a given list of
protein identifiers. Takes inputs as command-line arguments: 
first, a list of protein identifiers;
second, fasta file.
"""

#!/isr/bin/env python
import sys

def parse_fasta(fasta):
	
  d = {}

  with open(fasta) as f:
    for line in f:
      if line.find(">")==0:
        protein_id = line.split("|")[1]
      else:
        d[protein_id] = d.get(protein_id, "") + line.rstrip()

  return d


if __name__ == "__main__":
  ids = sys.argv[1]
  fasta = sys.argv[2]

  d = parse_fasta(fasta)
  list_id = open(ids).read().rstrip().split("\n")

  for protein_id in list_id:
    if protein_id in d:
      print(">" + protein_id)
      print(d[protein_id])



