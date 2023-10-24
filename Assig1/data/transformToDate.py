import csv
from math import floor
path = "C:\\Users\\diogo\\Desktop\\Mestrado\Masters\\Masters-MEI\\Assig1\\data\\";
dayInSecs = 86400;


fileOutput = open(path + "dataWithDates.csv", "w");



def format(row):
    line="";
    for text in row:
        line += str(text) + ";";
    line = line.removesuffix(";")
    return line + "\n";
            



with open(path+"data.csv", "r") as csvfileInput: 
   
    csvreader = csv.reader(csvfileInput);
    header = next(csvreader)[0];
    headerSplitted = header.split(";");
    headerSplitted[1] = 'Day Submited';

    fileOutput.write(format(headerSplitted));
    
        
    for row in csvreader:
        newRow = row[0].split(";");
        
        valueChanged = floor(int(newRow[1])/dayInSecs);
        newRow[1] = valueChanged;
        
        fileOutput.write(format(newRow));
    
    
    fileOutput.close();
    csvfileInput.close();
    
    
    
    
    
    

            
            
        

        
        
        