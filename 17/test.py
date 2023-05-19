# import string
#
# def abecele():
#     for r in string.ascii_letters:
#         yield r
#
#
#
# for raide in abecele():
#     print(raide)



# import itertools
#
# kvadratai = (x**2 for x in itertools.count(1))
#
# print(type(kvadratai))

def generatorius(max):
    n = 2
    while n <= max:
        yield n
        n += 2

gen = generatorius(100)
print(next(gen))









