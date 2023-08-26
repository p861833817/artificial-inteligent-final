import argparse
import numpy as np

def makeTMT(S,table,K,List):
    TMT=[]
    pointIndex = 0
    for point in S:
        numberOfP = int(List[pointIndex])
        row = []
        count = K
        while True:
            row.append(0) 
            count = count - 1
            if count == 0:
               break
        if numberOfP != 0:
            probability = 1/numberOfP
        else:
            probability = 0
            continue
        indexList = createIndexList(table[pointIndex],point,S,K)
        for index in indexList:
            row[index] = probability
        TMT.append(row)
        pointIndex = pointIndex +1 
    return TMT
                   
def createIndexList(string,point,S,K):
    List = []
    num1 = int(point[0])
    num2 = int(point[1])
    stringList = list(string)
    if stringList[0] == "0":
        tuple = (num1-1,num2)
        num = S.index(tuple)
        List.append(num)
    if stringList[1] == "0":
        tuple = (num1+1,num2)
        num = S.index(tuple)
        List.append(num)
    if stringList[2] == "0":
        tuple = (num1,num2-1)
        num = S.index(tuple)
        List.append(num)
    if stringList[3] == "0":
        tuple = (num1,num2+1)
        num = S.index(tuple)
        List.append(num)
    return List
           
                
def getFI(table,row,column):
    empatYList = []
    for i in range(row):
        for j in range(column):
            if table[i][j] == "X":
                continue
            else:
                add = table[i][j]
                empatYList.append(add)
    return empatYList
                
def creatEmission(Y,fourIndex,errorRate):
    EmissionTble = []
    for observation in Y:
        add=[]
        obList = list(observation)
        for points in fourIndex:
            tupleList = list(points)
            falseNumber = compare(obList,tupleList)
            errorProbability = ((1-errorRate)**(4-falseNumber)) * (errorRate **falseNumber)
            add.append(errorProbability)
        EmissionTble.append(add)
    return EmissionTble
                
def compare(obList,tupleList):
    num = 0
    for i in range(4):
        if obList[i] != tupleList[i]:
            num = num +1
    return num
                           
def makePart1(emissionMatrixTable,initialProbabilities):
    returnList = []
    for matrixs in emissionMatrixTable[0]:
        add = matrixs * initialProbabilities
        returnList.append(add)
    return returnList
               

def findIndex(O,rows,columns):
    newTable = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if O[i][j] == "X":
                add = "X"
            else:
                Nindex = getNIndex(i,j,O,rows,columns)
                Sindex = getSIndex(i,j,O,rows,columns)
                Windex = getWIndex(i,j,O,rows,columns)
                Eindex = getEIndex(i,j,O,rows,columns)
                add = Nindex + Sindex + Windex + Eindex
            row.append(add)
        newTable.append(row)
    return newTable

def findNeighbor(i,j,O):
    if O[i][j] == "X":
        return "1"
    else:
        return "0"

def getNIndex(i,j,O,row,columns):
    new = "1"
    if i == 0:
        return new
    else:
        new = findNeighbor(i-1,j,O)
        return new
    
def getSIndex(i,j,O,row,columns):
    new = "1"
    if i == row - 1:
        return new
    else:
        new = findNeighbor(i+1,j,O)
        return new
    
def getWIndex(i,j,O,row,columns):
    new = "1"
    if j == 0:
        return new
    else:
        new = findNeighbor(i,j - 1,O)
        return new

def getEIndex(i,j,O,row,columns):        
    new = "1"
    if j == columns - 1:
        return new
    else:
        new = findNeighbor(i,j +1,O)
        return new


def makeNeighborNumber(table):
    newList=[]
    for line in table:
        for point in line:
            if point == "X":
                continue
            else:
                num = point.count("0")
                newList.append(str(num))
    return newList
                
def makeTable(row,O):
        rowIndex = 0
        newTable = []
        for lines in O:
            rowline = []
            for point in lines:
                if point == "X":
                    add = "X"
                else:
                    add = row[rowIndex]
                    rowIndex = rowIndex +1
                rowline.append(add)
            newTable.append(rowline)
        return newTable    

