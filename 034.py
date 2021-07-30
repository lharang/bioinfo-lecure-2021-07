l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

print(max(l))
print(min(l))

max_val = l[0]
min_val = l[0]

for i in l:
	if i > max_val:
		max_val = i
	if i < min_val:
		max_val = i

print(max_val, min_val)
