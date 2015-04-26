import string

fname = "wordlist"
words = []
with open(fname) as f:
    words = f.readlines()
words = [x.strip('\n') for x in words]


fname = "soup"
needtofind = []
with open(fname) as f:
    needtofind = f.readlines()
needtofind = [x.strip('\n') for x in needtofind]

alphabet = list(string.ascii_uppercase)
total = 0
for elem in needtofind:
	tmp = elem
	longest = 0
	for letter in alphabet:
		tmp = tmp.replace('_', letter)
		for word in words:
			if word in tmp:
				if len(word) > longest:
					longest = len(word)
		tmp = elem
	total += longest
print(total)


	