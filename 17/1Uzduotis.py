#
def generatorius():
    skaicius = 2
    while True:
        yield skaicius
        skaicius +=2

gen =   generatorius()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# def lyginiai(num):
#
#     lyginiai = []
#     for x in range(num):
#         if x % 2 == 0:
#             lyginiai.append(x)
#     return lyginiai
# num = 100
# lyg = lyginiai(num)
#
# print(next(lyg))

