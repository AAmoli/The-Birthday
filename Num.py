import numpy as np
from PIL import Image
import os
import datetime
import pandas as pd


os.chdir(r"C:\Users\AmirA\Desktop\Programming\Phyton-Skript\Pixel_Fotos\Date")

white = [255,255,255]
df = pd.read_csv("dates.csv", index_col = 0)

os.chdir(r"C:\Users\AmirA\Desktop\Programming\Phyton-Skript\Pixel_Fotos\Date\Date")



# [y, x]

def mein_pixel(x_von, x_bis, y_von, y_bis, size, Farbe):
    for x in range(x_von * size, x_bis * size): # X-Achse
        for y in range(y_von * size, y_bis * size): # Y-Achse
            data[y, x] = Farbe


# RGB


size = 10

# df = pd.DataFrame()




for x in range(len(df)): #### len anpassen len(df)
    
    print(x)


    
    #%% Layout
    # =============================================================================
    # Außen
    # =============================================================================
    data = np.zeros((100 * size, 100 * size, 3), dtype=np.uint8)
    
    # # =============================================================================
    # # Links oben
    # # =============================================================================
    # mein_pixel(x_von = 5, x_bis = 395, y_von = 5, y_bis = 415, size = 1, Farbe = Layout3)
    
    
    
    #%% Pos 1
    def num(alphabet, pos_x, pos_y):
    
        
    
        # =============================================================================
        # "-"
        # =============================================================================
        if alphabet == "-":
            mein_pixel(x_von = 2 + pos_x, x_bis = 7 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
    
        
        # =============================================================================
        # 1    
        # =============================================================================
        if alphabet == 1:
        
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 5 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 7 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
    
        # =============================================================================
        # 2    
        # =============================================================================
        if alphabet == 2:
        
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 3 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 5 + pos_x, y_von = 6 + pos_y, y_bis = 7 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 4 + pos_x, y_von = 7 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 7 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
    
    
        # =============================================================================
        # 3    
        # =============================================================================
        if alphabet == 3:
        
            mein_pixel(x_von = 2 + pos_x, x_bis = 7 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 5 + pos_x, y_von = 4 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 6 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 7 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
    
    
        # =============================================================================
        # 4    
        # =============================================================================
        if alphabet == 4:
        
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 7 + pos_x, y_von = 6 + pos_y, y_bis = 7 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 4 + pos_x, y_von = 4 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 5 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
    
    
    
        # =============================================================================
        # 5    
        # =============================================================================
        if alphabet == 5:
        
            mein_pixel(x_von = 2 + pos_x, x_bis = 7 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 6 + pos_x, y_von = 4 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 5 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 7 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
    
    
    
        # =============================================================================
        # 6    
        # =============================================================================
        if alphabet == 6:
        
            mein_pixel(x_von = 4 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 4 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 4 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 6 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
    
    
        # =============================================================================
        # 7    
        # =============================================================================
        if alphabet == 7:
        
            mein_pixel(x_von = 2 + pos_x, x_bis = 7 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 3 + pos_y, y_bis = 4 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 4 + pos_x, y_von = 6 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 4 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 5 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
    
    
        # =============================================================================
        # 8    
        # =============================================================================
        if alphabet == 8:
        
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 3 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 6 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 3 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 6 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
    
    
        # =============================================================================
        # 9    
        # =============================================================================
        if alphabet == 9:
        
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 3 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 3 + pos_y, y_bis = 7 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 7 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 5 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
    
        # =============================================================================
        # 0    
        # =============================================================================
        if alphabet == 0:
        
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 2 + pos_y, y_bis = 3 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 6 + pos_x, y_von = 8 + pos_y, y_bis = 9 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 2 + pos_x, x_bis = 3 + pos_x, y_von = 3 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 6 + pos_x, x_bis = 7 + pos_x, y_von = 3 + pos_y, y_bis = 8 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 5 + pos_x, x_bis = 6 + pos_x, y_von = 4 + pos_y, y_bis = 5 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 4 + pos_x, x_bis = 5 + pos_x, y_von = 5 + pos_y, y_bis = 6 + pos_y, size = size, Farbe = [255,255,255])
            mein_pixel(x_von = 3 + pos_x, x_bis = 4 + pos_x, y_von = 6 + pos_y, y_bis = 7 + pos_y, size = size, Farbe = [255,255,255])
    
    
    
    # num(1, 0, 0)
    # num(2, 0, 0)
    # num(3, 0, 0)
    # num(4, 0, 0)
    # num(5, 0, 0)
    # num(6, 0, 0)
    # num(7, 0, 0)
    # num(8, 0, 0)
    # num(9, 0, 0)
    # num(0, 0, 0)
    
    
    # df.iloc[0, 0]
    # df.iloc[0, 1]
    # df.iloc[0, 2]
    # df.iloc[0, 3]
    # df.iloc[0, 4]
    # df.iloc[0, 5]
    # df.iloc[0, 6]
    # df.iloc[0, 7]
    # df.iloc[0, 8]
    # df.iloc[0, 9]
    
    
    
    num(df.iloc[x, 0], 0 + 8, 14)
    num(df.iloc[x, 1], 8 + 8, 14)
    num(df.iloc[x, 2], 16 + 8, 14)
    num(df.iloc[x, 3], 24 + 8, 14)
    num(df.iloc[x, 4], 32 + 8, 14)
    num(df.iloc[x, 5], 40 + 8, 14)
    num(df.iloc[x, 6], 48 + 8, 14)
    num(df.iloc[x, 7], 56 + 8, 14)
    num(df.iloc[x, 8], 64 + 8, 14)
    num(df.iloc[x, 9], 72 + 8, 14)
    

    
    #%%
    
    # =============================================================================
    # logo
    # =============================================================================
    mein_pixel(x_von = 92, x_bis = 99, y_von = 94, y_bis = 95, size = size, Farbe = white)
    mein_pixel(x_von = 92, x_bis = 97, y_von = 96, y_bis = 97, size = size, Farbe = white)
    mein_pixel(x_von = 92, x_bis = 95, y_von = 98, y_bis = 99, size = size, Farbe = white)
        
    
    
    #%%
    
    image = Image.fromarray(data)
    
    # image.show()
    
        
    image.save(str(df.iloc[x, 10]) + ".png")
