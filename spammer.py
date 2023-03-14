# -*- coding: utf-8 -*-
import os
try:
  import requests
except:
  os.system('pip install requests')
def find_input(URL_INPUT):
	html = requests.get(URL_INPUT)
	#gets html from the website
	inputs = ''
	for line in html:
		if 'input' in line:
			inputs + line, "\n"
	#puts each line with an input in a file
	thefile = open('w', 'inputs.txt')
	thefile.write(inputs)
	thefile.close()
#remove the hashtag from the start of the next line and put the url in the ''
#find_input('')
#this on is formatted like json if that helps
yourinputs = {
#formatted like this
#	"inputone":  'hi hello',
#	"inputwo": 'hows your day going'
}
#I name shit in python weird, you can rename it but you have to rename it everywhere
def putinthedata(URL_INPUT):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3)                 AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}
	r = requests.post(URL_INPUT, data = yourinputs, headers = headers)
	print('Cookie says: \n', r.cookies.get_dict())
	print('Response code:',r)
	print(r.text)
#remove the hashtag and put url in'' 
#putinthedata('')
