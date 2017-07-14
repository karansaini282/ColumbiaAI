from random import randint
from BaseAI_3 import BaseAI
 
class PlayerAI(BaseAI):
    def getMove(self, grid):
        initial= gridTree(grid,0,None,"max",-1)
        queue=[initial]
        total=[initial]
        while len(queue): 
            current=queue.pop()
            if(current.level>7):
                break
            if current.player=="max":
                moves = current.grid.getAvailableMoves()
                for i in moves:
                    gridCopy=current.grid.clone()
                    gridCopy.move(i)
                    newLevel=current.level+1
                    newParent=current
                    newPlayer="min"
                    newNode=gridTree(gridCopy,newLevel,newParent,newPlayer,i)
                    queue.append(newNode)
                    total.append(newNode)
                    current.addChild(newNode)
            if current.player=="min":                
                cells=grid.getAvailableCells()
                if(len(cells)>3):
                    cells=cells[0:4]
                for cell in cells:
                    gridCopy=current.grid.clone()
                    gridCopy.setCellValue(cell,getRandom())
                    newLevel=current.level+1
                    newParent=current
                    newPlayer="max"
                    newNode=gridTree(gridCopy,newLevel,newParent,newPlayer,cell)
                    queue.append(newNode)
                    total.append(newNode)
                    current.addChild(newNode)
        AlphaBeta(total[0])
        return total[0].bestMove

def score(grid):
    sum_heuristic=powerFunc(grid)
    return sum_heuristic

def powerFunc(grid):
    sum_adjacent=0
    sum_row=0
    sum_col=0
    sum_open=0
    sum_edge=0
    for i in range(grid.size):
        flag_min_row=True
        min_row=0
        flag_min_col=True
        min_col=0
        for j in range(grid.size):
            if (i==0 and j==0):
                sum_edge+=grid.map[i][j]
            if(grid.map[i][j]==0):
                sum_open+=1
            if(j!=grid.size-1):
                if(grid.map[i][j]==grid.map[i][j+1]):
                    sum_adjacent+=grid.map[i][j]
            if(i!=grid.size-1):
                if(grid.map[i][j]==grid.map[i+1][j]):
                    sum_adjacent+=grid.map[i][j]
            if grid.map[i][grid.size-1-j]>min_row:
                flag_min_row=False
            min_row=grid.map[i][grid.size-1-j]
            if grid.map[grid.size-1-j][i]>min_col:
                flag_min_col=False
            min_col=grid.map[grid.size-1-j][i]
        if flag_min_row:
            sum_row+=1
        if flag_min_col:
            sum_col+=1
    if sum_open==0:
        return 0
    sum_power=sum_adjacent*4+(sum_row+sum_col)*500+sum_open*1000+sum_edge*20
    return sum_power

def checkAdjacent(grid):
    sum_adjacent=0    
    for i in range(grid.size):
        for j in range(grid.size):
            if(j!=grid.size-1):
                if(grid.map[i][j]==grid.map[i][j+1]):
                    sum_adjacent+=grid.map[i][j]
            if(i!=grid.size-1):
                if(grid.map[i][j]==grid.map[i+1][j]):
                    sum_adjacent+=grid.map[i][j]
    return sum_adjacent
                

def checkHorizontal(grid):
    sum_row=0
    for i in range(grid.size):
        flag_min=True
        flag_max=True
        min_row=0
        max_row=0
        for j in range(grid.size):            
            if grid.map[i][j]>min_row:
                flag_min=False
            if grid.map[i][j]<max_row:
                flag_max=False
            min_row=grid.map[i][j]
            max_row=grid.map[i][j]
        if flag_min:
            sum_row+=1
        if flag_max:
            sum_row+=1
    return sum_row

def checkVertical(grid):
    sum_col=0
    for i in range(grid.size):
        flag_min=True
        flag_max=True
        min_col=0
        max_col=0
        for j in range(grid.size):            
            if grid.map[j][i]>min_col:
                flag_min=False
            if grid.map[j][i]<max_col:
                flag_max=False
            min_col=grid.map[j][i]
            max_col=grid.map[j][i]
        if flag_min:
            sum_col+=1
        if flag_max:
            sum_col+=1
    return sum_col

def openSquares(grid):
    sum_open=0
    for i in range(grid.size):
        for j in range(grid.size):
            if(grid.map[i][j]==0):
                sum_open+=1
    return sum_open

def edgeValues(grid):
    sum_edge=0
    for i in range(grid.size):
        for j in range(grid.size):
            if i==0 or j==0:
                sum_edge+=grid.map[i][j]*grid.map[i][j]
    return sum_edge

def AlphaBeta(node):
    if len(node.children)==0:
        return score(node.grid)
    if node.player=="max":
        for child in node.children:
            node.old_alpha=node.alpha
            node.alpha = max(node.alpha,AlphaBeta(child))
            if node.alpha>node.old_alpha:
                node.bestMove=child.move
            if node.beta <= node.alpha:
                break
        return node.alpha
    if node.player=="min":    
        for child in node.children:
            node.old_beta=node.beta
            node.beta = min(node.beta,AlphaBeta(child))
            if node.beta<node.old_beta:
                node.bestMove=child.move
            if node.beta <= node.alpha:
                break
        return node.beta

class gridTree:
    def __init__(self,grid,level,parent,player,move):
        self.grid=grid
        self.move=move
        self.children=[]
        self.player=player
        self.level=level
        self.parent=parent
        self.alpha=-100000
        self.beta=100000
        self.bestMove=-1
    def addChild(self,child):
        self.children.append(child)
    def hasChild(self):
        return len(self.children)

def getRandom():
    if randint(0,99) < 90:
        return 2
    else:
        return 4

def heuristicScore(grid):
    score = grid.getMaxTile()*openSquares(grid)-clusteringScore(grid)
    return score
    
def clusteringScore(grid):
    clusteringScore=0;
    neighbors = [-1,0,1]
    for i in range(grid.size):
        for j in range(grid.size):
                if grid.map[i][j]==0:
                    continue
                numOfNeighbors=0
                sum1=0
                for k in neighbors:
                    x=i+k
                    if x<0 or x>=grid.size:
                        continue                    
                    for l in neighbors:
                        y = j+l
                        if y<0 or y>=grid.size:
                            continue
                        if grid.map[x][y]>0: 
                            numOfNeighbors+=1
                            sum1+=abs(grid.map[x][y]-grid.map[i][j])
                clusteringScore+=sum1/numOfNeighbors
    return clusteringScore
