import re

text = """ Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020
"""

pattern = re.compile(r"(.*?)\:\s*(.*\d{4})")
result = pattern.findall(text)

for nr, item in enumerate(result, 1):
    event = item[0]
    date = item[1]
    print(f"\n{nr}.")
    print("Event:", event)
    print("Date:", date)











