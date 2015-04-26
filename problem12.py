import math

cords = []
with open("ships") as f:
    cords = f.readlines()
cords = [[float(y) for y in x.strip('\n').split()] for x in cords] 

def hitmore(shipcord1, shipcord2, exploded):
	distance = math.sqrt((shipcord1[0]-shipcord2[0]) ** 2 + (shipcord1[1] - shipcord2[1]) ** 2 + (shipcord1[2] - shipcord2[2]) ** 2)
	if shipcord2 in exploded or distance > 100:
		return 0
	else:
		return 1 + max(hitmore(shipcord2, [x for x in exploded], exploded.append(shipcord2)))

max_num = 0
for elem in cords:
	exploded = [elem]
	this_obj = 0
	for check_others in cords:
		if check_others not in exploded:
			distance = math.sqrt((elem[0]-check_others[0]) ** 2 + (elem[1] - check_others[1]) ** 2 + (elem[2] - check_others[2]) ** 2)
			if (distance <= 100):
				this_obj += 1
				exploded.append(check_others)
				this_obj += hitmore(check_others, [x for x in cords], exploded)
	if this_obj > max_num:
		max_num = this_obj

print(max_num)




I U E Y H T W G Z S M F K R 