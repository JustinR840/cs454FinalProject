import enum


class direction(enum.IntEnum):
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3


class NFA:
	def __init__(self, transition_table, states, m_input, state_map, input_map):
		self.transition_table = transition_table
		self.states = states
		self.state_map = state_map
		self.m_input = m_input
		self.input_map = input_map


class State:
	def __init__(self, tip1, tip2, top_vert, bot_vert):
		self.tip1 = tip1
		self.tip2 = tip2
		self.top_vert = top_vert
		self.bot_vert = bot_vert

	def __str__(self):
		return self.tip1.__str__() + " " + self.tip2.__str__() + " " + self.top_vert.__str__() + " " + self.bot_vert.__str__()


class TestObj:
	def __init__(self):
		self.state = \
			[
				# 0  1  2
				[0, 0, 0],  # 0
				[0, 0, 0],  # 1
				[0, 0, 0],  # 2
				[0, 0, 0],  # 3
				[0, 0, 0]  # 4
			]
		self.tip1 = [0, 0]
		self.tip2 = [0, 0]
		self.tip1_starting = [0, 0]
		self.tip2_starting = [0, 0]
		self.input_pair = [0, 0]

	def LeftTopVertUsed(self):
		return self.state[1][0] == 1

	def LeftBotVertUsed(self):
		return self.state[3][0] == 1

	def RightTopVertUsed(self):
		return self.state[1][2] == 1

	def RightBotVertUsed(self):
		return self.state[3][2] == 1

	def pickSuitableNumbers(self):

		def numAdjacentEdges(state, starting):
			num = 0

			if (state[starting[0] - 1][starting[1]] == 1):  # up
				num += 1
			if (state[starting[0] + 1][starting[1]] == 1):  # down
				num += 1
			if (state[starting[0]][starting[1] - 1] == 1):  # left
				num += 1
			if (state[starting[0]][starting[1] + 1] == 1):  # right
				num += 1

			return num

		self.input_pair[0] = numAdjacentEdges(self.state, [1, 1])
		self.input_pair[1] = numAdjacentEdges(self.state, [3, 1])

	def getMoveableTipDirections(self, tip):
		directions = []
		if (tip[1] < len(self.state[0]) - 1 and self.state[tip[0]][tip[1] + 2] == 0):
			directions.append(direction.RIGHT)
		if (tip[1] > 0 and self.state[tip[0]][tip[1] - 2] == 0):
			directions.append(direction.LEFT)
		if (tip[0] < len(self.state) - 1 and self.state[tip[0] + 2][tip[1]] == 0):
			directions.append(direction.DOWN)
		if (tip[0] > 0 and self.state[tip[0] - 2][tip[1]] == 0):
			directions.append(direction.UP)

		return directions

	def setTip1(self, x, y):
		self.state[y][x] = 1
		self.tip1[0] = y
		self.tip1[1] = x
		self.tip1_starting[0] = y
		self.tip1_starting[1] = x

	def setTip2(self, x, y):
		self.state[y][x] = 1
		self.tip2[0] = y
		self.tip2[1] = x
		self.tip2_starting[0] = y
		self.tip2_starting[1] = x

	def moveTip1(self, dir):
		if (dir == direction.UP):
			if (self.tip1[0] > 0):
				if (self.state[self.tip1[0] - 2][self.tip1[1]] == 0):
					self.state[self.tip1[0] - 1][self.tip1[1]] = 1
					self.state[self.tip1[0] - 2][self.tip1[1]] = 1
					self.tip1[0] -= 2
					# print("moved up")
					return True
				else:
					# print("can't move up: direction already taken")
					return False
			else:
				# print("can't move up: already at top")
				return False
		elif (dir == direction.RIGHT):
			if (self.tip1[1] < len(self.state[0]) - 1):
				if (self.state[self.tip1[0]][self.tip1[1] + 2] == 0):
					self.state[self.tip1[0]][self.tip1[1] + 1] = 1
					self.state[self.tip1[0]][self.tip1[1] + 2] = 1
					self.tip1[1] += 2
					# print("moved right")
					return True
				else:
					# print("can't move right: direction already taken")
					return False
			else:
				# print("can't move right: already at rightmost edge")
				return False
		elif (dir == direction.DOWN):
			if (self.tip1[0] < len(self.state) - 1):
				if (self.state[self.tip1[0] + 2][self.tip1[1]] == 0):
					self.state[self.tip1[0] + 1][self.tip1[1]] = 1
					self.state[self.tip1[0] + 2][self.tip1[1]] = 1
					self.tip1[0] += 2
					# print("moved down")
					return True
				else:
					# print("can't move down: direction already taken")
					return False
			else:
				# print("can't move down: already at bottom")
				return False
		elif (dir == direction.LEFT):
			if (self.tip1[1] > 0):
				if (self.state[self.tip1[0]][self.tip1[1] - 2] == 0):
					self.state[self.tip1[0]][self.tip1[1] - 1] = 1
					self.state[self.tip1[0]][self.tip1[1] - 2] = 1
					self.tip1[1] -= 2
					# print("moved left")
					return True
				else:
					# print("can't move left: direction already taken")
					return False
			else:
				# print("can't move left: already at leftmost edge")
				return False
		else:
			Exception("Unknown direction")

	def moveTip2(self, dir):
		if (dir == direction.UP):
			if (self.tip2[0] > 0):
				if (self.state[self.tip2[0] - 2][self.tip2[1]] == 0):
					self.state[self.tip2[0] - 1][self.tip2[1]] = 1
					self.state[self.tip2[0] - 2][self.tip2[1]] = 1
					self.tip2[0] -= 2
					# print("moved up")
					return True
				else:
					# print("can't move up: direction already taken")
					return False
			else:
				# print("can't move up: already at top")
				return False
		elif (dir == direction.RIGHT):
			if (self.tip2[1] < len(self.state[0]) - 1):
				if (self.state[self.tip2[0]][self.tip2[1] + 2] == 0):
					self.state[self.tip2[0]][self.tip2[1] + 1] = 1
					self.state[self.tip2[0]][self.tip2[1] + 2] = 1
					self.tip2[1] += 2
					# print("moved right")
					return True
				else:
					# print("can't move right: direction already taken")
					return False
			else:
				# print("can't move right: already at rightmost edge")
				return False
		elif (dir == direction.DOWN):
			if (self.tip2[0] < len(self.state) - 1):
				if (self.state[self.tip2[0] + 2][self.tip2[1]] == 0):
					self.state[self.tip2[0] + 1][self.tip2[1]] = 1
					self.state[self.tip2[0] + 2][self.tip2[1]] = 1
					self.tip2[0] += 2
					# print("moved down")
					return True
				else:
					# print("can't move down: direction already taken")
					return False
			else:
				# print("can't move down: already at bottom")
				return False
		elif (dir == direction.LEFT):
			if (self.tip2[1] > 0):
				if (self.state[self.tip2[0]][self.tip2[1] - 2] == 0):
					self.state[self.tip2[0]][self.tip2[1] - 1] = 1
					self.state[self.tip2[0]][self.tip2[1] - 2] = 1
					self.tip2[1] -= 2
					# print("moved left")
					return True
				else:
					# print("can't move left: direction already taken")
					return False
			else:
				# print("can't move left: already at leftmost edge")
				return False
		else:
			Exception("Unknown direction")
