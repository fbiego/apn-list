import re

lines = open("apn.h", "r").readlines()

x = 0
c = 0
lastC = ""
count = 0
apns = 0
countries = {}
for line in lines:
    x = x + 1
    if "{.mcc=" in line:
        iso = re.findall(r'iso="(.+?)"', line)[0]
        country = re.findall(r'country="(.+?)"', line)[0]
        if lastC != country:
            lastC = country
            c = x
        det = {"name": country, "start": c, "end": x}
        countries[iso] = {"name": country}
        countries[iso] = det
        count = count + 1
        if not ".apn=\"\"" in line:
            apns = apns + 1


print(count)
print(apns)

print(len(countries))

with open("README.md", "w") as f:
    f.write("# apni-list\n")
    f.write("List of apn settings\n\n")
    f.write("## status\n")
    f.write(str(apns) + " out of "+ str(count) + " apns available from "+ str(len(countries))+ " countries\n")
    f.write("## Countries\n")
    for cn in countries:
        f.write("["+ str(countries[cn]["name"]) + "](https://github.com/fbiego/apn-list/blob/main/apn.h#L"+ str(countries[cn]["start"])+"-L"+str(countries[cn]["end"])+")\n")
    f.close()
