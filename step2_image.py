import cv2
import numpy as np

image = np.ones((400,600,3),dtype=np.uint8) * 255

image[190:210, :] = 0
cv2.imwrite("test_Image.png", image)
cv2.imshow('Test Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print ("test_Image created and saved! ")

