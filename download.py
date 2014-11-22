import urllib2

def download(url):
	try:
		response = urllib2.urlopen(url)
		f = open('file{0}.xls'.format(i), 'w+')
		f.write(response.read())
		print url + " OK"
	except:
		print url + " Not Found."
		
for i in range(0,10):
    url = "http://www.ine.es/daco/daco42/codmun/codmun14/14codmun0{0}.xls".format(i)
    download(url)
for i in range(10,53):
    url = "http://www.ine.es/daco/daco42/codmun/codmun14/14codmun{0}.xls".format(i)
    download(url)

