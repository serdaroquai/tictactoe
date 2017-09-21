import numpy as np
import sys


class Environment:

	states={}
	
	currentState = np.zeros([3,3])
	
	# returns the winner player, 0 otherwise
	def getWinner(self,state):

		# state is a 3x3 np.array
		for player in [1,2]:
			for axis in range(3):  # 0,1,2
				# check horizontal and vertical
				if np.all(state[axis] == player) or np.all(state[:,axis] == player):
					return player
				# check diagonals
				if np.all(state.diagonal() == player) or np.all(np.diag(np.fliplr(state)) == player):
					return player
		return 0

	# returns latest state if the move is legal
	def playMove(self, player, nextState):

		# element wise subtraction should leave us with a matrix with one element either 1 or 2 with rest equals zero
		validation = nextState - self.currentState;

		if np.count_nonzero(validation == 0) == 8 or validation.sum() == player:
			currentState = nextState
			return currentState
		else:
			sys.exit("Illegal move! player:{0} \ncurrentState:\n{1}\nnextState:\n{2}".format(player,self.currentState,nextState))

	def playGame(self,player1,player2):
		

		self.currentState = np.zeros([3,3])

		players = [player1,player2]
		turn = 0

		while getWinner(self.currentState) == 0:
			currentPlayer = players[turn%2] # player1 always starts first
			
			state = currentPlayer.takeAction(self)

			for player in players:
				player.updateStateHistory(state)

			turn+=1

		for player in players:
			player.learn();

class Agent:

	def takeAction(self, environment):
		#TODO
	def updateStateHistory(self,state):
		#TODO
	def learn(self):
		#TODO




# main method			
if __name__ == '__main__':

	#TODO

	