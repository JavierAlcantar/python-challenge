import csv

file = open("election_data.csv")
reader = csv.reader(file)
TotalVotes = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes=0

next(reader)
for row in reader:
	TotalVotes = TotalVotes + 1
	if row[2]=="Khan":
		KhanVotes = KhanVotes +1
	elif row[2]=="Correy":
		CorreyVotes = CorreyVotes + 1
	elif row[2]=="Li":
		LiVotes = LiVotes + 1
	elif row[2]=="O'Tooley":
		OTooleyVotes=OTooleyVotes + 1
		

print("Election Results")
print("-----------------------")
print("Total Votes: " + str(TotalVotes))
print("-----------------------")

print("Khan: " + "{:.2%}".format(KhanVotes/TotalVotes)+ str(" ") + str(KhanVotes))
print("Correy: " + "{:.2%}".format(CorreyVotes/TotalVotes)+ str(" ") + str((CorreyVotes)))
print("Li: "+ "{:.2%}".format(LiVotes/TotalVotes)+ str(" ") + str(LiVotes))
print("O'Tooley: " + "{:.2%}".format(OTooleyVotes/TotalVotes)+ str(" ") + str(OTooleyVotes))

print ("----------------------")
print ("Winner: Khan")
print ("----------------------")