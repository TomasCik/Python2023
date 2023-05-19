Tekstas = "As the film begins, Jonathan Livingston Seagull is soaring through the sky hoping to travel at a speed more than 60 miles per hour (100 km/h). Eventually, with luck he is able to break that barrier, but when Jonathan returns to his own flock he is greeted with anything but applause. The Elders of the flock shame Jonathan for doing things the other seagulls never dare to do. Jonathan pleads to stay and claims that he wants to share his newfound discovery with everybody, but the Elders dismiss him as an outcast, and he is banished from the flock. "

teksto_sarasas = Tekstas.split(". ")
print(teksto_sarasas)

sauktukas = map(lambda x: x + "!", teksto_sarasas)
naujas_tekstas = " ".join(sauktukas)
print(naujas_tekstas)








