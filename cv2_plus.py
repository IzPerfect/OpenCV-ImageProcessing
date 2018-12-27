from matplotlib import pyplot as plt
import cv2

def img_show(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
