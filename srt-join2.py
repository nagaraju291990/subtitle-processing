# this scirpt will join two subtitle blocks

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

count = 1
out_subs = []
flag = 0
for i in range(0, len(subs)):
	if(flag == 1):
		flag = 0
		continue
	flag = 0
	#print(i,len(subs))
	#if(i == len(subs) -1 and i%2 == 0):
	#	subs[i].index = count
	#	out_subs.append(subs[i])
	#	continue
	#if(i%2 != 0):
	#	continue

	cur_sub = subs[i]
	try:
		next_sub = subs[i+1]
	except:
		#print(cur_sub.text)
		next_sub = cur_sub#'Hello just something here to skip' 

	#for line in next_sub.text:
	if(len(re.findall(" ", next_sub.text)) <= 1):
		flag = 1
		out_start_time = cur_sub.start
		out_end_time = next_sub.end
		out_text = cur_sub.text + " " + next_sub.text + "\n"

		out_subs.append(count)
		out_subs.append(str(out_start_time) + ' --> ' + str(out_end_time))
		out_subs.append(out_text)
		#count = count + 1
	else:
		out_start_time = cur_sub.start
		out_end_time = cur_sub.end
		out_text = cur_sub.text + "\n"

		out_subs.append(count)
		out_subs.append(str(out_start_time) + ' --> ' + str(out_end_time))
		out_subs.append(out_text)

	count = count + 1
	#print(i)
	#i = i + 2

for o in out_subs:
	print(o)