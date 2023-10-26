import csv
from math import floor
path = "C:\\Users\\diogo\\Desktop\\Mestrado\Masters\\Masters-MEI\\Assig1\\data\\";
dayInSecs = 86400;

daysOfWeek = ["Tuesday","Wednesday", "Thursday", "Friday", "Saturday","Sunday","Monday"];
months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar","Apr", "May", "Jun", "Jul", "Aug", "Sep"];
years = [1994, 1995, 1996];
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
    headerSplitted.append('Hour of Day');
    headerSplitted.append('Day');
    headerSplitted.append('Day of week');
    headerSplitted.append('Week');
    headerSplitted.append('Month');
    headerSplitted.append('Year');

    
    fileOutput.write(format(headerSplitted));
    
        
    # for row in csvreader:
    #     newRow = row[0].split(";");
        
    #     valueChanged = floor(int(newRow[1])/dayInSecs);
    #     newRow[1] = valueChanged;
        
    #     fileOutput.write(format(newRow));
    
    
    fileOutput.close();
    csvfileInput.close();
    
    
    
    
    
    

            
            
        

        
        
        