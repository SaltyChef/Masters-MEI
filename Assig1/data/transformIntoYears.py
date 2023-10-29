import csv

path = "C:\\Users\\diogo\\Desktop\\Mestrado\Masters\\Masters-MEI\\Assig1\\data\\";

file1994 = open(path + "data1994.csv", "w");
file1995 = open(path + "data1995.csv", "w");
file1996 = open(path + "data1996.csv", "w");


def format(row):
    line="";
    for text in row:
        line += str(text) + ";";
    line = line.removesuffix(";")
    return line + "\n";


with open(path+"dataWithDates.csv", "r") as csvfileInput:
    csvreader = csv.reader(csvfileInput);
    
    csvreader = csv.reader(csvfileInput);
    header = next(csvreader)[0];
    headerSplitted = header.split(";");
    file1994.write(format(headerSplitted));
    file1995.write(format(headerSplitted));
    file1996.write(format(headerSplitted));
    
    for row in csvreader:
        
        newRow = row[0].split(";");
        
        if(newRow[22] == "1994"):
            file1994.write(format(newRow));
        if(newRow[22] == "1995"):
            file1995.write(format(newRow));
        if(newRow[22] == "1996"):
            file1996.write(format(newRow));
            
                
        
        
        
     
   