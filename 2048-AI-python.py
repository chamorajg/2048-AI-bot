import random
import sys

N = 4

CODE = {'left': 37,
            'up': 38,
            'right': 39,
            'down': 40}
LEFT = 'left'
UP = 'up'
RIGHT = 'right'
DOWN = 'down'

class Board(object):
  def __init__(self):
    self.board = [[None] * N for i in range(N)]
    self.score = 0
    self.over = False

  def rotateleft(self,grid):
  	ret = self.emptyGrid()
  	for i in range(N):
  	  for j in range(N):
  	  	out[i][j] = grid[3-j][i]
    return ret

  def rotateright(self,grid):
  	ret = self.emptyGrid()
  	for i in range(N):
  	  for j in range(N):
  	  	out[i][j] = grid[j][3-i]
    return ret

  def emptyGrid(self):
  	ret = list()
  	for i in range(N):
  		col = list()
  		for j in range(N):
  			col.append(None)
  		ret.append(col)
  	return ret

  def to_move(self,grid,direction):
  	out = self.emptyGrid()

  	if direction == UP :
  	 	rot = 1
  	elif direction == RIGHT :
  		rot = 2
  	elif direction == DOWN :
  		rot = 3
  	else 
  		rot = 0 

  	for i in range(rot):
  		self.rotateleft(grid)

  	score = 0
  	for row in range(N):
  		oc = 0
  		ic = 0
  		while ic < 4 :
  			if grid[ic][r] is None :
  				ic += 1
  				continue
  			out[oc][r] = grid[ic][r]
  			oc += 1
  			ic += 1 

  		oc = 0
  		ic = 0

  		while ic < 4 :
  			if our[ic][r] is None :
  				break

  			if ic == 3 :
  			 out[oc][r] = out[ic][r]
  			 oc += 1
  			 break

  			if our[oc][r] == out[ic][r] :
  			  out[oc][r] = 2*out[ic][r]
  			  score  += out[oc][r]
  			  ic += 1
  			
  			else :
  				out[oc][r] = out[ic][r]
  			ic += 1
  			oc += 1

  			while oc < 4 :
  				out[oc][r] = None
  				oc += 1

  			for i in range(N):
  				out = self.rotateright()


  	return out, score

  def move(self,direction):
  	next_board, get_score = self.to_move(direction)
  	moved = (next_board != self.board)

  	self.board = next_board
  	self.score+ = get_score

  	if moved :
  		if not self.randomTile():
  			self.over = True

  def can_move(self,grid,direction):
  	return grid != self.to_move(grid,direction)[0]

  def get_empty_cells(self):
  	for i in range(N):
  		for j in range(N):
  			if self.board[i][j] is None :
  				yield i, j

  def randomTile(self):
  	cells = list(self.get_empty_cells())
  	if not cells:
  		return False

  	if random.random() < 0.9 :
  	   tile = 2
  	else :
  		tile = 4

  	cellid = random.choice(cells)
  	self.board[cellid[0]][cellid[1]] = tile

  def show(self):
    for i in range(N):
      for j in range(N):
        if self.board[j][i]:
          print '%4d' % self.board[j][i],
        else:
          print '   .',
      print

def load_ai_module():
  if len(sys.argv) > 3:
    name = sys.argv[3]
  else:
    name = 'kcwu'
  fullpath = 'ai_modules.' + name
  print 'load module', fullpath
  ai = __import__(fullpath)
  return getattr(ai, name)


class GameManager(object):
  def __init__(self):
    self.player = ''
    self.board = Board()
    self.board.randomTile()
    self.board.randomTile()
    self.board.show()
    self.ai = load_ai_module().AI()

  def setPlayer(self, name):
    self.player = name

  def getGameState(self):
    d = {}

    cells = []
    d['grid'] = {'cells': cells}
    for i in range(N):
      row = []
      for j in range(N):
        if self.board.board[i][j]:
          cell = { 'value': self.board.board[i][j] }
        else:
          cell = None

        row.append(cell)
      cells.append(row)

    d['won'] = False # i'm lazy
    d['over'] = self.board.over

    return d

  def getGrid(self):
    gs = self.getGameState()
    if gs is None:
      return None
    raw_grid = gs['grid']['cells']
    grid = list()
    for i in xrange(4):
      col = [x['value'] if x else None for x in raw_grid[i]]
      grid.append(col)
    return grid

  def getScore(self):
    return self.board.score

  def isLost(self):
    return self.board.over

  def isWin(self):
    return False

  def pressKey(self, kc):
    #print 'pressKey', kc
    if kc == CODE['left']:
      self.board.move(KEY_LEFT)
    elif kc == CODE['right']:
      self.board.move(KEY_RIGHT)
    elif kc == CODE['up']:
      self.board.move(KEY_UP)
    elif kc == CODE['down']:
      self.board.move(KEY_DOWN)
    else:
        raise ValueError
    #self.board.show()

  def keepGoing(self):
    pass

  def isOver(self):
    return self.board.over














