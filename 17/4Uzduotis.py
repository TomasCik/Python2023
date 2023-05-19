

import os
def eilutes ():

    with open("zuvedra.txt", 'r', encoding='utf-8') as failas:
        for eilute in failas:
            yield eilute.strip()


text  = eilutes()
print(next(text))

print(next(text))
print(next(text))
print(next(text))
print(next(text))















