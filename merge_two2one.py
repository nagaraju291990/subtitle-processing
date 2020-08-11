
#input a subtitle file 
#it will combine two lines of a subtitle into single line

import sys
import re
import pysrt 

with open(sys.argv[1]) as f:
	lines = f.readlines()

subs = pysrt.open(sys.argv[1])

index = 1
for sub in subs:
	start_time = sub.start
	end_time = sub.end

	cur_text = sub.text
	cur_text = re.sub(r'\n', ' ', cur_text)

	print(index)
	print(start_time,"-->",end_time,sep=' ')
	print(cur_text,"\n")
	index = index + 1


