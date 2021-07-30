
with_open("test.txt", "r") as handle:
	for line in handle:
		print(line.strip())
