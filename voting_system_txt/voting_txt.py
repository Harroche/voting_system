import pyrankvote
from pyrankvote import Candidate, Ballot

# #opens file 
# file = open("STV/votes.txt","r")
# lineForCan = file.readline().replace("\n","")
# canArr= lineForCan.split('\t') #places candiates in array
# candidates =[]
# canDict ={}
# count =0
# #puts in both an array and dict
# for can in canArr:
#     candidates.append(Candidate(can))
#     canDict.update({canArr[count]: Candidate(can)})
#     count+=1
 
# lines = file.readlines()
# ballot=[]
# #puts all the votes in the ballot 
# ballot.append(Ballot(ranked_candidates=[canDict.get(canArr[0]),canDict.get(canArr[1]),canDict.get(canArr[2])])) #first  line
# for line in lines:  #the rest of the lines
#     line.replace("\n","")
#     standing=line.split()
#     ballot.append(Ballot(ranked_candidates=[Candidate(standing[0]),Candidate(standing[1]),Candidate(standing[2])]))

# #prints election results 
# election_results = pyrankvote.single_transferable_vote(candidates,ballot,1)
# print(election_results)
#opens file 
file = open("STV/votes.txt","r")
lineForCan = file.readline().replace("\n","")
canArr= lineForCan.split('\t') #places candiates in array
candidates = []
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
election_results = pyrankvote.single_transferable_vote(candidates,ballot,1)
print(election_results)