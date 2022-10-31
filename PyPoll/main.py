#importing modules
import os
import csv

#setting file path to csv file containing our data
csvpath = os.path.join("Resources","election_data.csv")

def percent(portion,whole):
    return (float(portion)/float(whole)*100)

#Reading the file using CSV module
with open(csvpath,encoding='utf-8') as csvfile:

#CSV reader which uses variable csvfile (which has the contents of the file) and specifies delimiter
    csvreader = csv.reader(csvfile,delimiter=',')

#CSV header will make reader skip the row containing the headers for the data file
    csv_header= next(csvreader)

#Function that creates a list containing each candidate vote per row in the election data
    candidatelist = [row[2] for row in csvreader]

#Votingtotal is the amount of rows (votes) in the list above
    votingtotal = len(candidatelist)

#Function that creates a list of list elements (candidate and candidate voter count) for each unique candidate
    candidatevotecount = [[candidate, candidatelist.count(candidate)] for candidate in set(candidatelist)]

#Function that rearranges the list in descending order of vote count
    candidatevotecount = sorted(candidatevotecount, key=lambda k:k[1], reverse= True)

#Functions that will find the vote percentage per candidate when compared to the grand total
    dianapercent = percent(candidatevotecount[0][1],votingtotal)
    charlespercent = percent(candidatevotecount[1][1],votingtotal)
    raymonpercent = percent(candidatevotecount[2][1],votingtotal)

#This code will print out our output on the terminal
print('Election Results\n-------------------------')
print('Total Votes: {}'.format(votingtotal))
print(f'Charles Casper Stockham: {charlespercent:.3f}% ({candidatevotecount[1][1]})')
print(f'Diana DeGette: {dianapercent:.3f}%  ({candidatevotecount[0][1]})')
print(f'Raymon Anthony Doane: {raymonpercent:.3f}% ({candidatevotecount[2][1]})' )
print('-------------------------')
print('Winner: {}'.format(candidatevotecount[0][0]))

#This code is setting up the path where our analysis output file will be created, as well as what will be written in the file when the script is ran
output_file = os.path.join("Analysis","analysis.txt")
with open(output_file,"w") as f:
    f.write('Election Results\n-------------------------')
    f.write('\nTotal Votes: {}'.format(votingtotal))
    f.write(f'\nCharles Casper Stockham: {charlespercent:.3f}% ({candidatevotecount[1][1]})')
    f.write(f'\nDiana DeGette: {dianapercent:.3f}%  ({candidatevotecount[0][1]})')
    f.write(f'\nRaymon Anthony Doane: {raymonpercent:.3f}% ({candidatevotecount[2][1]})' )
    f.write(f'\n-------------------------')
    f.write('\nWinner: {}'.format(candidatevotecount[0][0]))