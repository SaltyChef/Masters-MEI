
f = open("dados.txt", "r")
fout = open("newDados.csv", "w")
txt = f.readlines()

for line in txt: 
    line = line.split(" ")
    newLine = ""
    for inLine in line:
        if(inLine != ""):
            newLine += inLine + ";"
    newLine = newLine.removesuffix(";")
    fout.write(newLine)        
    
    


