import csv
import sys

def gridPrint(arr):
    ans=""
    for i in range(9):
        for j in range(9):
            ans+=str(arr[i][j])
    text_file = open("output.txt", "w")
    text_file.write(ans)
    text_file.close()
 

def getNone(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
 
def rowCheck(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
 
def colCheck(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
 
def boxCheck(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False
 
def valCheck(arr,row,col,num):
    return not rowCheck(arr,row,num) and not colCheck(arr,col,num) and not boxCheck(arr,row - row%3,col - col%3,num)
 
def gridSolve(arr):
    l=[0,0]     
    if(not getNone(arr,l)):
        return True     
    row=l[0]
    col=l[1]     
    for num in range(1,10):         
        if(valCheck(arr,row,col,num)):             
            arr[row][col]=num 
            if(gridSolve(arr)):
                return True
            arr[row][col] = 0             
    return False
 
if __name__=="__main__":
    gridStr=sys.argv[1]
    grid=[]
    for i in range(9):
        subGrid=[int(k) for k in list(gridStr[i*9:i*9+9])]
        grid.insert(len(grid),list(subGrid))
    if(gridSolve(grid)):
        gridPrint(grid)        
    else:
        print("Solution not found")
