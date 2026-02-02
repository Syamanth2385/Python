matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matrix) #printed output:- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#if you want to access an index from this matrix you can use
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])
#this will print the output linewise
#to make this same output print in same line we can use
print(matrix[0][0], matrix[1],[1],matrix[2],[2])
#if you want to access every item from the matrix you can use for loop to iterate
for row in matrix:
  for col in row:
    print(col)
