import numpy as np
import sys
import pdb
import random

class State:
	
	def key(state):
		state1D = state.ravel()
		acc = 0
		for i in range(9):
			acc += 3**i * state1D[i]
		return acc

	def value(key):
		#pdb.set_trace()
		state1D = np.zeros(9,)
		for i in range(8,-1,-1):
			state1D[i] = key // (3**i)
			key -= state1D[i] * (3**i)
			#print (state1D, key)
		return state1D.reshape(3,3)

class Environment:

	def getValidStates(self,currentState, player):
		validStates = []

		for i in range(9):
			flatArr = np.zeros([9,])
			flatArr[i] = player.id
			state = currentState + flatArr.reshape(3,3)
			if self.isValidAction(currentState,state, player):
				validStates.append(state)

		return validStates


	# returns the winner player, 0 otherwise from a given state
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

	# returns true if the game is over at a given state
	def isGameOver(self,state):
		# if there is a winner or there are no more free space on board
		if not self.getWinner(state) == 0 or np.count_nonzero(state == 0) ==0:
			return True
		else:
			return False

	# returns true if the next state is a valid transition from currentstate
	def isValidAction(self, currentState, nextState, player):
		#make sure an action on empty slot is taken by comparing number of zeros between consecutive states
		if not np.count_nonzero(currentState == 0) == np.count_nonzero(nextState == 0) +1:
 			return False

		# element wise subtraction should leave us with a matrix with one element either 1 or 2 with rest equals zero
		validation = nextState - currentState;
		return (np.count_nonzero(validation == 0) == 8 and validation.sum() == player.id)

	def playGame(self, player1, player2, draw = False):
		stateHistory = [np.zeros([3,3])]

		#player 1 starts first
		player = player1
		while not self.isGameOver(stateHistory[len(stateHistory)-1]):
			
			nextState = player.makeChoice(self, self.getValidStates(stateHistory[len(stateHistory)-1], player))
			stateHistory.append(nextState)

			#toggle player
			player = player2 if player == player1 else player1

		if draw:
			print("---------------")
			for state in stateHistory:
				print(state)
			print("---------------")

		#update the agents
		player1.updateStateValues(stateHistory[:], self) # make a copy of list
		player2.updateStateValues(stateHistory[:], self) # make a copy of list

		





class Agent:

	#key: state.key value: (value,N)
	knownStates = {}


	def __init__(self, id, epsilon = 0.1, learningRate = 0.1):
		self.id = id
		self.epsilon = epsilon
		self.learningRate = learningRate

	def shouldTakeRandomAction(self):
		return random.random() < self.epsilon

	def makeChoice(self, envrionment, validStates):
		
		if self.shouldTakeRandomAction():						
			randomIndex = random.randint(0,len(validStates)-1)
			return validStates[randomIndex]
		else:
			maxValue = -100 # should be less then minimum state
			maxState = None
			for state in validStates:
				tmpValue , tmpN = self.getStateValueTuple(state, envrionment)
				if  tmpValue > maxValue:
					maxValue = tmpValue
					maxState = state

			return maxState

	def getStateValueTuple(self, state, envrionment):
		key = State.key(state)
		stateTuple = self.knownStates.get(key)

		#if visiting state for the first time
		if stateTuple is None:
			if envrionment.isGameOver(state):			
				winner = envrionment.getWinner(state)
				if winner == self.id:
					# win
					self.knownStates[key] = (1,1)
				else:
					# lose or draw
					self.knownStates[key] = (0,1)
			else:
				#any non terminal state
				self.knownStates[key] = (0.5,1)

		# return value of state
		return self.knownStates[key]

	def updateStateValues(self, stateHistory, envrionment):


		vs = stateHistory.pop()

		# Iterate 
		while len(stateHistory) > 0:
			vsPrime = vs
			vs = stateHistory.pop()

			#pdb.set_trace()
			vsValue, vsN = self.getStateValueTuple(vs, envrionment)
			vsPrimeValue, vsPrimeN = self.getStateValueTuple(vsPrime, envrionment)

			#update value
			vsValue = vsValue + self.learningRate * (vsPrimeValue - vsValue)
			self.knownStates[State.key(vs)] = (vsValue,vsN+1)
			
			



# main method			
if __name__ == '__main__':
	env = Environment()

	player1 = Agent(1)
	player2 = Agent(2)
	

	for i in range(20000):
		print("Game {0}".format(i))
		env.playGame(player1,player2)


	env.playGame(player1,player2,True)
	env.playGame(player1,player2,True)
	env.playGame(player1,player2,True)
	
	
	

	
	