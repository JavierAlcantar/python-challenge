import csv

file = open("budget_data.csv")
reader = csv.reader(file)
Total=0
ProfitLoss=list()
MonthCounter = 0
next(reader)
for row in reader:
	Total = Total + int((row[1]))
	MonthCounter = MonthCounter + 1
	ProfitLoss.append(int(row[1]))


DiffList = list()

for Difference in range(1,len(ProfitLoss)):
	DiffList.append(ProfitLoss[Difference] - ProfitLoss[Difference-1])

MaxChange = max(DiffList)
MinChange =min(DiffList)
AverageChange = sum(DiffList)/len(DiffList)



print("Financial Analysis")
print ("------------------")
print("Total Months: " + str(MonthCounter))
print(str(Total))
print ("Average Change: " + str(AverageChange))
print ("Greatest Increase in Profits: " + str(MaxChange))
print ("Greatest Decrease in Profits: " + str(MinChange))