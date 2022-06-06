from tkinter import *
root= Tk()





label_month = Label(root)
label_profit = Label(root)

label_max_month = Label(root)
label_min_profit = Label(root)



month = ("january","feburary","march","april","may","june","july","august","september","october","november","december")
profit = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)
 

label_month["text"] = "Months :" + str(month)
label_profit["text"] = "Profits :" +str(profits)

def maxProfits();
    max_profit = max(profit)
    max_profit_index = profit.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_profit["text"] = " maximum profit of" +str(max_profit)+"was given in the month of" +str(max_profit_month)

def minProfits();
   min_profit = min(profit)
   min_profit_index = profit.index(min_profit)
   min_profit_month = month[min_profit_index]
   label_min_profit["text"] = " minimum profit of" +str(min_profit)+"was given in the month of" +str(min_profit_month)