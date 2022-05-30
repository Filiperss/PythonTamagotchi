from Game import newPet, playGame
from Pet import Pet

"""
Test of the method play(self,game,exp)
    - attributes
        - self (the Pet object reference)
        - game: Will impact the happiness of the Pet.
        - exp: Will affect the thirst and hunger of the Pet by having played a game.

    NOTE: This attributes aren't relevant to the test, but still required to execute the method

    Boundary [1,2] 
    TBoundary Values to be tested: [-1,1,2,3]
"""
def genBoundary1():
    choice = ['1']
    gameConditions = ['0'] # Number to guess, not relevant but required to end the function
    inputs = choice + gameConditions
    for i in inputs:
        yield i


def test_blackbox_1(monkeypatch):
    GEN = genBoundary1()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert Pet.play(currPet,game=0,exp=0) is True

def genBoundary2():
    choice = ['2']
    gameConditions = ['8','0','1','2'] # Letters to be guessed, not relevant but required to end the function
    inputs = choice + gameConditions
    for i in inputs:
        yield i


def test_blackbox_2(monkeypatch):
    GEN = genBoundary1()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert Pet.play(currPet,game=0,exp=0) is True


def genBoundaryMinus1():
    choice = ['-1']
    gameConditions = []
    inputs = choice + gameConditions
    for i in inputs:
        yield i


def test_blackbox_minus1(monkeypatch):
    GEN = genBoundaryMinus1()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert Pet.play(currPet, game=0, exp=0) is False

def genBoundary3():
    choice = ['3']
    gameConditions = []
    inputs = choice + gameConditions
    for i in inputs:
        yield i


def test_blackbox_3(monkeypatch):
    GEN = genBoundary3()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert Pet.play(currPet, game=0, exp=0) is False
