# this scirpt will join srt text into previous line if it has only two words

from argparse import ArgumentParser
import re
import os
import sys
import pysrt


parser = ArgumentParser(description='Join two words line into previous line in a srt file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=file.srt "
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .srt file name",required=True)


args = parser.parse_args()

srtfilename = args.inputfile


subs = pysrt.open(srtfilename)

for sub in subs:
	cur_text = sub.text
	i = 1
	for line in cur_text.split("\n"):
		if(i == 2 and len(re.findall(" ", line)) <= 1):
			sub.text = cur_text.split("\n")[0] + " " + line
		#print(line)
		i = i + 1
	print(sub)