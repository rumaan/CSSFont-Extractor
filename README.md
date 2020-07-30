# CSS Font Extractor
_Extract_ fonts (`.woff`) encoded into base64 format from _CSS_ files.

**`make_woff.sh`** - It gets one ore more CSS files as arguments, then calls `extract_font.py` to extract the _base64_ strings as `.txt` files in _**/output**_ directory then converts them into `.woff` font files.

**`extract_font.py`** - Extracts _base64_ lines from CSS files and saves them into individual `.txt` files inside _**/output**_ directory. It tries to retrieve font name, weight and style from the CSS file and use this info for the file names generated in the format _[NAME\_WEIGHT\_STYLE\_]NUMBER.woff_.

### Optional
Use [Woff2Otf](https://github.com/hanikesn/woff2otf) tool by [hanikesn](https://github.com/hanikesn/) to convert `.woff` files to `.otf` (the file is downloaded from GitHub on demand using `curl`, coverting to OTF is skipped if file is missing).

### Requirements
bash & Python 3: It should run without problems on Linux or macOS, please report any issues.

### How to run
Clone or download this git, then:

```bash
bash make_woff.sh FILE1.CSS [FILE2.CSS...]
```

<br></br>
*TO-DOs* are mentioned in the individual files. PR's and issues are welcome!😊 . 
<br></br>
_**Note**: All this can be done easily using Chrome Dev Tools from Network Tab and saving base64 files into binary files as mentioned [here](https://stackoverflow.com/a/31854648/9540400)._
😉😉
