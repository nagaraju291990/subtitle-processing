## Script1:

To extract text from srt file.

```bash
python3 srt-text2.py -i=input.srt > sub_text.txt
```
<span style="color:blue">This script will extract text from srt file with timelines being replaced into placeholders as [SUB____1000] or newline.
Also there will be a timeline file generated from srt file that will be used in the later stage.</span>

### Dependency:

```bash
pip3 install pysrt
```

## Script2:

To make sentence wise tokenisation
```bash
    python3 sent_tokenize.py sub_text.txt > sub_text_sentence.txt
```

This step will convert the file from previous stage into sentences.

### Dependency:
    pip3 install nltk

## Script3:

To generate timeline from translated text file and timeline file

```bash
python3 generate-srt.py -i=sub_text_sentence_translated.txt -t=/path/to/timeline/file/from/step1 
```

This script will generate subtitles as in original srt file named 'outfile.srt' with each subtitle consisting exactly one line of text.


## Script4:

    python3 break_half.py outfile.srt 

This script will break each subtitle into two lines.


## Script5:

```bash
python3 remove_rich_text.py -i input.srt 
```

This script wiil remove rich text from subtitle(srt)/transcription file.

## Script6:

```bash
python3 auto_tagging_basic.py -i=inputfile(.txt|.srt) -t=[ab|lp|both] 
```
In the tag option use any one of the tag ab or lp or both without square brackets.


This script will add annotaitons of &lt;lp&gt; and &lt;AB&gt; based on heuristics.
