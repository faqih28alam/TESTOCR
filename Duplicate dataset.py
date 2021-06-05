import albumentations as A
import numpy as np
import cv2
#untuk menginput serangkaian files
import glob
import os

os.mkdir('C:/Users/user/Downloads/DATASET KTP/img_gray')
img_path = glob.glob('C:/Users/user/Downloads/DATASET KTP/*.jpg')

i=0
for imgs in img_path:
    
    # Declare an augmentation pipeline
    transform = A.Compose([
        #A.RandomCrop(width=256, height=256),
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
    ])

    #membaca gambar
    img = cv2.imread(imgs)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Augment an image
    transformed = transform(image=img)
    transformed_image = transformed["image"]

    #menampilkan gambar
    cv2.imshow('akhirnya', img_gray)
    #menyimpan gambar
    cv2.imwrite('C:/Users/user/Downloads/DATASET KTP/img_gray/image%02i.jpg' %i, img_gray)
    i += 1
    
    #menunda agar windows tidak langsung hilang
    cv2.waitKey(600)

    #menghilangkan windows
    cv2.destroyAllWindows()
