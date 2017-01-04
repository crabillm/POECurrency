from selenium import webdriver
import time

rangeend = 9
matrix = [[0]*(rangeend + 1) for i in range(rangeend + 1)]


desiredratio = 1.2




br = webdriver.PhantomJS('phantomjs')
br.get('http://currency.poe.trade/search?league=Breach&online=x&want=1-2-3-4-5-6-7-8&have=1-2-3-4-5-6-7-8')

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


for i in range(1, rangeend):
	print matrix[i][1:rangeend]

# Cycles of length 2
for i in range(1, rangeend):
    for j in range(1, i):
        if i != j:
            if (matrix[i][j] * matrix[j][i]) > desiredratio:
                print "Cycle of length 2 detected from " + str(i) + " to " + str(j) + " to " + str(i)
    
# Cycles of length 3
for i in range(1, rangeend):
    for j in range(1, i):
        for k in range(1, j):
            if i != j and j != k and k != i:
                if (matrix[i][j] * matrix[j][k] * matrix[k][i]) > desiredratio:
                    print "Cycle of length 3 detected from " + str(i) + " to " + str(j) + " to " + str(k) + " to " + str(i)

