#!/usr/bin/env python

import requests
import re

class Parser:

	def __init__(self):
		pass

	def fetch(self):
		r = requests.get('https://www.google.com/design/spec/style/color.html')
		pname = re.compile(".*<span class=\"name.*\">(.*)</span>.*")
		pshade = re.compile(".*<span class=\"shade[ a-z]*\">([0-9 a-zA-Z]+)</span>.*")
		pcolor = re.compile(".*<span class=\"hex\">#([0-9a-zA-Z]+)</span>.*")
		name = None
		for line in r.text.split("\n"):
			m = pname.match(line)
			if m is not None:
				name = m.group(1)

			m = pshade.match(line)
			if m is not None:
				shade = m.group(1)

			m = pcolor.match(line)
			if m is not None:
				color = m.group(1)
				print "%s,%s,%s"%(name, shade, color)




parser = Parser()
parser.fetch()		