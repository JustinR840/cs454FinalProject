from Objs import *
import random
import copy


def main():
	allobjs = []
	newobjs = []
	processedojs = []

	makeTestStates(allobjs)

	stillIterating = True
	while (stillIterating):
		for obj in allobjs:
			tip1_moveable_dirs = obj.getMoveableTipDirections(obj.tip1)

			for dir in tip1_moveable_dirs:
				newobj = copy.deepcopy(obj)
				newobj.moveTip1(dir)
				newobjs.append(newobj)
			# tip2_moveable_dirs = obj.getMoveableTipDirections(obj.tip2)
			# for dir in tip2_moveable_dirs:
			# 	newobj = copy.deepcopy(obj)
			# 	newobj.moveTip2(dir)
			# 	newobjs.append(newobj)

			obj.pickSuitableNumbers()
			# Put processed objects in a different list so we won't process them in the next iteration
			processedojs.append(obj)

		# Set the next iteration to process the NEW objects
		allobjs = newobjs

		if (len(allobjs) == 0):
			stillIterating = False
		else:
			# Clear the new objects list for the next iteration
			newobjs = []

	# processedobjs contains all final objects, set it to allobjs
	allobjs = processedojs


	# Create states
	states = []
	states_map = {}

	count = 0
	for obj in allobjs:
		in_state = State(obj.tip1_starting, obj.tip2_starting, obj.LeftTopVertUsed(), obj.LeftBotVertUsed())
		out_state = State(obj.tip1, obj.tip2, obj.LeftTopVertUsed(), obj.LeftBotVertUsed())

		if(not areStatesSame(in_state, out_state)):
			if(not doesStateExists(in_state, states)):
				states.append(in_state)
				states_map[in_state.__str__()] = count
				count += 1
			else:
				pass
				#print("state already exists")
			if(not doesStateExists(out_state, states)):
				states.append(out_state)
				states_map[out_state.__str__()] = count
				count += 1
			else:
				pass
				#print("state already exists")
		else:
			#print("states are same")
			if(not doesStateExists(in_state, states)):
				states.append(in_state)
				states_map[in_state.__str__()] = count
				count += 1
			else:
				pass
				#print("state already exists")


	alphabet = [-1, 0, 1, 2, 3]
	input_pairs = []
	input_pairs_map = {}

	count = 0
	for i in alphabet:
		for j in alphabet:
			input_pairs.append([i, j])
			input_pairs_map[[i, j].__str__()] = count
			count += 1

	transition_table = [[[] for x in range(len(input_pairs))] for y in range(len(states))]

	nfa = NFA(transition_table, states, input_pairs, states_map, input_pairs_map)

	for obj in allobjs:
		in_state = State(obj.tip1_starting, obj.tip2_starting, obj.LeftTopVertUsed(), obj.LeftBotVertUsed())
		out_state = State(obj.tip1, obj.tip2, obj.LeftTopVertUsed(), obj.LeftBotVertUsed())

		for i in range(len(nfa.states)):
			pass








	print()

def areStatesSame(state1, state2):
	# for i in range(len(state1.state)):
	# 	for j in range(len(state1.states[i])):
	# 		if(state1.state[i][j] != state2.state[i][j]):
	# 			return False

	# tip1 endings in different spots
	if(state1.tip1[0] != state2.tip1[0] or state1.tip1[1] != state2.tip1[1]):
		return False

	# tip2 endings in different spots
	if (state1.tip2[0] != state2.tip2[0] or state1.tip2[1] != state2.tip2[1]):
		return False

	# Reversed tips
	# if((state1.tip1[0] != state2.tip2[0] or state1.tip1[1] != state2.tip2[1]) and
	# 	   (state1.tip2[0] != state2.tip1[0] or state1.tip2[1] != state2.tip1[1])):
	# 	return False

	# top/bot verticals not the same
	if(state1.top_vert != state2.top_vert or state2.bot_vert != state2.bot_vert):
		return False

	# if(state1.tip1_starting[0] != state2.tip1_starting[0] or state1.tip1_starting[1] != state2.tip1_starting[1]):
	# 	return False
	#
	# if(state1.tip2_starting[0] != state2.tip2_starting[0] or state2.tip1_starting[1] != state2.tip2_starting[1]):
	# 	return False

	return True

def doesStateExists(state, state_list):
	for i in state_list:
		if(areStatesSame(state, i)):
			return True

	return False

def makeTestStates(allobjs):
	objtm = TestObj()
	objtm.setTip1(0, 0)
	objtm.setTip2(0, 2)
	allobjs.append(objtm)

	objtb = TestObj()
	objtb.setTip1(0, 0)
	objtb.setTip2(0, 4)
	allobjs.append(objtb)

	objtn = TestObj()
	objtn.setTip1(0, 0)
	# objtn.setTip2(0, 2)
	allobjs.append(objtn)

	# objmt = TestObj()
	# objmt.setTip1(0, 2)
	# objmt.setTip2(0, 0)
	# allobjs.append(objmt)

	objmb = TestObj()
	objmb.setTip1(0, 2)
	objmb.setTip2(0, 4)
	allobjs.append(objmb)

	objmn = TestObj()
	objmn.setTip1(0, 2)
	# objtn.setTip2(0, 2)
	allobjs.append(objmn)

	# objbt = TestObj()
	# objbt.setTip1(0, 4)
	# objbt.setTip2(0, 0)
	# allobjs.append(objbt)

	# objbm = TestObj()
	# objbm.setTip1(0, 4)
	# objbm.setTip2(0, 2)
	# allobjs.append(objbm)

	objbn = TestObj()
	objbn.setTip1(0, 4)
	# objtn.setTip2(0, 2)
	allobjs.append(objbn)

	# objnt = TestObj()
	# # objnt.setTip1(0, 2)
	# objnt.setTip2(0, 0)
	# allobjs.append(objnt)

	# objnm = TestObj()
	# # objnm.setTip1(0, 2)
	# objnm.setTip2(0, 2)
	# allobjs.append(objnm)

	# objnb = TestObj()
	# # objnb.setTip1(0, 2)
	# objtn.setTip2(0, 4)
	# allobjs.append(objnb)

	objnn = TestObj()
	# objnn.setTip1(0, 2)
	# objtn.setTip2(0, 2)
	allobjs.append(objnn)

	# testobj = TestObj()
	# testobj.setTip1(0, 4)
	# testobj.setTip2(0, 2)
	#
	# allobjs.append(testobj)

main()
