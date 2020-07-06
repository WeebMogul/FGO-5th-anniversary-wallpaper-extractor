import os
import requests
from urllib.request import Request
from tqdm import tqdm
from cv2 import cv2
import shutil
from bs4 import BeautifulSoup
import json
import re

'''
1. Create directory.
2. Put all the numbers in an array or list.
3. Attach no. to existing link.
4. Extract the link using the number 
5. Place in directory 
6. Convert to 1920 x 1080 resolution using ffmpeg
'''

def resolution_convert(path, arr):
    # path = os.chdir(r'D:\Python\Python Projects\FGO-5th-anniversary-wallpaper-extractor')

    for i in tqdm(range(len(arr))):

        file_no = arr[i]
        img_name = os.path.join(path,file_no)
        img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)
        
        
        new = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_AREA)
        new_file = arr[i]
        folder_path = os.path.join(path, new_file)
        cv2.imwrite(folder_path, new)
        

full_fnames = []

# For extracting the images 

url = 'https://5th.fate-go.jp/'

htm = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(htm.content,'lxml')

scri = soup.find_all('script')[6].string
json_format = re.sub(r'window.archiveData = |;','',scri)
json_serv = json.loads(json_format)

for i in json_serv:
    fullname = i['id'] + '_' + i['hash'] + '.jpg'
    full_fnames.append(fullname)

pic_link = 'https://5th.fate-go.jp/assets/img/archive/ph/fullsize/'

cwd = os.getcwd()
folder_name = 'FGO_5th_anniversary_full_artwork'
output = os.path.join(cwd,folder_name)

os.mkdir(output)

for file_name in tqdm(full_fnames):
    img_url = pic_link + file_name
    imgs = requests.get(img_url)

    output_file = os.path.join(output,file_name)

    try:
        open(output_file,'wb').write(imgs.content)
    except FileNotFoundError:
        print("Error : File does not exist")
    except OSError:
        print("Error : Something went wrong with the file writing")

# resolution_convert(output,full_fnames)



