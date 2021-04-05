import os
import csv
import datetime


employeedata_csv = os.path.join('Resources','employee_data.csv')
export_csv = os.path.join('Export','employee_data.csv')

with open(employeedata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    employees = []
    for row in csvreader:
        emp_id = row[0]
        first_name, last_name = row[1].split(" ")
        new_date = datetime.datetime.strptime(row[2],'%Y-%m-%d').strftime('%m/%d/%Y')
        ssn = str(row[3])
        new_ssn = '***-**-' + ssn[7:]
        us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
        }
        abb_state = us_state_abbrev[row[4]]
        rows = [emp_id, first_name, last_name, new_date, new_ssn, abb_state]
        employees.append(rows)
new_header = ['Emp ID','First Name','Last Name','DOB','SSN','State']
with open(export_csv, 'w') as csvfile1:
    csvwriter = csv.writer(csvfile1, delimiter=',')
    csvwriter.writerow(new_header)
    csvwriter.writerows(employees)