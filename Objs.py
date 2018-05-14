import enum

class direction(enum.IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class TestObj:
    def __init__(self):
        self.state =\
            [
                #0  1  2
                [0, 0, 0], # 0
                [0, 0, 0], # 1
                [0, 0, 0], # 2
                [0, 0, 0], # 3
                [0, 0, 0]  # 4
            ]
        self.tip1 = [0, 0]
        self.tip2 = [0, 0]
        #self.top_vert_used = False
        #self.bot_vert_used = False
        self.input_pair = [0, 0]
        self.processed = 0

    def isTopVertUsed(self):
        return self.state[1][2] == 1

    def isBotVertUsed(self):
        return self.state[3][2] == 1

    def pickSuitableNumbers(self):

        def numAdjacentEdges(state, starting):
            num = 0

            if(state[starting[0] - 1][starting[1]] == 1): # up
                num += 1
            if(state[starting[0] + 1][starting[1]] == 1): # down
                num += 1
            if(state[starting[0]][starting[1] - 1] == 1): # left
                num += 1
            if(state[starting[0]][starting[1] + 1] == 1): # right
                num += 1

            return num


        self.input_pair[0] = numAdjacentEdges(self.state, [1, 1])
        self.input_pair[1] = numAdjacentEdges(self.state, [3, 1])



    def getMoveableTipDirections(self, tip):
        directions = []
        if(tip[1] < len(self.state[0]) - 1 and self.state[tip[0]][tip[1] + 2] == 0):
            directions.append(direction.RIGHT)
        if(tip[1] > 0 and self.state[tip[0]][tip[1] - 2] == 0):
            directions.append(direction.LEFT)
        if(tip[0] < len(self.state) - 1 and self.state[tip[0] + 2][tip[1]] == 0):
            directions.append(direction.DOWN)
        if(tip[0] > 0 and self.state[tip[0] - 2][tip[1]] == 0):
            directions.append(direction.UP)

        return directions

    def setTip1(self, x, y):
        self.state[y][x] = 1
        self.tip1[0] = y
        self.tip1[1] = x

    def setTip2(self, x, y):
        self.state[y][x] = 1
        self.tip2[0] = y
        self.tip2[1] = x

    def moveTip1(self, dir):
        if(dir == direction.UP):
            if(self.tip1[0] > 0):
                if(self.state[self.tip1[0] - 2][self.tip1[1]] == 0):
                    self.state[self.tip1[0] - 1][self.tip1[1]] = 1
                    self.state[self.tip1[0] - 2][self.tip1[1]] = 1
                    self.tip1[0] -= 2
                    #print("moved up")
                    return True
                else:
                    #print("can't move up: direction already taken")
                    return False
            else:
                #print("can't move up: already at top")
                return False
        elif(dir == direction.RIGHT):
            if(self.tip1[1] < len(self.state[0]) - 1):
                if(self.state[self.tip1[0]][self.tip1[1] + 2] == 0):
                    self.state[self.tip1[0]][self.tip1[1] + 1] = 1
                    self.state[self.tip1[0]][self.tip1[1] + 2] = 1
                    self.tip1[1] += 2
                    #print("moved right")
                    return True
                else:
                    #print("can't move right: direction already taken")
                    return False
            else:
                #print("can't move right: already at rightmost edge")
                return False
        elif(dir == direction.DOWN):
            if(self.tip1[0] < len(self.state) - 1):
                if(self.state[self.tip1[0] + 2][self.tip1[1]] == 0):
                    self.state[self.tip1[0] + 1][self.tip1[1]] = 1
                    self.state[self.tip1[0] + 2][self.tip1[1]] = 1
                    self.tip1[0] += 2
                    #print("moved down")
                    return True
                else:
                    #print("can't move down: direction already taken")
                    return False
            else:
                #print("can't move down: already at bottom")
                return False
        elif(dir == direction.LEFT):
            if(self.tip1[1] > 0):
                if(self.state[self.tip1[0]][self.tip1[1] - 2] == 0):
                    self.state[self.tip1[0]][self.tip1[1] - 1] = 1
                    self.state[self.tip1[0]][self.tip1[1] - 2] = 1
                    self.tip1[1] -= 2
                    #print("moved left")
                    return True
                else:
                    #print("can't move left: direction already taken")
                    return False
            else:
                #print("can't move left: already at leftmost edge")
                return False
        else:
            Exception("Unknown direction")