#!/usr/bin/env python3
import re, sys

OUTPUTDIR = "output"    # output dir
base64array = []        # array containing fonts in base64 format
fontname = []           # font name
fontweight = []         # font weight
fontstyle = []          # font stule
fonts = []              # fonts
fontfile = []           # fonts file names
numf = 0                # number of fonts (counter)

# Check for errors
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

# Extract the arrays per line
for line in file:
    base64array += regexa.findall(line)
    fontname += regexn.findall(line)
    fontweight += regexw.findall(line)
    fontstyle += regexs.findall(line)

# Extract useful data
while numf < len(base64array):
    x = base64array[numf]
    if x == []:
        continue

    x = str(x)
    filestring = ""
    tmpstring = ""
    
    if numf < len(fontname) and fontname[numf] != []:
        tmpstring = str(fontname[numf])
        filestring += tmpstring[12:len(tmpstring)-1] + "_"
        
    if numf < len(fontweight) and fontweight[numf] != []:
        tmpstring = str(fontweight[numf])
        filestring += tmpstring[12:len(tmpstring)-1] + "_"
        
    if numf < len(fontstyle) and fontstyle[numf] != []:
        tmpstring = str(fontstyle[numf])
        filestring += tmpstring[11:len(tmpstring)-1] + "_"
    
    print("{:02d} - Font found: {}".format(numf+1, filestring.replace("_", " ")))
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

