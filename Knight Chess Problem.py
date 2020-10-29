# queue node used in BFS
class Node:
	# (x, y) represents chess board coordinates
	# dist represent its minimum distance from the source
	def __init__(self, x, y, dist=0):

		self.x = x
		self.y = y
		self.dist = dist

	# As we are using Node as a key in a dictionary,
	# we need to implement hashCode() and equals()
	def __hash__(self):

		return hash((self.x, self.y, self.dist))

	def __eq__(self, other):

		return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)

# Below lists details all 8 possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


# Check if (x, y) is valid chess board coordinates
# Note that a knight cannot go out of the chessboard
def valid(x, y, N):
	return not (x < 0 or y < 0 or x >= N or y >= N)


# Find minimum number of steps taken by the knight
# from source to reach destination using BFS
def DFS(src, dest, N):

	# set to check if matrix cell is visited before or not
	visited = set()

	# create a queue and enqueue first node
	s = []
	s.append(src)

	# loop till queue is empty
	while s:

		# pop front node from queue and process it
		node = s.pop()

		x = node.x
		y = node.y
		dist = node.dist

		# if destination is reached, return distance
		if x == dest.x and y == dest.y:
			return dist

		# Skip if location is visited before
		if node not in visited:
			# mark current node as visited
			visited.add(node)

			# check for all 8 possible movements for a knight
			# and enqueue each valid movement into the queue
			for i in range(8):
				# Get the valid position of Knight from current position on
				# chessboard and enqueue it with +1 distance
				x1 = x + row[i]
				y1 = y + col[i]

				if valid(x1, y1, N):
					s.append(Node(x1, y1, dist + 1))

	# return INFINITY if path is not possible
	return float('inf')
 
 
if __name__ == '__main__':

	N = 8

	src = Node(0, 7)   # source coordinates
	dest = Node(7, 0)  # destination coordinates

	print("Minimum number of steps required is", DFS(src, dest, N))