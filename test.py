from Game import newPet, playGame
from Pet import Pet

def geninputs():
    inputs = ['i','c','a','a','a','b']
    for i in inputs:
        yield i


def test_p1(monkeypatch):   
    GEN = geninputs()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump"]
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert currPet.game2(words[8], [0,1,2])

def test_p2(monkeypatch):   
    GEN = geninputs()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump"]
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert currPet.game2(words[8], [0,1,3])

