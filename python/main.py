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

def viewTable(table):
    rowFiller=" -- "
    columnFiller="|"
    twoD=arrayConverter(table)
    for i in range(7):
        for j in range(7):
            print(twoD[j][i]+rowFiller,end="")
        print(twoD[7][i])
        for j in range(7):
            print(columnFiller+"    ",end="")
        print(columnFiller)
    for j in range(7):
        print(twoD[j][7]+rowFiller,end="")
    print(twoD[7][7])


def randomAssign(table):
    


def main():
    table= [0]*8
    viewTable(table)


if __name__ == '__main__':
    main()
