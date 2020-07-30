#!/bin/bash
# Creates .WOFF format font from base64 .txt files
# FIXME: Font weights, name and other details aren't extracted.

OUTPUTDIR="output"
GITURL="https://github.com/hanikesn/woff2otf/blob/master"
EXTRACTFONT="extract_font.py"
WOFF2OTF="woff2otf.py"

download() {
	printf "Downloading WOFF to OTF converter from GitHub…"
	curl -sLS "$GITURL/$WOFF2OTF?raw=true" --output "$OUTPUTDIR/$WOFF2OTF"
}

[ "$1" == "" ] && printf "Please provide at least one file as an argument.\n" && exit 1

convert=0 && [ ! -d $OUTPUTDIR ] && mkdir $OUTPUTDIR

[ ! -r "$OUTPUTDIR/$WOFF2OTF" ] && download
[ -r "$OUTPUTDIR/$WOFF2OTF" ] && convert=1 || printf "$WOFF2OTF not found, WOFF will not be converted to OTF.\n" 

for inputfile in "${@}"
do
	printf "Extracting from file: ${inputfile}\n"

	if [ -r "$inputfile" ]
	then
		python3 $EXTRACTFONT "$inputfile"
		cd $OUTPUTDIR
		for filename in `ls *.txt 2>/dev/null`
		do
			if [ -r "$filename" ]
			then 
				# Convert the base64 text into WOFF format
				file="${filename%.*}"
				printf "Converting $filename to ${file}.woff\n"
				base64 --decode "$filename" > "${file}.woff"
				
				# OPTIONAL
				# Convert the WOFF font to OTF using woff2Otf tool
				[ $convert == "1" ] && python3 $WOFF2OTF "${file}.woff" "${file}.otf"
			fi
		done
		[ -r "${filename}" ] && rm *.txt && cd ..

	else
		printf "Cannot access: ${inputfile}\n"
	fi

done
