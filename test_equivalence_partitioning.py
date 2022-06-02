import random
from Game import newPet, playGame
from Pet import Pet

import sys

"""
water(self, water):
    - Gives water to the Pet, input is the 'percentage of water given'.
    Where the pet can die if it does to many actions while with thrist on 0%.
    - Valid values: [0;100]

Partitions:
    - Valid: [0][1;9][10;99][100]
    - Invalid: [-9;-1][101;125] None String Obj Array
"""

def test_water_part0():
    from_partition = 0;
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)
    
    assert currPet.thirst == from_partition

def test_water_part1_9():
    from_partition = random.randint(1, 9)
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == from_partition

def test_water_part10_99():
    from_partition = random.randint(10, 99)
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == from_partition

def test_water_part100():
    from_partition = 100
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == from_partition

def test_water_invalid_negative():
    from_partition = -(random.randint(1, 9))
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 0

def test_water_invalid_over100():
    from_partition = random.randint(101, 125)
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 100


def test_water_invalid_none():
    from_partition = None
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 0

def test_water_invalid_string():
    from_partition = ''
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 0

def test_water_invalid_object():
    from_partition = {None: None}
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 0

def test_water_invalid_array():
    from_partition = []
    #Pet Generation with 0 Thirst
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 0

"""
ageUp(self, time):
    - Adds time to the age, making him older.
    Time inputted will be the new internal time if in valid values
    - Valid values: [86400;∞[ <- this value will be get with InputTime - InternalTime, we will consider the internalTime to be 0

Partitions:
    - Valid: [86400;99999] [100000; 999999] [1000000; 9999999] [10000000;99999999] MAXINT
    - Invalid: [0;86400][-86400;-1] None String Obj Array
"""

def test_ageUp_86400_99999():
    from_partition = random.randint(86400, 99999)
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition)


def test_ageUp_100000_999999():
    from_partition = random.randint(100000, 999999)
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition)


def test_ageUp_1000000_9999999():
    from_partition = random.randint(1000000, 9999999)
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition)

def test_ageUp_10000000_99999999():
    from_partition = random.randint(10000000, 99999999)
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition)


def test_ageUp_max_int():
    from_partition = sys.maxsize
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)
    assert Pet.ageUp(currPet, time=from_partition)


def test_ageUp_invalid_0_86400():
    from_partition = random.randint(0, 86400)
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition) == False


def test_ageUp_invalid_minus_86400_1():
    from_partition = -random.randint(1, 86400)
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition) == False


def test_ageUp_invalid_none():
    from_partition = None
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition) == False


def test_ageUp_invalid_string():
    from_partition = 'String'
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition) == False

def test_ageUp_invalid_object():
    from_partition = {None : None}
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition) == False

def test_ageUp_invalid_array():
    from_partition = []
    #Pet Generation with 0 Time
    currPet = Pet('name', 1, 90, 0, 0, False, 0, 0)

    assert Pet.ageUp(currPet, time=from_partition) == False
