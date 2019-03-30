import sys, webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#modify this to point to the text file with the json text
#make sure .txt file is a copy/paste of json from nasa order
file = open("C:\\Users\\twburton\\Desktop\\modisscript\\file.txt",'r').read()


def downloadfiles(s):
	for i in xrange(len(s)):
		strlen=8
		if s[i:i+strlen] == '"name":"':
			j2=strlen
			for j in xrange(1000):
				if s[i+strlen+j]=='"':
					j2=j
					break
			filename =s[i+strlen:i+strlen+j2]
			if(filename!="name"):
				#make sure this is correct url of order location
				url= "https://ladsweb.modaps.eosdis.nasa.gov/archive/orders/insertordernumhere/"+ filename
				webbrowser.get(chrome_path).open(url) 
		
downloadfiles(file)
