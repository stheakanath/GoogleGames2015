fname = "clothes"
content = []
with open(fname) as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]

shirt = []
pants = []
onshirt = True
for elem in content:
	if elem == 'Pants':
		onshirt = False
	if onshirt:
		shirt.append(elem.split())
	else:
		pants.append(elem.split())

pants = pants[1:]
shirt = shirt[1:]

#for ccalculation nwo

total = 0
for pant in pants:
	for s in shirt:
		panthue = float(pant[0])
		shirthue = float(s[0])
		if (panthue > shirthue):
			difference1 = abs(panthue - shirthue)
			difference2 = abs(360 + shirthue - panthue)
		else:
			difference1 = abs(shirthue - panthue)
			difference2 = abs(360 + panthue - shirthue)
		op1 = difference1 >= 110 and difference1 <= 130 or difference1 >= 170 and difference1 <= 190 or difference1 >= 230 and difference1 <= 250
		op2 = difference2 >= 110 and difference2 <= 130 or difference2 >= 170 and difference2 <= 190 or difference2 >= 230 and difference2 <= 250

		
		
		if (abs(float(pant[1]) - float(s[1])) <= 10 and abs(float(pant[2]) - float(s[2])) <= 10 and op1 and op2):
			total += 1

print (total)