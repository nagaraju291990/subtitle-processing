#This script converts srt file into text format like text.....[SUB____1]....text [SUB____2]
#and also generates a timeline file required later for processing
from argparse import ArgumentParser
import re
import os
import sys
import pysrt

parser = ArgumentParser(description='Extract text from srt file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=file.srt " + "-p=[ab|lp|both]"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .srt file name",required=True)
parser.add_argument("-p", "--placeholder", dest="placeholder",
                    help="yes or no",required=False)
args = parser.parse_args()

inputfile = args.inputfile
placeholder = args.placeholder
if(placeholder == None):
	placeholder = 'no'
else:
	placeholder = placeholder.lower()

new_line = []
timeline = []
timeline_hash = {}

outfp = open(inputfile + "_timeline.txt","w")


def extractText(i):

	srtfilename = i
	subs = pysrt.open(srtfilename)
	ts_start = []
	ts_end = []
	remaining_text = ''
	front_text = ''
	#print(subs)
	count = 1
	for sub in subs:
		timeline_start = str(sub.start)
		timeline_end = str(sub.end)
		cur_text = sub.text
		cur_text = re.sub(r'\n', ' ' ,cur_text)
		#sub_placeholder = "[SUB____" + str(count) + "]"
		sub_placeholder = " ";#z\n"
		#print(sub_placeholder)
		outfp.write(str(sub.start) + " --> " + str(sub.end) +"\n")
		#timeline_hash[sub_placeholder] = str(sub.start) + " --> " + str(sub.end)
		#new_line.append("[" + str(sub.start) + " --> " + str(sub.end) + "]")
		new_line.append(sub_placeholder)
		new_line[-1] = new_line[-1].strip() + cur_text
		count = count + 1

		#print(subs.text)
	#print("Subtitle processed Successfully!")



extractText(inputfile)
#print(timeline_hash)
#exit(0)

count = 1
for line in new_line:
	#print(count)
	line = re.sub(r']', '] ',line)
	#line = re.sub(r'\.', '.\n' ,line)
	#line = line.strip()
	if(placeholder == "yes"):
		print(line)
	else:
		print(line, end='')
	#print(line)
	count = count + 1
