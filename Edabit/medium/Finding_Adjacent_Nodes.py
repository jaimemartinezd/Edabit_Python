'''
Your task is to determine if two nodes are adjacent in an undirected graph when given the adjacency matrix and the two nodes.
'''

matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]

def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2] == 1

print(is_adjacent(matrix, 0, 1))
print(is_adjacent(matrix, 0, 2))
print(is_adjacent(matrix, 2, 1))