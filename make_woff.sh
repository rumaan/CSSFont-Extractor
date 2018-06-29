# Creates .WOFF format font from base64 .txt files
# FIXME: Font weights, name and other details aren't extracted.
cd ./encoded
for filename in `ls`
do
    # Convert the base64 text into WOFF format
    echo "Converting $filename to ${filename:0:2}woff"
    base64 -D $filename > "${filename:0:2}woff"
    # Convert the WOFF font to OTF using woff2Otf tool
    chmod u+x woff2otf.py
    ./woff2otf.py ${filename:0:2}woff ${filename:0:2}otf
done