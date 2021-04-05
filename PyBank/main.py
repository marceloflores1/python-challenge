import os
import csv

budgetdata_csv = os.path.join('Resources','budget_data.csv')

with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    months = 0
    net_profitloss = 0
    greatest_increase = 0
    greatest_decrease = 0
    average_change = 0
    for row in csvreader:
        months += 1
        net_profitloss += int(row[1])
        if int(row[1]) > int(greatest_increase):
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        if int(row[1]) < int(greatest_decrease):
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
    average_change = net_profitloss/months        
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${net_profitloss}')
    print(f'Average Change: ${"{:.2f}".format(average_change)}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

f = open("Analysis/Financial Analysis.txt", "w")
f.write("Financial Analysis")
f.write("\n----------------------------")    
f.write(f'\nTotal Months: {months}')
f.write(f'\nTotal: ${net_profitloss}')
f.write(f'\nAverage Change: ${"{:.2f}".format(average_change)}')
f.write(f'\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
f.write(f'\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
