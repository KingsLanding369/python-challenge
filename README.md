# python-challenge
## PyBank:

My task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

Firstly,  I use codes to open and read the csv file

I then use next(reader) to get the first row and int(first_row[1]) to get the next row for profit and loss

I then set count = 1 and use the for loop to loop though all the rows in the file

with count = count + 1 inside the for loop, I get the total of months at the end.

* The net total amount of "Profit/Losses" over the entire period

I set total = previous_net, and with total = total + int(row[1])  in the for loop I get the total amount of profit/loss over the period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

I use net_change = int(row[1])-previous_net and PL_net_change_list.append(net_change) in the for loop to append the net changes into a list.

I also use previous_net = int(row[1] to change previous net value to current row's profit and loss.

This will give us the changes in P/L over the period and we can calculate the average from there.

* The greatest increase in profits (date and amount) over the entire period

To get the greatest increase, we use MAX function for the P/L net change list

* The greatest decrease in profits (date and amount) over the entire period

To get the greatest decrease, we use MIN function for the P/L net change list