#importing modules
import os
import csv

#setting file path to read csv file containing our data
csvpath = os.path.join("Resources","budget_data.csv")

#Reading the file using CSV module

with open(csvpath,encoding="utf-8") as csvfile:

#CSV reader which uses variable csvfile (which has the contents of the file) and specifies delimiter
    csvreader = csv.reader(csvfile,delimiter=',')

#CSV header will make reader skip the row containing the headers for the data file
    csv_header = next(csvreader)

#Setting initial variable value for total and row_count, creating lists for profit loss and date
    total = 0
    date=[]
    row_count = 0
    profitloss=[]

    for row in csvreader:
        total = total + int(row[1])
        profitloss.append(int(row[1]))
        date.append(row[0])
        row_count = row_count+1
#List for Average Change and Change
    change=[]
    averagechange=[]

#for loop that compares two consecutive rows to find greatest increase and decrease
    for x in range(1, len(profitloss)):
        change.append(profitloss[x]-profitloss[x-1])
        averagechange= (sum(change)/len(change))

#setting the greatest increase and decrease values to the highest and lowest values of the 'change' list respectively
        greatestincreasechange = max(change)
        greatestdecreasechange = min(change)

#setting the date for greatest increase and decrease values the 'change' list 

        greatestincreasedate = date[change.index(max(change))+1]
        greatestdecreasedate = date[change.index(min(change))+1]

#rounding the value for average change, storing rowcount (months) value
averagechange = round(averagechange,2)
months = row_count
#printing text showing the financial analysis done on the budget data with the average change rounded to 2 decimal places
print('Financial Analysis\n----------------------------')
print('Total Months: ', months)
print('Total: $', total)
print("Average Change: $", averagechange)
print('Greatest Increase in Profits: ',greatestincreasedate, '( $', greatestincreasechange, ")")
print('Greatest Decrease in Profits: ',greatestdecreasedate, '( $', greatestdecreasechange, ")")

#writing our financial analysis output from the terminal into a text file
Financial_analysis = os.path.join("Analysis","analysis.txt")
with open(Financial_analysis,"w",) as f:
   
    f.write('Financial Analysis\n----------------------------')
    f.write('\nTotal Months: {}'.format(months))
    f.write('\nTotal: ${}'.format(total))
    f.write("\nAverage Change: ${}".format(averagechange))
    f.write('\nGreatest Increase in Profits: {} $'.format(greatestincreasechange))
    f.write('\nGreatest Decrease in Profits: {} $'.format(greatestdecreasechange))
