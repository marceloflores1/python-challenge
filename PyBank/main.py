import os
import csv

budgetdata_csv = os.path.join('Resources','budget_data.csv')

with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    months = -1
    net_profitloss = 0
    greatest_increase = 0
    greatest_decrease = 0
    average_change = 0
    for row in csvreader:
        if months == 0:
            print('Financial Analysis')
            print('----------------------------')
            months += 1
        else:
  #          print(f'\t{row[0]} date and {row[1]} profit/loss')
            months += 1
            net_profitloss += int(row[1])
            if int(row[1]) > int(greatest_increase):
                greatest_increase = int(row[1])
                greatest_increase_name = row[0]
            if int(row[1]) < int(greatest_decrease):
                greatest_decrease = int(row[1])
                greatest_decrease_name = row[0]
            
    print(f'Total Months: {months}')
    print(f'Total: {net_profitloss}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_name} {greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease_name} {greatest_decrease}')

    
