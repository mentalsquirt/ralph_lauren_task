import os
import cv2
import numpy as np

def preprocess(cloth, cloth_mask):
  # init a blue background with the correct shape
  blue_background = np.zeros(cloth.shape, dtype=np.uint8)
  blue_background[:] = (255, 0, 0)
  mask = cloth_mask
  inv_mask = cv2.bitwise_not(mask)
  
  # use erosion/dilation on the mask to remove noise
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
  mask = cv2.erode(mask, kernel, iterations=3)
  mask = cv2.dilate(mask, kernel, iterations=1)
  inv_mask = cv2.erode(inv_mask, kernel, iterations=3)
  inv_mask = cv2.dilate(inv_mask, kernel, iterations=6)
  
  # use the cloth mask to isolate the cloth from the background
  masked_cloth = cv2.bitwise_and(cloth, cloth, mask=mask)
  cv2.imshow("masked_cloth`", masked_cloth)
  
  # use the inverted mask to isolate the background
  blue_background = cv2.bitwise_and(blue_background, blue_background, mask=inv_mask)
  cv2.imshow("blue_background", blue_background)
  
  # combine
  result = cv2.add(masked_cloth, blue_background)
  cv2.imshow("result", result)

  return result

def convert_to_3_channel(image):
  # check if image is grayscale
  if len(image.shape) == 2:
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
  # check if image is 4 channel (RGBA)
  elif image.shape[2] == 4:
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
  return image

if __name__ == "__main__":
  name = "28"
  cloth = cv2.imread(os.path.join(name, name + ".jpg"))
  cloth = convert_to_3_channel(cloth)
  mask = cv2.imread(os.path.join(name, name + "_mask.jpg"), 0)
  res = preprocess(cloth, mask)
  cv2.imwrite(os.path.join(name, name + "_blue_background.jpg"), res)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
