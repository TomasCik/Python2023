import datetime

siandienos_data = datetime.datetime.now()
print(siandienos_data)

print(siandienos_data - datetime.timedelta(days=5))
print(siandienos_data - datetime.timedelta(hours=8))

print(siandienos_data.strftime("%Y %m %d, %H:%M:%S"))

