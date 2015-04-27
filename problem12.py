f = open('ships', 'r')

coordinates = [[float(x) for x in line.split()] for line in f]

def findDistance(p1, p2):
	return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

maxCount = 0
for i in range(len(coordinates)):
	count = 0
	for j in range(len(coordinates)):
		if findDistance(coordinates[i], coordinates[j]) < 100:
			count += 1
	if count > maxCount:
		maxCount = count
print(maxCount)
