import sys
import Textstat

if (len(sys.argv))>1: #to input file name as argument/ it is by default with length of 1
    ls,cs,ws,ss= Textstat.stats_from_filename(sys.argv[1])
    print(f'{ls} lines, {cs} characters, {ws} words, {ss} sentences')
    
#type -> python Textstatsmain.py gregor.txt  in CMD