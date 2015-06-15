import datetime
import csv
def parseLog(filename, searchToken):
    results={}
    file = open(filename) # open log file
    for line in file: # for each in the file - read the line
       if searchToken in line:
            components = line.split(":")
            date = components[0]
            results[date] = results.get(date, 0) + 1
    return(results)
def sortDates(dateStrings):
    dates = [datetime.datetime.strptime(date, "%Y-%m-%d %H") for date in dateStrings]
    dates.sort()
    results = [date.strftime('%Y-%m-%d %H') for date in dates]
    return(results)
# MAIN PROCESS STARTS HERE
resultsForConnectionError = parseLog("master.log", "Error connecting to loggly")
resultsForServerError = parseLog("master.log", "[error]: <html>")
nonUniqueDates = list(resultsForConnectionError.keys()) + list(resultsForServerError.keys())
uniqueDates = list(set(nonUniqueDates))
sortedDates = sortDates(uniqueDates)
# sortedDates to be the .keys() value for both of the above, but only unique values (so no duplicates)
#with open("Error Count.csv", "wb") as output:
#writer = csv.writer(output)
#for date in sortedDates:
 #   output.writerow([date, resultsForConnectionError.get(date, 0), resultsForServerError.get(date, 0) ])
  #  output.close()

with open("Error Counter.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(("date", "connection errors", "server errors"))
    for date in sortedDates:
        writer.writerow((date, resultsForConnectionError.get(date, 0), resultsForServerError.get(date, 0)))

output.close()