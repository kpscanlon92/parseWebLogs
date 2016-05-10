#!/usr/bin/python

import re
import sys, getopt
from collections import OrderedDict

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'usage: parseWebLog.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: parseWebLog.py -i <inputfile>'
            sys.exit(1)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    if inputfile == '':
        print 'usage: parseWebLog.py -i <inputfile>'
        sys.exit(2)
        
    ipDict = OrderedDict()
    with open(inputfile, 'r') as inf:
        for line in inf:
            # regex break down: an ip address at the beginning and 200 followed by either a 
            # number or a dash at the end
            # (\d{1,3}\.) - a number that has between 1 and 3 digits followed by a .
            # ^(\d{1,3}\.){3} - at the beginning three groups of numbers.
            # \d{1,3}\s - the last number followed by a space instead of a .
            # .* - anything inbetween the ip address and 200
            # \s200\s - 200 surrounded by spaces
            # (\d+|-)$ - at the end any greedy number or a dash
            m = re.match( r'^(\d{1,3}\.){3}\d{1,3}\s.*\s200\s(\d+|-)$', line)
            if m:
                ip = line.split(' ')[0]
                ipDict[ip] = ipDict.get(ip, 0) + 1
    
        for ip in ipDict:
            print ip,"    ",ipDict[ip] 
        
    inf.close()

if __name__ == "__main__":
    main(sys.argv[1:])
