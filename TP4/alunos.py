

d = {}

def readAndPrintAlunos():
    f = open("alunos.csv", "r")
    for line in f:
        print(line)
    f.close()


def howManyLines():
    f = open("alunos.csv", "r")
    counter = 0;
    for line in f:
        if line != "\n":
            counter += 1
    f.close()

    return counter

def createDictionary():
    f = open("alunos.csv", "r")
    ans = {}
    counter = 0
    for line in f:
        if(counter != 0):
            parsedLine = line.split(",")
            idAl = parsedLine[0].split('"')[1]
            name = parsedLine[1].split('"')[1]
            curso = parsedLine[2].split('"')[1]
            tpc1 = -1
            tpc2 = -1
            tpc3 = -1
            tpc4 = -1
            if(len(parsedLine) == 7):
                tpc1 = parsedLine[3]
                tpc2 = parsedLine[4]
                tpc3 = parsedLine[5]
                tpc4 = parsedLine[6].split("\n")[0]         
            elif(len(parsedLine) == 6):   
                tpc1 = parsedLine[3]
                tpc2 = parsedLine[4]
                tpc3 = parsedLine[5].split("\n")[0]           
            elif(len(parsedLine) == 5):   
                tpc1 = parsedLine[3]
                tpc2 = parsedLine[4].split("\n")[0]     
            elif(len(parsedLine == 4)):
                tpc1 = parsedLine[3].split("\n")[0]
            elif(len(parsedLine == 3)):
                curso = parsedLine[2].split("\n")[0]
            ans[(parsedLine[0].split('"'))[1]] = {}           
            ans[(parsedLine[0].split('"'))[1]]["id_aluno"] = idAl
            ans[(parsedLine[0].split('"'))[1]]["nome"] = name
            ans[(parsedLine[0].split('"'))[1]]["curso"] = curso
            ans[(parsedLine[0].split('"'))[1]]["tpc1"] = tpc1
            ans[(parsedLine[0].split('"'))[1]]["tpc2"] = tpc2
            ans[(parsedLine[0].split('"'))[1]]["tpc3"] = tpc3
            ans[(parsedLine[0].split('"'))[1]]["tpc4"] = tpc4          
        counter += 1
    f.close()
    return ans

def topAverage(num):
    bestAvs = []
    bestNames = []
    i = 0
    while i < num:
        bestAvs.append(0)
        bestNames.append("")
        i += 1
    for value in d.keys():
        id_al = d[value]["id_aluno"]
        name = d[value]["nome"]
        tpc1 = int(d[value]["tpc1"])
        tpc2 = int(d[value]["tpc2"])
        tpc3 = int(d[value]["tpc3"])
        tpc4 = int(d[value]["tpc4"])
        av = (tpc1 + tpc2 + tpc3 + tpc4) / 4
        for i in range(0, num):
            if av > bestAvs[i]:
                bestAvs[i] = av
                bestNames[i] = id_al + " - " + name
                break
    return bestNames

def withoutOneOrMoreTPC():
    counter = 0
    for value in d.keys():
        tpc4 = int(d[value]["tpc4"])
        if(tpc4 == -1): 
            counter += 1
    return counter
    
def averageBetterThan15InLEI():
    counter = 0
    for value in d.keys():
        tpc1 = int(d[value]["tpc1"])
        tpc2 = int(d[value]["tpc2"])
        tpc3 = int(d[value]["tpc3"])
        tpc4 = int(d[value]["tpc4"])
        av = (tpc1 + tpc2 + tpc3 + tpc4) / 4
        if av > 15:
            counter += 1
    return counter