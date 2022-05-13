import random as rnd
from timeit import default_timer as timer
rnd.seed(5)
# Gradient Descent approach is chosen to solve The Eight Queens problem

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

# a function that calculates the current state's collisions
# between all of the queens so it will have at least combination of n to 2= n*(n-1)/2=O(n^2)

def calculateCollision(table):
    collisions=0
    nQueens=len(table)
    for i in range(0,nQueens):
        for j in range(i+1,nQueens):
            # the 2 queens can be in the same axis or diagonal line
            #m=(y2-y1)/(x2-x1)
            m=(table[j]-table[i])/(j-i)
            # j-i!=0 => j!=i so We need to handle zero division.
            # queens cant be in the same column  in random start or in any other transition state.
            # we ensured that i wont be equal to the j.
            if m in [0,1,-1]:
                collisions+=1

    return collisions

#for available queen pairs
def pairList(nQueens):
    Pairs=[]
    for i in range(nQueens-1):
        for j in range(i+1,nQueens):
            Pairs.append([i,j])
    return Pairs

# a function that gets 2 random queens and it checks whether new state is better than current one
    # and swaps the queens positions as new positions.
    # if the current table has zero collisions that is a solution
    # if no queen can swap
def gradientDecent(table,Pairs):
    nSwaps=0
    nRndStart=0
    nQueens=len(table)
    currentCollisions=calculateCollision(table)

    while currentCollisions != 0 :
        availablePairs=Pairs.copy()

        while True:
            nextState=table.copy()
            index=rnd.randint(0,len(availablePairs)-1)
            queen1=availablePairs[index][0]
            queen2=availablePairs[index][1]

            temp=nextState[queen1]
            nextState[queen1]=nextState[queen2]
            nextState[queen2]=temp

            nextCollision=calculateCollision(nextState)
            if nextCollision<currentCollisions:
                table=nextState
                currentCollisions=nextCollision
                nSwaps+=1
                break
            else:
                availablePairs.remove(availablePairs[index])

            #local minima found so we need a random start
            if len(availablePairs)==0:
                rndStart(table)
                currentCollisions=calculateCollision(table)
                nRndStart+=1
                break
    #viewTable(table)
    #print("  ")
    #print("  ")
    return (nSwaps,nRndStart)


def outPuts(output):
    swaps=0
    randomRestarts=0
    TTC=0
    print(f"{'Swaps    ' }{'Random Restarts       '}{'TTC'}")
    for i in range(len(output)):
        time="{:.6f}".format(output[i][2])
        print(f"{output[i][0] : ^5}{output[i][1] : ^22}{ time+' s'  : <0}")
        swaps+=output[i][0]
        randomRestarts+=output[i][1]
        TTC+=output[i][2]
    print(f"{'Swaps Mean   ' }{'Random Restarts Mean     '}{'TTC Mean'}")
    TTC="{:.6f}".format(TTC/15)
    swaps="{:.2f}".format(swaps/15)
    randomRestarts="{:.2f}".format(randomRestarts/15)
    print(f"{swaps : ^10}{randomRestarts : ^28}{ TTC+' s'  : <5}")





def main():
    numberOfqueens=8
    table= [0]*numberOfqueens
    Pairs=pairList(numberOfqueens)
    output=[]
    for i in range(15):
        start = timer()
        temp=gradientDecent(table,Pairs)
        end= timer()
        temparr=[temp[0],temp[1],end-start]
        output.append(temparr)

    outPuts(output)







if __name__ == '__main__':
    main()
