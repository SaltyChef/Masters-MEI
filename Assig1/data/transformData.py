import csv
import datetime
path = "C:\\Users\\diogo\\Desktop\\Mestrado\Masters\\Masters-MEI\\Assig1\\data\\";


dayInSecs = 86400;
hourInSecs = 3600;
normalYearInSec = 31536000;

year = 1994;
startTime = (276 * 3600 * 24) + 25272; 


fileOutput = open(path + "dataWithDates.csv", "w");


def get_day_month_day_hour(seconds, year):
    # Convert seconds to a datetime object
    dt = datetime.datetime.fromtimestamp(seconds)

    # Set the year of the datetime object
    dt = dt.replace(year=year)

    # Subtract 1 hour from the datetime
    dt = dt - datetime.timedelta(hours=1)

    # Get the day of the week (0=Monday, 6=Sunday)
    day_of_week = dt.strftime('%A')

    # Get the month
    month = dt.strftime('%B')

    # Get the day of the month
    day_of_month = dt.day

    # Get the hour of the day
    hour_of_day = dt.strftime('%H')

    return day_of_week, month, day_of_month, hour_of_day




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
    headerSplitted.append('Hour');
    headerSplitted.append('Day');
    headerSplitted.append('Day of the week');
    headerSplitted.append('Month');
    headerSplitted.append('Year');

    
    fileOutput.write(format(headerSplitted));
    
    currentTime = startTime;   
    
    for row in csvreader:
        
        newRow = row[0].split(";");
      
        currentTime = (startTime + int(newRow[1])) ;
    
        if(currentTime < normalYearInSec):  
            year = 1994
        elif currentTime >= normalYearInSec and currentTime < 2*normalYearInSec :
            year = 1995    
        elif currentTime >= 2*normalYearInSec and currentTime < (2*normalYearInSec + startTime):
            year = 1996
        
        day_of_the_week, month, day_of_month, hour = get_day_month_day_hour(currentTime, year)
        
        newRow.append(hour);
        newRow.append(day_of_month);
        newRow.append(day_of_the_week);
        newRow.append(month);    
        newRow.append(year);    
        fileOutput.write(format(newRow));


    fileOutput.close();
    csvfileInput.close();
    
    
    
    
    
    

            
            
        

        
        
        