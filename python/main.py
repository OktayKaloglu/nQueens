import random as rnd
# Gradient Descent approach is chosen to solve The Eight Queens problem

def viewMatrix(table):
    rowFiller=" -- "
    columnFiller="|"
    twoD=table
    tableLen=len(table)
    for i in range(tableLen-1):
        for j in range(tableLen-1):
            print(twoD[i][j],end=rowFiller)
        print(twoD[i][tableLen-1])
        for j in range(tableLen-1):
            print(columnFiller+"    ",end="")
        print(columnFiller)
    for j in range(tableLen-1):
        print(twoD[tableLen-1][j],end=rowFiller)
    print(twoD[tableLen-1][tableLen-1])

#The chess table has 8 rows, 8 columns and total of 64 squares
#I am using the rows as an array and store the columns as the data

#make a new two dimensional array from one dimensional array
def arrayConverter(table):
    convertedArray=[]
    for i in range(len(table)):
        emptyArray=["O"]*8
        emptyArray[table[i]]="X"
        convertedArray.append(emptyArray)

    return convertedArray

#a function for viewing the chess table. The queens is displayed as X and the rest are displayed as 0
def viewTable(table):
    rowFiller=" -- "
    columnFiller="|"
    twoD=arrayConverter(table)
    tableLen=len(table)
    for i in range(tableLen-1):
        for j in range(tableLen-1):
            print(twoD[j][i]+rowFiller,end="")
        print(twoD[tableLen-1][i])
        for j in range(tableLen-1):
            print(columnFiller+"    ",end="")
        print(columnFiller)
    for j in range(tableLen-1):
        print(twoD[j][tableLen-1]+rowFiller,end="")
    print(twoD[tableLen-1][tableLen-1])

# randomly assigning queens positions
#this method insures the queens wont be in the same row at the initial state
def rndStart(table):
    iniPos=[]

    tableLen=len(table)
    for i in range(tableLen):
        iniPos.append(i)
    for i in range(tableLen):
        randomIndex=rnd.randint(0,len(iniPos)-1)
        table[i]=iniPos[randomIndex]
        iniPos.remove(iniPos[randomIndex])


#calculate the collisions at the squares that caused by the queens
#return the collision matrix
#necessary calculations made by the help of breadth first approach
def calculateTheMatrix(table):
    numberOfQueens=len(table)
    collisionMatrix=[]
    for i in range(numberOfQueens):
        collisionMatrix.append([0]*numberOfQueens)
    for i in range(numberOfQueens):
        #i specifies the column
        # add a collision to the squares that the queen can reach

        collisionMatrix[table[i]][i]+=1 #for the starting point

        for j in range(1,numberOfQueens):#needs improvement for this loop count
            #for lateral collision from starting position
            if i+j<numberOfQueens:
                collisionMatrix[table[i]][i+j]+=1 #add collisions after the starting position's  at x axis
            if i-j>-1:
                collisionMatrix[table[i]][i-j]+=1 #add collisions before the starting position's  at x axis

            if table[i]-j>-1:
                collisionMatrix[table[i]-j][i]+=1 #add collisions above the starting position's  at y axis
                if i-j>-1:
                    collisionMatrix[table[i]-j][i-j]+=1 #add collisions to the starting position above and left at y axis and x axis

                if i+j<numberOfQueens:
                    collisionMatrix[table[i]-j][i+j]+=1 #add collisions to the starting position above and right at y axis and x axis
            if table[i]+j<numberOfQueens:
                collisionMatrix[table[i]+j][i]+=1 #add collisions below the starting position's at y axis
                if i-j>-1:
                    collisionMatrix[table[i]+j][i-j]+=1 #add collisions to the starting position above and left at y axis and x axis

                if i+j<numberOfQueens:
                    collisionMatrix[table[i]+j][i+j]+=1 #add collisions to the starting position above and right at y axis and x axis


    return collisionMatrix

def gradientDecent(table):
    nQueens=len(table)
    while(True):
        collisionMatrix=calculateTheMatrix(table)

        while(True):
            arandomQueen=rnd.randint(0,nQueens)
            queensCurrenCollision=collisionMatrix[arandomQueen][table[arandomQueen]]
            coloumnsCollisions=[]
            for i in range(0,nQueens):
                coloumnsCollisions.append([collisionMatrix[i][table[arandomQueen]],i])#number of collision,column index
            while(len(coloumnsCollisions)>0):
                randNum=rnd.randint(0,len(coloumnsCollisions))
                if(coloumnsCollisions[randNum][0]<queensCurrenCollision):
                    table[arandomQueen]=randNum
                    break

        viewMatrix(collisionMatrix)


def main():
    numberOfqueens=4
    table= [0]*numberOfqueens
    rndStart(table)
    table=[3,0,2,1]
    gradientDecent(table)
    viewTable(table)


if __name__ == '__main__':
    main()
