#!/usr/bin/python

# membaca rss dari situs berita CNN.com
# import urllib
import xml.etree.ElementTree as ET
import urllib.request
from time import gmtime, strftime
from datetime import datetime, timedelta


with urllib.request.urlopen("http://rss.cnn.com/rss/edition.rss") as url:
    s = url.read()
# print(s)

# tree = ET.parse('cnn.xml')
# root = tree.getroot()
# root.tag

root = ET.fromstring(s)
for channel in root.findall('channel'):
	for item in channel.findall('item'):
		lastday = datetime.today() - timedelta(hours = 24)
		date = item.find('pubDate').text
		
		nowHour = int(strftime("%H"))
		nowMinute = int(strftime("%M"))
		nowDay = int(strftime("%d"))
		
		itDay = int(date[5:7])
		itHour = int(date[17:19])
		itMinute = int(date[20:22])
		
		# print(date + ">>"+itDay+":"+itHour+":"+itMinute)
		title = item.find('title').text
		desc = item.find('description').text
		
		if (itDay == nowDay):
			print(date+ "\n" +title + "\n" + desc)
		elif (itDay+1 == nowDay):
			if(itHour > nowHour):
				print(date+ "\n" +title + "\n" + desc)
			elif(itHour == nowHour):
				if(itMinute > itHour):
					print(date+ "\n" +title + "\n" + desc)
		
		# dateO = time.strftime("%a, %d %b %Y %H:%M:%S %z", date);
		
		# if (dateO > lastday):
			# print(date + " " + title)

# f = open("cnn.rss","r")
# contents = f.read()
# f.close()

# for row in contents:
        # print(row)
        
