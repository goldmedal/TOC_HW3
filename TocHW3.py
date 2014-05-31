#!/usr/bin/python
# -*- coding=utf-8 -*-

import urllib2
import json
import sys

url = sys.argv[1]
targetCityArea = unicode(sys.argv[2], "utf-8")
targetRoadName = sys.argv[3]
targetYear = int(sys.argv[4])
response = urllib2.urlopen(url)
data = response.read()
jload = json.loads(data)

cityArea = unicode("鄉鎮市區", "utf-8")
roadName = unicode("土地區段位置或建物區門牌", "utf-8")
year = unicode("交易年月", "utf-8")
price = unicode("總價元", "utf-8")

countMatch = 0
sumOfMatch = 0
errorCount = 0
index = 0
end = len(jload)

for column in jload:
	try:
		if not cmp(column[cityArea], targetCityArea):

			road = str(column[roadName].encode("utf-8"))
			if road.find(targetRoadName) != -1:

				_year = column[year]/100
				if _year >= targetYear and _year < 104:

					countMatch = countMatch + 1
					sumOfMatch = sumOfMatch + column[price]
	#				print json.dumps(column, ensure_ascii=False)

	except:
		errorCount += 1

print sumOfMatch/countMatch
#print "Have %d Error in data" %(errorCount)

