import re

lines = open("apn.h", "r").readlines()

x = 0
c = 0
i = 0
j = 0
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
            i = 0
        
        if not ".apn=\"\"" in line:
            apns = apns + 1
            if i == 0:
                j = j + 1
            i = i + 1
        det = {"name": country, "start": c, "end": x, "count" : i}
        countries[iso] = {"name": country}
        countries[iso] = det
        count = count + 1


print(count)
print(apns)
print(len(countries))

with open("README.md", "w") as f:
    f.write("# apn-list\n")
    f.write("List of apn settings\n\n")
    f.write("[![Script](https://github.com/fbiego/apn-list/actions/workflows/main.yml/badge.svg)](https://github.com/fbiego/apn-list/actions/workflows/main.yml)\n")
    f.write("## Status\n")
    f.write("| Description | Available | Total |\n")
    f.write("| --- | --- | --- |\n")
    f.write("| APN Settings | "+ str(apns) + " | "+ str(count) + " |\n")
    f.write("| Countries | " + str(j) + " | "+ str(len(countries))+ " |\n")
    f.write("\n")
    f.write("## Contributing\n")
    f.write("- Add apn settings on the existing list then modify the apn, user & pass or\n")
    f.write("- Add new apn settings below the country\n\n")
    #f.write('`{.mcc=412, .mnc=01, .code=93, .iso="af", .country="Afghanistan", .network="AWCC", .apn="", .user="", .pass=""},`\n')
    f.write("- Submit a PR\n\n")
    f.write("NB: Do not run the python script\n\n")
    f.write("## Countries\n")
    f.write("| Country | Available | APNs |\n")
    f.write("| --- | --- | --- |\n")
    for cn in countries:
        f.write("| [`"+ str(countries[cn]["name"]) + "`](https://github.com/fbiego/apn-list/blob/main/apn.h#L"+ str(countries[cn]["start"])+"-L"+str(countries[cn]["end"])+") | "+str(countries[cn]["count"])+" | "+str(countries[cn]["end"] + 1 - countries[cn]["start"])+" |\n")
    f.close()
