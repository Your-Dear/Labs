import cv2
import numpy as np

image_path = 'variant-3.jpeg'
image = cv2.imread(image_path)
if image is None:
    raise ValueError("Не удалось загрузить изображение. Проверьте путь к файлу.")


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv_image, lower_red, upper_red)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Check if its centered
center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
square_size = 200
top_left = (center_x - square_size // 2, center_y - square_size // 2)
bottom_right = (center_x + square_size // 2, center_y + square_size // 2)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if top_left[0] < x < bottom_right[0] and top_left[1] < y < bottom_right[1]:
        print("Метка находится внутри центрального квадрата.")
    else:
        print("Метка находится вне центрального квадрата.")

cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
