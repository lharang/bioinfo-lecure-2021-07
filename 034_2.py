#!/usr/bin/python

data = dict()

with open("covid19.fasta", "r") as handle:
	for line in handle:
		if line.startswith(">"):
			continue
		for base in line.strip(): #AACG
			if base not in data:
				data[base] = 0
			data[base] += 1

print(f"A: {data['A']}")
print(f"A: {data['C']}")
print(f"A: {data['G']}")
print(f"A: {data['T']}")
print(data)

