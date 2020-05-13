import pysrt
import re
import sys

subs = pysrt.open(sys.argv[1])

index = 1
for sub in subs:
	#print(sub)
	cur_text = sub.text
	cur_text = re.sub(r'(.*\|.*\|.*)?', '', cur_text)
	if(re.search(r'[A-z]', cur_text)):
		print("Subtitle no: ", index, " contains english text")
	index = index + 1