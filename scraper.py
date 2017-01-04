from selenium import webdriver
from operator improt itemgetter
import time

rangeend = 67
matrix = [[0]*(rangeend + 1) for i in range(rangeend + 1)]
desiredratio = 1.0
out = []

currencyNames = ["Reserved", "Alteration", "Fusing", "Alchemy", "Chaos", "Gemcutter", "Exalt", "Chromatic", "Jeweller", "Chance", "Chisel", "Scouring", "Blessed",
    "Regret", "Regal", "Divine", "Vaal", "Wisdom", "Portal", "Armourer", "Whetstone", "Glassblowers", "Transmutation", "Augmentation", "Mirror", "Eternal", "Perandus",
    "Silver", "Sacrafice at Dusk", "Sacrafice at Midnight", "Sacrafice at Dawn", "Sacrafice at Noon", "Mortal Grief", "Mortal Rage", "Mortal Hope", "Mortal Ignorance",
    "Ebers", "Yriels", "Inya", "Volkuur", "Offering", "Fragment of the hydra", "phoenix", "Minotaur", "Chimera", "Apprentice Sextant", "Journeyman Sextant",
    "Master Sextant", "Sacrifce Set", "Mortal Set", "Pale Court Set", "Shaper set", "Spliter of Xoph", "Splinter of Tul", "Splinter of Esh", "Splinter of Uul-Netol", "Splinter of Chayula", "Xoph",
    "Blessing of Tul", "Blessing of Esh", "Blessing of Uul-Netol", "Blessing of Chayula", "Xophs Breechstone", "Tuls Breechstone", "Eshs Breechstone", "Uul-netol breechstone", "Chayula Breechstone"]

br = webdriver.PhantomJS('phantomjs')

#br.get('http://currency.poe.trade/search?league=Breach&online=x&want=1-2-3-4-5-6-7-8&have=1-2-3-4-5-6-7-8')
br.get('http://currency.poe.trade/search?league=Breach&online=x&want=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-35-27-28-29-30-31-32-33-34-36-37-38-39-40-41-42-43-44-45-46-47-48-49-50-51-52-53-54-55-56-57-58-59-60-61-62-63-64-65-66&have=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-35-27-28-29-30-31-32-33-34-36-37-38-39-40-41-42-43-44-45-46-47-48-49-50-51-52-53-54-55-56-57-58-59-60-61-62-63-64-65-66')

time.sleep(10)
src = br.page_source
sep = src.split('\n')
for line in sep:
	if "class=\"displayoffer\"" in line:
		tag = line.split('>')[0]
		data = tag.split('"')[1::2]
		buytype = int(data[2])
		buyamt = data[5]
		selltype = int(data[4])
		sellamt = data[3]
		user = data[6]
		if matrix[buytype][selltype] == 0:
			matrix[buytype][selltype] = float(float(sellamt)/float(buyamt))


#for i in range(1, rangeend):
#	print matrix[i][1:rangeend]

# Cycles of length 2
for i in range(1, rangeend):
    for j in range(1, i):
        if i != j:
            actualratio = (matrix[i][j] * matrix[j][i])
            if  actualratio > desiredratio:
                s = "Cycle of length 2 R: " + str(actualratio) +  " detected from " + str(currencyNames[i]) + " to " + str(currencyNames[j]) + " to " + str(currencyNames[i])
                out.append((actualratio, s))
    
# Cycles of length 3
for i in range(1, rangeend):
    for j in range(1, i):
        for k in range(1, j):
            if i != j and j != k and k != i:
                actualratio = (matrix[i][j] * matrix[j][k] * matrix[k][i])
                if  actualratio > desiredratio:
                    s = "Cycle of length 3 R: " + str(actualratio) + " detected from " + str(currencyNames[i]) + " to " + str(currencyNames[j]) + " to " + str(currencyNames[k]) + " to " + str(currencyNames[i])
                    out.append((actualratio, s))

# Cycles of length 4
for i in range(1, rangeend):
    for j in range(1, i):
        for k in range(1, j):
            for w in range(1, k):
                if i != j and j != k and k != i and w != j and w != k and w != i:
                    actualratio = (matrix[i][j] * matrix[j][k] * matrix[k][w] * matrix[w][i])
                    if  actualratio > desiredratio:
                        s = "Cycle of length 4 R: " + str(actualratio) + " detected from " + str(currencyNames[i]) + " to " + str(currencyNames[j]) + " to " + str(currencyNames[k]) + " to " + str(currencyNames[w]) + " to " + str(currencyNames[i])
                        out.append((actualratio, s))


sorted(out, key=imemgetter(0), reverse=True)
# Print all the cycles
print(out)
