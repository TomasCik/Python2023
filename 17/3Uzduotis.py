

for x in range(10000):
#     if x == int(pin):
#         print("Ha ha - tavo pin kodas: ", pin)
#         break

pin = "1001"
#
#



def breikeris():
    for x in range(10000):
        if x == int(pin):
            yield pin
            break



for lauziam in breikeris():
    if lauziam == pin:
        print("Ha ha - tavo pin kodas:", pin)
        break
else:
    print("kodas nerastas")








