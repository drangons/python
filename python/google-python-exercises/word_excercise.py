"""excersice2 from the http://www.greenteapress.com/thinkpython/html/thinkpython014.html """

import sys
import codecs
import string

verbose = 0
def build_histogram(filename):
  
  #f=codecs.open(filename,'rU','utf-8')
  f=open(filename,'rU')
  i=0
  skip_header= 1
  histogram={}
  for lines in f:
    #print lines
    # below two if loops skips over header part
    # real text begins after the *** START OF ....*** 
    if '***' in lines:
      skip_header=0
      continue
    if skip_header :
      continue
    # tranform the line
    line=lines.translate(None,string.punctuation).lower().split() 
    
    if not len(line): #skip over empty lines
      continue
    if verbose:
      print line
    
    for item in line:
      if item not in histogram:
        histogram[item]=1
      else:
        histogram[item]+=1
        
  return histogram  
  
def reverse_lookup(d,value):
  for key in d :
    if d[key] == value :
      return key

histogram=build_histogram('pg42492.txt')
"""for alphabet,frequency in histogram.items():
  print alphabet,'===>', frequency """
print 'no of words in text is ', sum(histogram.values())
print 'word with max occurance ', reverse_lookup(histogram,max(histogram.values())), " with frequency " , max(histogram.values())

print histogram['the']

key=sorted(histogram.values(),reverse=True)

#print key
#print key

for itr in range(20):
  print key[itr]
  print reverse_lookup(histogram,key[itr]) , " ==> ", key[itr]