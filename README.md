# CSS Font Extractor
_Extract_ fonts (`.woff`) encoded into base64 format from _css_ files.

`extract_font.py` - Extracts _base64_ lines from CSS files and saves them into individual `.txt` files inside _**/encoded**_ directory.

`make_woff.sh` - Converts all the _base64_ files in _**/encoded**_ directory into `.woff` font files.

####Optional
Use [Woff2Otf](https://github.com/hanikesn/woff2otf) tool by [hanikesn](https://github.com/hanikesn/) to convert `.woff` files to `.otf`

###### Make Sure Both the files are in parent directory.
<br></br>
*TO-DOs* are mentioned in the individual files. PR's and issues are welcome!😊 . 
<br></br>
_**Note**: All this can be done easily using Chrome Dev Tools from Network Tab and saving base64 files into binary files as mentioned [here](https://stackoverflow.com/a/31854648/9540400)._
😉😉