import re

lines = open("apn.h", "r").readlines()

count = 0
apns = 0
countries = {}
for line in lines:
    if "{.mcc=" in line:
        iso = re.findall(r'iso="(.+?)"', line)
        country = re.findall(r'country="(.+?)"', line)
        countries[iso[0]] = country[0]
        count = count + 1
        if not ".apn=\"\"" in line:
            apns = apns + 1

print(count)
print(apns)

print(len(countries))
print(countries)

with open("README.md", "w") as f:
    f.write("# apni-list\n")
    f.write("List of apn settings\n\n")
    f.write("## status\n")
    f.write(str(apns) + " out of "+ str(count) + " apns available from "+ str(len(countries))+ " countries\n")
    f.close()
