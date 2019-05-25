## Step1:


    python3 srt-text2.py -i=input.srt > sub_text.txt

### This script will extract text from srt file with timelines being replaced into placeholders as [SUB____1000]
### Also there will be a timeline file generated from srt file that will be used in the later stage.

### Dependency:
    pip3 install pysrt

## Step2:

    python3 sent_tokenize.py sub_text.txt > sub_text_sentence.txt

This step will convert the file from previous stage into sentences.

### Dependency:
    pip3 install nltk

## Step3:

    python3 generate-srt.py -i=sub_text_sentence_translated.txt -t=/path/to/timeline/file/from/step1 

This script will generate subtitles as in original srt file named 'outfile.srt' with each substitle consisting exactly one line of text.


## Step4:

    python3 break_half.py outfile.srt 

This script will break each subtitle into two lines.
