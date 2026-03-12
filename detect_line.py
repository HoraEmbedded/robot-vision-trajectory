import cv2
import numpy as np

image = cv2.imread("test_Image.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]

black_pixels = np.sum(binary == 0)

line_center = np.where(binary == 0)[0].mean()

print(f"Line detected at row: {line_center:.2f}, black pixels: {black_pixels}")

cv2.imshow("Binary Image", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
