import pyrankvote
from pyrankvote import Candidate, Ballot

class votingSystem:

    def __init__(self,path,seats) -> None:
        self.file_array = open(path,"r").readlines()
        self.candidates = []
        self.ballot =[]
        self.numberOfSeats = seats

    def countVotes (self) -> None:
        candidates_init=self.file_array[0].replace("\n","").split('\t')
        for candid in candidates_init:
            self.candidates.append(Candidate(candid))
        for vote in self.file_array:
            placements=vote.replace("\n","").split('\t')
            ranking =[]
            for place in placements:
                ranking.append(Candidate(place))
            self.ballot.append(Ballot(ranked_candidates=ranking))
    
    def results (self) -> object:
        return pyrankvote.single_transferable_vote(self.candidates,self.ballot,self.numberOfSeats)


def main():
    file = "voting_system_txt/votes.txt"
    numberOfSeats = int(input("Input the amount of seats for postion: "))
    sys=votingSystem(file,numberOfSeats)
    sys.countVotes()
    print(sys.results())

if __name__ == '__main__':
    main()