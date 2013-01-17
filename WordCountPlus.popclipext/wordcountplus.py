#!/usr/bin/env python
# -*- coding: utf-8 -*-
# script based on http://markmail.org/message/iaztipcld4hvk4q7#query:+page:1+mid:tn2q7nenk5pmyiks+state:results
import re
import os
data = os.environ['POPCLIP_TEXT']
encoding = "utf-8"
data = data.decode(encoding)
def main():
	cjkReg = re.compile(u'[\u1100-\uFFFD]+?')
	trimedCJK = cjkReg.sub( ' a ', data, 0)
	wordCount = len(trimedCJK.split())
	charCount = len(''.join(trimedCJK.split()))
	if wordCount > 1:
		wordCount = str(wordCount) + ' words'
	else:
		wordCount = str(wordCount) + ' word'
	if charCount > 1:
		charCount = str(charCount) + ' characters'
	else:
		charCount = str(charCount) + ' character'
	print wordCount + ', ' + charCount
main()