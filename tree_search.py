import sys

# 0 1 2
# 3 4 5 
# 6 7 8

class State:
  board = [0 for i in range(9)]
  space = 0

def canMoveLeft(state):  
  if state.space in [0, 3, 6]:
    return False
  return True

def canMoveRight(state):
  if state.space in [2, 5, 8]:
    return False
  return True

def canMoveUp(state):
  if state.space in [0, 1, 2]:
    return False
  return True

def canMoveDown(state):
  if state.space in [6, 7, 8]:
    return False
  return True

def moveLeft(state):
  new_state = State()
  new_state.board = [i for i in state.board]
  new_state.space = state.space - 1
  new_state.board[state.space], new_state.board[new_state.space] =  state.board[new_state.space], state.board[state.space]  
  return new_state

def moveRight(state):
  new_state = State()
  new_state.board = [i for i in state.board]
  new_state.space = state.space + 1
  new_state.board[state.space], new_state.board[new_state.space] =  state.board[new_state.space], state.board[state.space]  
  return new_state

def moveUp(state):
  new_state = State()
  new_state.board = [i for i in state.board]
  new_state.space = state.space - 3
  new_state.board[state.space], new_state.board[new_state.space] =  state.board[new_state.space], state.board[state.space]  
  return new_state

def moveDown(state):
  new_state = State()
  new_state.board = [i for i in state.board]
  new_state.space = state.space + 3
  new_state.board[state.space], new_state.board[new_state.space] =  state.board[new_state.space], state.board[state.space]  
  return new_state

def solved(state):
  for i in range(9):
    if state.board[i] != (i+1)%9:
      return False
  return True



fringe = []

def DFS():
  if len(fringe): return fringe.pop()
  return None

def BFS():
  if len(fringe): return fringe.pop(0)
  return None

def branch_search(state, strategy, moves, d, b, n):

  #print(state.board)

  if solved(state):
    print("State solved at depth %i, branch %i, after %i problems searched" % (d, b, n))
    print(len(moves))    
    print([i.__name__ for i in moves])
    return

  if d > 2: return

  actions = []

  if canMoveLeft(state): actions.append(moveLeft)
  if canMoveRight(state): actions.append(moveRight)
  if canMoveUp(state): actions.append(moveUp)
  if canMoveDown(state): actions.append(moveDown)

  # For all available actions, add a new state to the fringe
  for a in actions:
    fringe.append((a, a(state), d+1))
  #print([i.__name__ for i in actions])

  # Search strategy 
  x = strategy()  
  b_search = 0
  while x != None:
    branch_action, branch_state, new_d = x
    #print(branch_action.__name__)
    new_moves = [i for i in moves]  
    new_moves.append(branch_action)
    n += 1
    branch_search(branch_state, strategy, new_moves, new_d, b_search, n)
  
    b_search += 1
    x = strategy()  



def createState(text):
  state = State()
  for i in range(9):
    if text[i] == "_": state.space = i
    else: state.board[i] = int(text[i])

  return state



programName = sys.argv[0]
board = sys.argv[1]

start_state = createState(board)
branch_search(start_state, BFS, [], 0, 0, 0)
