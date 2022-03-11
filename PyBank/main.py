# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
   
    # To get the first row
    first_row  = next (reader)
    
    # To get the next row profit/loss
    previous_net = int(first_row[1])

    count = 1
    total = previous_net
    PL_net_change_list =[]
    
    for row in reader:
        count = count + 1
        total = total + int(row[1]) 
        #net_change = previous_net-(int(row[1]))
        net_change = int(row[1])-previous_net
        PL_net_change_list.append(net_change)
        # change previous net value to current row's profit and loss
        previous_net = int(row[1])
    #print(PL_net_change_list)
      
    average =  round((sum(PL_net_change_list)/len(PL_net_change_list)),2) 
    
    
    greatest_profit = max(PL_net_change_list)
    greatest_loss = min(PL_net_change_list)

    # print (PL_net_change_list)
    print ("Total Months: " ,count)
    print ("Total: " ,"$",total)
    print ("Average net_change: ","$",average)
    print ("Greatest Increase in Profit: ","$",greatest_profit)
    print ("Greatest Decrease in Profit: ","$",greatest_loss)
    
 # Print the results to "PyBank.txt" file
    print(f"Total Months: {count}", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Total: $ {total}", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Average net_change: $ {average}", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Greatest Increase in Profit: {greatest_profit}", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Greatest Decrease in Profit: {greatest_loss}", file=open("PyBank.txt", "a"))