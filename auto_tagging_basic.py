#detecting repeititions/hesitattions/ and other tags specified in gudidelines

import sys
import re
from argparse import ArgumentParser

parser = ArgumentParser(description='This script will tag <lp> and <fw> in a srt file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + " -t=ab|fw|both"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-t", "--tags", dest="tag",
					help="specify what are the tags to be marked", required=False)
parser.add_argument("-f", "--fwfile", dest="fwfile",
					help="specify foreign word file name; Required if tag option is having fw/both values", required=False)

args = parser.parse_args()

inputfile = args.inputfile
tag = args.tag

if(tag == None):
	tag = 'ab'
else:
	tag = tag.lower()

with open(inputfile) as fp:
	lines = fp.read().split("\n")

if(tag == "both" or tag == "fw"):
	try:
		fwfile = args.fwfile
	except:
		print("Foregin word file not specifed, for ex: use -f=fw.txt")
		exit()
	#fwfile = args.fwfile

	with open(fwfile) as fp:
		fwlines = fp.readlines()#.split("\n")

	#save as regex
	fw_dict = "(\\b" + "\\b|".join(fwlines)  + ")"
	fw_dict = re.sub(r'\n', "", fw_dict)
	fw_dict += "\\b"
	#print(fw_dict)
	#exit()
for line in lines:
	#if(re.search(r'(cough|sneeze|laugh|)', line, flags=re.MULTILINE, flags=re.)):

	#Anthrophoneics
	#line = re.sub(r'(\bcough\b|\bsneeze\b|\blaugh\b)', r'<O>\1</O>', line, flags=re.MULTILINE|re.IGNORECASE)

	#Abbrevations
	if( (tag == "both" or tag =="ab") and (not re.search(r'-->', line))  and (not re.search(r'HES|PET|MUSIC', line))) :
		line = re.sub(r'([A-Z]([\-\.])?[A-Z]+([\-\.])?([A-Z]+)?)', r'<AB>\1</AB>', line, flags=re.MULTILINE)

	#hesistations
	#line = re.sub(r'(\bAhh\b|\buhh\b|\buh\b|\ber\b)', r'<HES>\1</HES>', line, flags=re.MULTILINE|re.IGNORECASE)

	#pet phrases or filler words
	#line = re.sub(r'(\bokay\b|\bok\b|\bright\b|\bso\b)', r'<PET>\1</PET>', line, flags=re.MULTILINE|re.IGNORECASE)


	#lp -- longpause annotation
	#if( (tag == "both" or tag =="lp") and (not re.search(r'-->', line)) ):
	#	line = re.sub(r'(,|\.|:|;|\'|\?)', r'\1 <lp> ', line, flags = re.MULTILINE)

	#fw marking
	if( (tag == "both" or tag == "fw") and (not re.search(r'-->', line)) ):
		line = re.sub(r'' + fw_dict , r'<FW>\1</FW>', line, flags=re.MULTILINE|re.IGNORECASE)

	##spaces normalization
	line = re.sub(r'^ *', "", line, flags = re.MULTILINE)
	line = re.sub(r' *$', "", line, flags = re.MULTILINE)
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)

	print(line)
