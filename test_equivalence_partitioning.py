import random
from Game import newPet, playGame
from Pet import Pet


"""
water(self, water):
    - Gives water to the Pet, input is the 'percentage of water given'.
    Where the pet can die if it does to many actions while with thrist on 0%.
    - Valid values: [0;100]

Partitions:
    - Valid: [0][1;9][10;99][100]
    - Invalid: [-9;-1][101;125] None String Obj Array
"""
# def test_water():
#     #Equivalence Inputs
#     equivalence_valid_inputs = [
#         0,
#         random.randint(1, 9),
#         random.randint(10,99),
#         100
#     ]

#     equivalence_invalid_inputs = [
#         -(random.randint(1, 9)),
#         random.randint(101, 125),
#         None,
#         'string',
#         {None : None},
#         []
#     ]
    
#     #Catch Errors
#     errors = []

#     for value in equivalence_valid_inputs:
#         #Pet Generation with 0 Thirst
#         currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
#         #Call the Function to be tested
#         Pet.water(currPet, water= value )
#         if currPet.thirst != value: 
#             errors.append(value)

#     for value in equivalence_invalid_inputs:
#         #Pet Generation with 0 Thirst
#         currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
#         #Call the Function to be tested
#         try:
#             Pet.water(currPet, water=value)
#             if currPet.thirst != 0 and (currPet.thirst != 100 and (value >= 101 and value <= 125)):
#                 errors.append(value)
#             print(str(value) + " - " + str(currPet.thirst))
#         except: 
#             print("E: "+ str(value) + " - " + str(currPet.thirst))
#             errors.append(value)
#             continue

#     assert not errors, "errors occured: " + str(errors)

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
    currPet = Pet('name', 1, 90, 0, 0, False, 3, 3)
    Pet.water(currPet, water=from_partition)

    assert currPet.thirst == 0
