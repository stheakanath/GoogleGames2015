content = []
fname = "test.in"
with open(fname) as f:
    content = f.readlines()
content = [x.strip('\n') for x in content] 

shifted = []

for elem in content:
	if len(elem) == 5:
		shifted.append(elem)

print(shifted)