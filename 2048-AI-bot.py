import sys

range = range(4)

def rotateright(grid) :
  return [[grid[r][3-c] for r in range] for c in range4]

def moverow(grid):
  out = [x for x in row if x]
  ic = 0
  oc = 0
  while(out[ic:]) :
    if out[ic+1:] and out[ic+1] == out[ic] :
      out[oc] = 2*out[ic]
      ic += 1
   else :
      out[oc] = out[ic]
	ic += 1
	oc += 1
	out[oc:] = [None]*(4-oc)
return out

def move(grid,rot)
	for i in range(rot) :
		grid = rotateright(grid)
	out = map(moverow,grid)
return out, out != grid

def heuristicscore(actualscore, noemptycells, clusteringscore):
	score = int(actualscore + log10(actualscore)*noemptycells - clusteringscore)
return score

def calc_clusteringscore(grid):
	clusteringscore = 0
	neighbors = [-1,0,1]
	for i in range :
		for j in range :
			if grid[i][j] is None :
				continue
			numofneighbors = 0
			score = 0
			for k in neighbors :
          x = i+k
				if x < 0 and x > len(grid) :
          continue
        for l in neighbors :
          y = j+l
          if y < 0 and y > len(grid) :
            continue
          if grid[x][y] > 0 :
            numofneighbors++
          score += abs(grid[x][y]-grid[i][j])

      clusteringscore += score/numofneighbors
return clusteringscore

def alphabetapruning(board, depth, alpha, beta, player) :
      if board.isWin :
        bestscore = sys.maxint

      elif board.isLost :
        bestscore = min(board.getScore(), 1)

      elif depth == 0 :
        bestscore = heuristic(board.score(), board.get_empty_cells(), calc_clusteringscore(grid))
        
      else :
        if player == 'USER' :
          
          for d in direction :
            newboard = board.getGrid()
            points = newboard.move(d)
            
            if points == 0 and newboard == board
              continue
             current_score, current_direction =  alphabetapruning(newboard, depth-1, alpha, beta, 'COMPUTER'))
            
            if current_score <= alpha :

            if beta <= alpha :
              break
            
        else :
          moves = board.get_empty_cells()
          possible_values = { 2 , 4 }
          
          for cell_ID in moves :
            i = cell_ID/range4
            j = cell_ID%range4
            
            for values in possible_values :
              newboard = board.getGrid()
              newboard.set_empty_cells(i,j,value)
              current_score, current_direction = alphabetapruning(child, depth-1, alpha, beta, 'USER')
              
              if current_score < beta :
                beta = current_score
              
              if beta <= alpha :
                break

          bestscore = beta

          if moves is None :
            bestscore = 0

  return bestscore, current_direction


            

