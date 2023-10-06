# media-anlyse
### Install

# Do not install manually unless you are debugging or contributing!

## Recommeded Install 
''' bash
docker build -t media-analyse .
docker run -it -v /path/to/images:/media media-analyse
'''

## Debug install

Make sure all dependancies are installed 
``` bash
pip install opencv-python numpy tqdm threading subprocess inquirer pillow shutil
```

### To run program 
``` bash
python main.py
```
