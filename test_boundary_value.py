from Game import newPet, playGame
from Pet import Pet

"""Boundary [1,2] test: [-1,1,2,3]"""
def genBoundary1():
    choice = ['1']
    gameConditions = ['0']
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
    gameConditions = ['8','0','1','2']
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
    assert Pet.play(currPet, game=0, exp=0) is True

def genBoundary3():
    choice = ['-1']
    gameConditions = []
    inputs = choice + gameConditions
    for i in inputs:
        yield i


def test_blackbox_3(monkeypatch):
    GEN = genBoundary3()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert Pet.play(currPet, game=0, exp=0) is True
