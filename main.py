from FGO_5th_anniv_webrip_extractor import FGO_5th_anniv_wallpaper_webrip
from FGO_5th_anniv_ads_extractor import FGO_5th_anniversary_ads

if __name__ == "__main__":
    
    wall_input = input("Which artwork do you want to download ? \n 1. Wallpapers extracted from the website \n 2. The artworks with ads \n 3. Both \n\n Choose one : ")

    if wall_input == '1' : 
        FGO_5th_anniv_wallpaper_webrip()

    elif wall_input == '2' : 
        FGO_5th_anniversary_ads()

    elif wall_input == '3' : 
        FGO_5th_anniv_wallpaper_webrip() 
        FGO_5th_anniversary_ads()
    else :
        print('Wrong input')

    