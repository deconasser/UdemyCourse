import cv2
import numpy as np


def call_back_func(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at ({x}, {y})")
    elif event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse moved to ({x}, {y})")


cv2.namedWindow("image")
cv2.setMouseCallback("image", call_back_func)

img = np.zeros((512, 512, 3), np.int8)
while True:
  cv2.imshow('image', img)
  if cv2.waitKey(20) & 0xFF == 27:  # Nhấn phím ESC để thoát
      break

cv2.destroyAllWindows()

