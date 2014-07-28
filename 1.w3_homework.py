#-*- coding: utf-8 -*-
# sbs 뉴스 속보 xml문서 파싱하기
from bs4 import BeautifulSoup
from xml.etree.ElementTree import parse
import urllib
import webbrowser

xml = urllib.urlopen('http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=external')	# 속보
tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
root = tree.getroot()	# root태그 얻어오기

i = 0
for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):	# item 태그를 모두 반복
		i += 1
		print i,
		# 뉴스 제목 보기
		print child.find("title").text
#		print child.findtext("title")


print 
num = raw_input("뉴스번호를 입력하세요 : ")
num = int(num)

i = 0
for parent in root.getiterator():
	for child in parent.findall("item"):
		i += 1
		if i == num:
			print child.findtext("title")
			url = child.findtext("link")
			print url
			webbrowser.open(url)
			break

		# 뉴스 내용 보기
#		print child.findtext("description")ef get_html(num):