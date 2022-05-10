import random as rnd
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
        for j in range(i,nQueens):
            # the 2 queens can be in the same axis or diagonal line
                        


    return collisions



# a function that gets 2 random queens and it checks whether new state is better than current one
    # and swaps the queens positions as new positions.
    # if the current table has zero collisions that is a solution
    # if no queen can swap
def gradientDecent(table):



def main():
    numberOfqueens=5
    table= [0]*numberOfqueens
    rndStart(table)





if __name__ == '__main__':
    main()
