#import libraries
import glob as glob
import os
import numpy as np

from PIL import Image

# Import an image from directory:
read_path = '/content/drive/My Drive/agroNav_LineDetection' #'./data/agroNav_LineDetection'

with open('./data/training/agroNav_LineDetection_train.txt', 'w') as f:
    for file in glob.glob(os.path.join(read_path, '*.jpg')):
	
        filename = os.path.split(file)[1]
        filename = os.path.splitext(filename)[0]
   
        f.write('agroNav_LineDetection_resized_100_100/'+filename+"\n")
        f.write('agroNav_LineDetection_resized_100_100/'+filename+"_flip"+"\n")
  
