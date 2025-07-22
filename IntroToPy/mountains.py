import ast
import statistics
tari = {}
munti = {}
inalt = {}
names = []
count= 0
with open("IntroToPy/mountains_db.tsv", "r",encoding= "UTF-8") as data:
    for line in data.readlines():
        part = line.split("\t", -1)
        #print(f"{part[0]} _ {part[1]} _ {part[2]} _ {part[3]}")
        names.append(part[0])
        if part[0] not in munti:
            munti[part[0]] = []
        munti[part[0]].append(count)
        if part[1] not in inalt:
            inalt[part[1]] = []
        inalt[part[1]].append(count)
        if part[2] not in tari:
            tari[part[2]] = []
        tari[part[2]].append(count)
        count += 1
print(f"THe number of countries :: {len(tari.keys())}")
print(f"The unmber of unknown altitudes :: {len(inalt["NULL"])}")
sort_inalt = sorted(inalt.keys())
sort_inalt.pop()
sort_inalt = [round(float(x)) for x in sort_inalt]
#print(f"{names[[inalt[smth]][0]]}")
print(f"Minimum altitude :: {sort_inalt[0]}; Maximum random :: {sort_inalt[-1]} ")
print(f"The average value of altitude :: {statistics.mean(sort_inalt)}")
print(f"Median of the heights :: {statistics.median(sort_inalt)}")
topp =int( input("How many mountains should be on the podium? \n"))
lopp =0
print(f"{names[791]}")
if topp > len(sort_inalt):
    topp = len(sort_inalt)
    print(f"Hey! Those are too many mountains!")
    print(f"There are only {topp} mountains to show:")
for n in range(1,int(topp)):
    place = sort_inalt[int(-n)]
    if str(place) not in inalt:
        print(place)
        break
    for h in inalt[str(place)]:
        if lopp < topp:
            print(f"The number {lopp+1} place goes to {names[h]}")
            lopp+=1
