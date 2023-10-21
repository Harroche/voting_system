import pytest
from voting_txt import votingSystem
import pyrankvote
from pyrankvote import Candidate, Ballot

@pytest.fixture
def votingSystemFixture1 () ->votingSystem :
    file = "voting_system_txt/test_vote1.txt" 
    numberOfSeats=1
    return votingSystem(file,numberOfSeats)

@pytest.fixture
def votingSystemFixture2 () ->votingSystem :
    file = "voting_system_txt/test_vote2.txt" 
    numberOfSeats=1
    return votingSystem(file,numberOfSeats)

def test_countVotes_candidates(votingSystemFixture1):
    sys = votingSystemFixture1
    sys.countVotes()
    #v = votingSystem("",1)
    assert sys.candidates == [Candidate("James Doe"),Candidate("Jane Doe"),Candidate("David Doe")]

def test_countVotes_ballot_and_cadidates_numbers(votingSystemFixture1):
    sys = votingSystemFixture1
    sys.countVotes()
    assert len(sys.ballot) == 101
    assert len(sys.candidates) == 3

def test_voting_results (votingSystemFixture2):
    sys = votingSystemFixture2
    sys.countVotes()
    canArr = [Candidate("James Doe"),Candidate("Jane Doe"),Candidate("David Doe"),Candidate("Jarred Doe")]
    ballotArr = [Ballot(ranked_candidates=[Candidate("James Doe"),Candidate("Jane Doe"),Candidate("David Doe"),Candidate("Jarred Doe")]),
                 Ballot(ranked_candidates=[Candidate("Jane Doe"),Candidate("James Doe"),Candidate("David Doe"),Candidate("Jarred Doe")])]
    assert sys.results().get_winners() == pyrankvote.single_transferable_vote(canArr,ballotArr,1).get_winners()
