from Game import newPet, playGame
from Pet import Pet

words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump"]
# Test P1
def geninputs1():
    inputs = ['i','n']
    for i in inputs:
        yield i

def test_p1(monkeypatch):   
    GEN = geninputs1()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert currPet.game2(words[8], [0,2,3])

# def test_p2(monkeypatch):   
#    GEN = geninputs()
#    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
#    words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump"]
#    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
#    assert currPet.game2(words[8], [0,1,3])

# Test P2
def geninputs2():
    inputs = ['a','b', 'c', 'g', 'h', 'o']
    for i in inputs:
        yield i

def test_p2(monkeypatch):   
    GEN = geninputs2()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert currPet.game2(words[6], [0,1,2])

# Test P3
def geninputs3():
    inputs = ['d','d', 'a', 'j', 'm', 'p', 'r', 's', 't']
    for i in inputs:
        yield i

def test_p3(monkeypatch):   
    GEN = geninputs3()
    monkeypatch.setattr('builtins.input', lambda x: next(GEN))
    currPet = Pet('name', 1, 10, 10, 10, 0, 3, 3)
    assert currPet.game2(words[8], [0,2,3]) == False

