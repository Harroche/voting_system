import pyrankvote
from pyrankvote import Candidate, Ballot

file = open("voting_system_txt/votes.txt","r")
lineForCan = file.readline().replace("\n","")
canArr= lineForCan.split('\t') #places candiates in array
candidates = []
seats=int(input("input the amount of seats for postion: "))
#puts in both an array and dict
for can in canArr:
    candidates.append(Candidate(can))
file.seek(0)
lines = file.readlines()
ballot=[]
for line in lines:  #the rest of the lines
    line.replace("\n","")
    standing=line.split()
    ballotArray = []
    for can in standing:
        ballotArray.append(Candidate(can))
    ballot.append(Ballot(ranked_candidates=ballotArray))

#prints election results 
election_results = pyrankvote.single_transferable_vote(candidates,ballot,seats)
print(election_results)
