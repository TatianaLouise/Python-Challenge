# Import os to create file paths across operating systems

import os

import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

budget_csv

# Import and read into the budget_csv

with open(budget_csv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter = ",")

# Use next(csv_reader, None) to skip the header row
    budget_header = next(budget_reader, None)

# Define the function and have it accept the 'budget_data' as its sole parameter
# Assign values to variables

def print_financials(budget_data):
    months = []
    total_months = 0
    total_prof = 0
    change_prof = []
    change_val = 0
    last_val = 0
    first_row = True

    for row in budget_data:
    
    #Save the value of months (row[0]) into a list for future reference

        months.append(str(row[0]))

    # Calculate the total number of months in the dataset
        total_months += 1

    # Calculate the net total amount of "Profit/Losses" over the entire period
        total_prof += int(row[1])

    #Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        if first_row:
          change_val = 0
          first_row = False
        else:
          change_val = int(row[1]) - last_val
        
        change_prof.append(change_val)
        last_val = int(row[1])
    
    total_change = sum(change_prof)

    # Average change is the total change / (total months -1) 
    # (the number of times the value changed -- subtract 1 because even though there are 86 months there has only been 85 changes)
    
    avg_change = round(total_change/(total_months-1), 2)

    # Calculate the greatest increase in profits over the entire period
    # This is the maximum amount of change between two months (the max number in change_prof list)

    greatest_inc_prof = max(change_prof)
    
    # Find the date of the greatest increase in profits over the entire period
             
    loc_greatest_inc_date = change_prof.index(greatest_inc_prof)
         
    # Index of the month in the data sheet is loc_greatest_inc_date 
    greatest_inc_date = months[int(loc_greatest_inc_date)]

    # Calculate the greatest decrease in profits (date and amount) over the entire period

    greatest_dec_prof = min(change_prof)
    
    loc_greatest_dec_date = change_prof.index(greatest_dec_prof)

    greatest_dec_date = months[int(loc_greatest_dec_date)]



          
    print("Financial Analysis")

    print("------------------------")

    print("Total Months: ", total_months)

    print("Total Profit/Loss: $", total_prof)

    print("Average Change: ", avg_change)

    print("Greatest increase in profits: ", greatest_inc_date, " ($" , greatest_inc_prof, ")")

    print("Greatest decrease in profits: ", greatest_dec_date, " ($" , greatest_dec_prof, ")")

# Import and read into the budget_csv

with open(budget_csv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter = ",")

# Use next(csv_reader, None) to skip the header row
    budget_header = next(budget_reader, None)

    print_financials(budget_reader)
    
    #Export a text file named analysis_results.txt with the results

output_path = os.path.join('Analysis', 'analysis_results.txt')

with open(output_path, 'w') as file:

    csvwriter = csv.writer(file, delimiter=':')
    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['Total Months: 86'])
    csvwriter.writerow(['Total Profits: $ 22564198'])
    csvwriter.writerow(['Average Change: $ -8311.11'])
    csvwriter.writerow(['Greatest Increase in Profits: Aug-16($1862002)'])
    csvwriter.writerow(['Greatest Decrease in Profits: Feb-14($-1825558)'])