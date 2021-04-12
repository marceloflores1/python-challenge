#Importing libraries
import os
import csv

#Filepath
budgetdata_csv = os.path.join('Resources','budget_data.csv')

#Read csv file
with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    months = 0
    net_profitloss = 0
    greatest_increase = 0
    greatest_decrease = 0
    average_change = 0
    change = 0
    prev_value = 0
    for row in csvreader: #loop through every row
        months += 1 #this will get the total months
        net_profitloss += int(row[1]) #this will get net profit and loss
        change += int(row[1])-prev_value
        if (int(row[1])-prev_value) > int(greatest_increase): #determine the greatest increase
            greatest_increase = int(row[1])-prev_value
            greatest_increase_month = row[0]
        if (int(row[1])-prev_value) < int(greatest_decrease): #determine the greatest decrease
            greatest_decrease = int(row[1])-prev_value
            greatest_decrease_month = row[0]
        prev_value = int(row[1])
    average_change = change/months
#Printing results in terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${net_profitloss}')
    print(f'Average Change: ${"{:.2f}".format(average_change)}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

#Printing results by exporting txt file
f = open("Analysis/financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("\n----------------------------")    
f.write(f'\nTotal Months: {months}')
f.write(f'\nTotal: ${net_profitloss}')
f.write(f'\nAverage Change: ${"{:.2f}".format(average_change)}')
f.write(f'\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
f.write(f'\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
#END