from selenium import webdriver
import time

matrix = [[0]*10 for i in range(10)]


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
		buyamt = data[3]
		selltype = int(data[4])
		sellamt = data[5]
		user = data[6]
		if matrix[buytype][selltype] == 0:
			matrix[buytype][selltype] = float(float(sellamt)/float(buyamt))


for i in range(1, 9):
	print matrix[i][1:9]

