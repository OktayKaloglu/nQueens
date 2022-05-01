import random as rnd
# Gradient Descent approach is chosen to solve The Eight Queens problem


#The chess table has 8 rows, 8 columns and total of 64 squares
#I am using the rows as an array and store the columns as the data

#make a new two dimensional array from one dimensional array
def arrayConverter(table):
    convertedArray=[]
    for i in range(8):
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
    for j in range(7):
        print(twoD[j][tableLen-1]+rowFiller,end="")
    print(twoD[tableLen-1][tableLen-1])

# randomly assigning queens positions
#this method insures the queens wont be in the same row at the initial state
def rndStart(table):
    iniPos=[0,1,2,3,4,5,6,7]
    tableLen=len(table)
    for i in range(tableLen):
        randomIndex=rnd.randint(0,len(iniPos)-1)
        table[i]=iniPos[randomIndex]
        iniPos.remove(iniPos[randomIndex])

def calculateTheMatrix(table):
    i=1

def main():
    numberOfqueens=8
    table= [0]*numberOfqueens
    rndStart(table)
    viewTable(table)


if __name__ == '__main__':
    main()
