from itertools import accumulate # Note this was added in Python 3.3

def transpose(matrix):
	result = [[0 for y in range(len(matrix[0]))] for x in range(len(matrix))]

	# iterate through rows
	for i in range(len(matrix)):
	   # iterate through columns
	   for j in range(len(matrix[0])):
	       result[j][i] = matrix[i][j]
	return result
    
def min_path_sum(matrix):
    """Returns the minimum path sum of a matrix moving only down and right"""
    size = len(matrix)
    if size == 0:
        return 0
    for i in range(len(matrix)):
    	matrix[i] = matrix[i][::-1]
    matrix = transpose(matrix)
    print(matrix)
    matrix[0] = list(accumulate(matrix[0][i] for i in range(size)))

    for i in range(1, size):
        matrix[0][i-1] += matrix[i][1]

    for i in range(1, size):
        for j in range(1, size):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
    return matrix[size-1][size-1]

if __name__ == '__main__':
    with open("snowfield") as file:
        matrix = []
        for line in file:
            matrix.append(list(map(int, line.strip().split())))
        print(min_path_sum(matrix))