#!/usr/bin/env python3
import re, sys

OUTPUTDIR = "output"
base64array = []    # font
fontname = []       # font name
fontweight = []     # font weight
fontstyle = []      # font stule
fonts = []
fontfile = []
numf = 0

if len(sys.argv) < 2:
    print ("This program needs at least one argument")
    exit()

filename = str(sys.argv[1])
try: 
    file = open(filename, "r")

except IOError:
    print ("Error opening file: " + filename)
    exit()
 
regexa = re.compile(r"url\(data:application\/font-woff;charset=utf-8;base64,[\w+/=]+\)")
regexn = re.compile(r"font-family\:[\w\s]+\;")
regexw = re.compile(r"font-weight\:[\w\s]+\;")
regexs = re.compile(r"font-style\:[\w\s]+\;")

for line in file:
    base64array += regexa.findall(line)
    fontname += regexn.findall(line)
    fontweight += regexw.findall(line)
    fontstyle += regexs.findall(line)

while numf < len(base64array):
    x = base64array[numf]
    if x == []:
        continue
    x = str(x)
    #startIndex = x.rfind(',')
    #endIndex = x.rfind(')')
    filestring = ""
    tempstring = ""
    
    if numf < len(fontname) and fontname[numf] != []:
        string = str(fontname[numf])
        filestring += string[12:len(string)-1] + "_"
        
    if numf < len(fontweight) and fontweight[numf] != []:
        string = str(fontweight[numf])
        filestring += string[12:len(string)-1] + "_"
        
    if numf < len(fontstyle) and fontstyle[numf] != []:
        string = str(fontstyle[numf])
        filestring += string[11:len(string)-1] + "_"
    
    print("{:02d} - Found font: {}".format(numf+1, filestring.replace("_", " ")))
    #print("Start1: {} - End: {}".format(startIndex, endIndex))
    #print("Start2: {} - End: {}".format(51, len(x)-1))
    #fonts.append(x[startIndex+1:endIndex])
    fonts.append(x[52:len(x)-1])
    fontfile.append(filestring + str(numf+1).zfill(2) + ".txt")
    numf += 1

# Write each base64 found into a seperate file
for i, l in enumerate(fonts):
    # Move the individual files to corresponding files
    outfile = open("./{}/{}".format(OUTPUTDIR, fontfile[i]), "w")
    outfile.write(l)
    outfile.close()

file.close()

if numf == 0:
    print ("No font found in " + filename)
else:
    print (str(numf) + " font(s) found in " + filename)

