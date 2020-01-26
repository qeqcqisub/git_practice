import os
import numpy as np
from PIL import Image

# Raw Image to BMP File
for i in range(10):    
    raw_img = np.fromfile('./raw/'+str(i)+'.raw', dtype='uint8') 
    # print(raw_img.shape)
    raw_img=np.reshape(raw_img,(480,640))
    # print(raw_img.shape)
    Image.fromarray(raw_img).save('./bmp/'+str(i)+'.bmp')