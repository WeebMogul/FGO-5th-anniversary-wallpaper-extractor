import os
import requests
from tqdm import tqdm

# For extracting the images 
def image_extractor(url, img_names, folder_dir):
    """Used for extracting the images from the website.

    Args:
        url (list): The list of all the image URLs.
        img_names (list): The list of all the name of the images.
        folder_dir (str) : Path of the download folder

    Returns:
        Wallpapers (.jpg): All of the wallpapers in the .jpg format 

    """
    for i in tqdm(range(len(img_names))):

        file_no = 's' + img_names[i] + '.jpg'
        output = os.path.join(folder_dir, file_no)
        img_url = url.replace('s01.jpg', file_no)
        imgs = requests.get(img_url)

        try:
            open(output,'wb').write(imgs.content)
        except FileNotFoundError:
            print("Error : File does not exist")
        except OSError:
            print("Error : Something went wrong with the file writing")

def get_dem_wallpapers(fold_name,folder,img,wall_no):
    """For creation of the wallpaper directory based on each month and saving it in each folder.

    Args:
        fold_name (str): Name of the subfolder.
        folder (str): Name of the parent folder.
        img (str): Link to the image from the FGO 5th anniv. website
        wall_no (int): Number of wallpapers to download
    """
        
    folder_name = fold_name
    new_folder_path = os.path.join(folder,folder_name)
    os.mkdir(new_folder_path)

    wall_names = [str(i).zfill(2) for i in range(1,wall_no)]
    image_extractor(img, wall_names, new_folder_path)

img_links = ['https://5th.fate-go.jp/assets/img/slide_0504_jzgkaw3b/s01.jpg','https://5th.fate-go.jp/assets/img/slide_0525_r6dwy7nt/s01.jpg','https://5th.fate-go.jp/assets/img/slide_0603_d486tjek/s01.jpg']
wall_no = [12,7,9]
fold_name = ['April Collection','May Collection','June Collection']

parent_dir = os.getcwd()
main_folder_name = "FGO 5th anniversary wallpapers"
folder = os.path.join(parent_dir, main_folder_name)

months = 3

if not os.path.exists(folder):

    os.mkdir(folder)

    for i in range(0,months):

       get_dem_wallpapers(fold_name[i],folder,img_links[i],wall_no[i])
       print(f"\n Downloaded the {fold_name[i]} wallpapers \n")

else :

    for i in range(0,months):
        
        if os.path.exists(os.path.join(folder,fold_name[i])):
            print(f'The {fold_name[i]} exists')
        else :
            get_dem_wallpapers(fold_name[i],folder,img_links[i],wall_no[i])
            print(f"\n Downloaded the {fold_name[i]} wallpapers \n")

