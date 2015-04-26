import string 

x = "V O I U L E Q Y A H X J N B T W G C Z D S M P F K R".split()

print("LETTERS TO GO")
for elem in list(string.ascii_uppercase):
	if elem not in x:
		print(elem)
