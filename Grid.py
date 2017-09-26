import numpy as np


class Grid:
	
	# grid of i:height and j:width
	# i = 0 is the top and j = 0 is the left


	def __init__(self, height, width, startingTuple = (0,0), impassableTupleList = [], terminalTupleList = [], rewardMatrix = None):
		self.i,self.j = startingTuple
		self.height = height
		self.width = width
		self.states = np.ones([height,width], dtype = np.int8)

		for tuple in impassableTupleList:
			self.states[tuple] = 0;

		for tuple in terminalTupleList:
			self.states[tuple] = -1;

		self.rewardMatrix = np.zeros(height,width) if rewardMatrix is None else rewardMatrix


	def drawTerrain(self):
		print (self.states)

	def isInTerminalState(self):
		return self.states[(self.i,self.j)] == -1


	


if __name__ == '__main__':

	impassableTupleList = [(1,1)]
	terminalTupleList = [(0,3),(1,3)]

	grid = Grid(3,4,(2,0),impassableTupleList, terminalTupleList)
	grid.drawTerrain()

	print(grid.isInTerminalState())
	grid.i,grid.j = (1,3)
	print(grid.isInTerminalState())
	