def makeRow(part1,emissionTable ,fourIndex,O,round,S,listNumber):
    newList = []
    pointIndex = 0
    for x,rowlist in enumerate(O):
        for y,point in enumerate(rowlist):
            if O[x][y] == "X":
                continue
            else:
                tuple1 = (x+1,y+1)
                num1 = 0
                for n,nodes in enumerate(S):
                    if nodes == tuple1:
                        num1 = n
                basicProbabily = getBasic(emissionTable,round,num1)
                pointFourIndex = fourIndex[pointIndex]
                neighborList = findItsNeighbor(x+1,y+1,pointFourIndex)
                if len(neighborList) == 0 :
                    newList.append(0)
                    pointIndex = pointIndex +1
                    continue
                probabilityList = []
                for neighbor in neighborList:
                    po = findNeighborsNumber(neighbor,part1,S,listNumber)
                    probabilityList.append(po)
                num = max(probabilityList) * basicProbabily
                pointIndex = pointIndex +1
                newList.append(num)
    return newList

def getBasic(table,round,num1):
    return table[round][num1]


def findNeighborsNumber(neighbor,part1,S,listNumber):
    num1 = neighbor[0]
    num2 = neighbor[1]
    neighborIndex = S.index(neighbor)
    po = 0
    numberOfNeighbor = listNumber[neighborIndex]    
    po = 1/int(numberOfNeighbor)
    numberPro = part1[neighborIndex]
    return po * numberPro
    
                
def findItsNeighbor(x,y,string):
    nList = []
    stringList = list(string)
    if stringList[0] == "0":
        add = (x-1,y)
        nList.append(add)
    if stringList[1] == "0":
        add = (x+1,y)
        nList.append(add)
    if stringList[2] == "0":
        add = (x,y-1)
        nList.append(add)
    if stringList[3] == "0":
        add = (x,y+1)
        nList.append(add)
    return nList
    
                         
                              
def main():
    parser = argparse.ArgumentParser(description="process inputs")
    parser.add_argument('inputFile', help='loading input file...')
    args = parser.parse_args()
    inputs = args.inputFile
    with open(inputs, "r") as file:
        lines = file.readlines()

    line = lines[0].split()
    row = int(line[0])
    column = int(line[1])
    i = 0
    O = []
    K = 0
    S = []
    line_index = 1
    while i < row:
        line = lines[line_index].split()
        j = 0
        row_list = []
        while j < column:
            if line[j] == "0":
                K += 1
                xIndex = i + 1
                yIndex = j + 1
                add = (xIndex,yIndex)
                S.append(add)
            row_list.append(line[j])
            j += 1
        O.append(row_list)
        i += 1
        line_index += 1
    line = lines[line_index].split()
    count = int(line[0])
    Y = []
    line_index += 1
    while count > 0:
        Y.append(lines[line_index].strip())
        count -= 1
        line_index += 1

    errorRate = float(lines[line_index].strip())
    initialProbabilities = 1 / K
    tableFourIndex= findIndex(O,row,column)
    
    fourIndex = getFI(tableFourIndex,row,column)
    listNumberOfNeighbor = makeNeighborNumber(tableFourIndex)
    transitionMatrixTable = makeTMT(S,fourIndex,K,listNumberOfNeighbor)
    
    emissionMatrixTable = creatEmission(Y,fourIndex,errorRate)
    TrellisMatrix = []
    
    part1 = makePart1(emissionMatrixTable,initialProbabilities)
    TrellisMatrix.append(part1)
    counter = len(Y)
    round = 1
    while True:
        MatrixPart = makeRow(part1,emissionMatrixTable ,fourIndex,O,round,S,listNumberOfNeighbor)
        TrellisMatrix.append(MatrixPart)
        part1 = MatrixPart
        round = round+1
        if round == counter:
            break
    data_dict = {}
    num = 1
    for arrays in TrellisMatrix:
        data1 = makeTable(arrays,O)
        data1 = [[0 if val == 'X' else val for val in row] for row in data1]
        array = np.array(data1)
        string = "array" + str(num)
        num = num +1
        data_dict.update({string:array})
    np.savez("output.npz", **data_dict)
    
    
    
    
    
    
    
    

                
        
        
        
    
        
    
        
main()