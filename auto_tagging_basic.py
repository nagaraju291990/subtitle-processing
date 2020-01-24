#detecting repeititions/hesitattions/ and other tags specified in gudidelines

import sys
import re

with open(sys.argv[1]) as fp:
	lines = fp.read().split("\n")


for line in lines:
	#if(re.search(r'(cough|sneeze|laugh|)', line, flags=re.MULTILINE, flags=re.)):

	#Anthrophoneics
	#line = re.sub(r'(\bcough\b|\bsneeze\b|\blaugh\b)', r'<O>\1</O>', line, flags=re.MULTILINE|re.IGNORECASE)

	#Abbrevations
	#line = re.sub(r'([A-Z](\-)?[A-Z]+(\-)?[A-Z]+)', r'<AB>\1</AB>', line, flags=re.MULTILINE)

	#hesistations
	#line = re.sub(r'(\bAhh\b|\buhh\b|\buh\b|\ber\b)', r'<HES>\1</HES>', line, flags=re.MULTILINE|re.IGNORECASE)

	#pet phrases or filler words
	#line = re.sub(r'(\bokay\b|\bok\b|\bright\b|\bso\b)', r'<PET>\1</PET>', line, flags=re.MULTILINE|re.IGNORECASE)


	#lp -- longpause annotation 
	if(not re.search(r'-->', line)):
		line = re.sub(r'(,|\.)', r'\1 <lp> ', line, flags = re.MULTILINE)

	##spaces normalization
	line = re.sub(r'^ *', "", line, flags = re.MULTILINE)
	line = re.sub(r' *$', "", line, flags = re.MULTILINE)
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)

	print(line)