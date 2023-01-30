import math
import numpy as np
import cv2

def psnr(img1,img2):
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1-img2)**2)
    if mse == 0:
        return float('inf')
    return 20*math.log10(255.0/math.sqrt(mse))


#imgA = cv2.imread('./Original/a4568-kme_0578.png',cv2.IMREAD_UNCHANGED)#dataset
imgA = cv2.imread('./Original/n03950228_pitcher.jfif',cv2.IMREAD_UNCHANGED)#imagenet

#imgB = cv2.imread('./c/a4568-kme_0578_glad.png',cv2.IMREAD_UNCHANGED)#dataset
imgB = cv2.imread('./c/n03950228_pitcher_glad.png',cv2.IMREAD_UNCHANGED)#imagenet

#imgC = cv2.imread('./g/a4568-kme_0578_glad.png',cv2.IMREAD_UNCHANGED)#dataset
imgC = cv2.imread('./g/n03950228_pitcher_glad.png',cv2.IMREAD_UNCHANGED)#imagenet

#imgD = cv2.imread('./u/a4568-kme_0578_glad.png',cv2.IMREAD_UNCHANGED)#dataset
imgD = cv2.imread('./u/n03950228_pitcher_glad.png',cv2.IMREAD_UNCHANGED)#imagenet

scoreC = psnr(imgA,imgB)
scoreG = psnr(imgA,imgC)
scoreU = psnr(imgA,imgD)
print('PSNR of CBAM image is: %0.5f'% scoreC)
print('PSNR of GLADNet image is: %0.5f'% scoreG)
print('PSNR of UNet image is: %0.5f'% scoreU)


