import math
import numpy as np
import cv2

def ssim(img1,img2):
    C1 = (0.01*255)**2
    C2 = (0.03*255)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11,1.5)
    window = np.outer(kernel,kernel.transpose())

    mu1 = cv2.filter2D(img1,-1,window)[5:-5,5:-5]
    mu2 = cv2.filter2D(img2,-1,window)[5:-5,5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1*mu2
    sigma1_sq = cv2.filter2D(img1**2,-1,window)[5:-5,5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2,-1,window)[5:-5,5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1*img2,-1,window)[5:-5,5:-5] - mu1_mu2

    ssim_map = ((2*mu1_mu2 +C1)*(2*sigma12+C2)) / ((mu1_sq + mu2_sq +C1)*(sigma1_sq + sigma2_sq + C2))

    return ssim_map.mean()

def calculate_ssim(img1,img2):
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions')
    if img1.ndim == 2:
        return ssim(img1,img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1,img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1),np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')

imgA = cv2.imread('./Original/a4568-kme_0578.png',cv2.IMREAD_UNCHANGED)#dataset
#imgA = cv2.imread('./Original/n03950228_pitcher.jfif',cv2.IMREAD_UNCHANGED)#imagenet

imgB = cv2.imread('./c/a4568-kme_0578_glad.png',cv2.IMREAD_UNCHANGED)#dataset
#imgB = cv2.imread('./c/n03950228_pitcher_glad.png',cv2.IMREAD_UNCHANGED)#imagenet

imgC = cv2.imread('./g/a4568-kme_0578_glad.png',cv2.IMREAD_UNCHANGED)#dataset
#imgC = cv2.imread('./g/n03950228_pitcher_glad.png',cv2.IMREAD_UNCHANGED)#imagenet

imgD = cv2.imread('./u/a4568-kme_0578_glad.png',cv2.IMREAD_UNCHANGED)#dataset
#imgD = cv2.imread('./u/n03950228_pitcher_glad.png',cv2.IMREAD_UNCHANGED)#imagenet
scoreC = calculate_ssim(imgA,imgB)
scoreG = calculate_ssim(imgA,imgC)
scoreU = calculate_ssim(imgA,imgD)
print('SSIM of CBAM image is: %0.5f'% scoreC)
print('SSIM of GLADNet image is: %0.5f'% scoreG)
print('SSIM of UNet image is: %0.5f'% scoreU)
