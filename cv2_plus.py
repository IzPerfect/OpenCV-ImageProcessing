from matplotlib import pyplot as plt
from matplotlib import font_manager, rc # 주피터 한글 폰트 출력을 위해 추가
import cv2

# 밑의 font_name과 rc는 주피터 한글 폰트 출력을 위해 추가
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def img_show(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

def imshow(image, title = None, fig_size = None, img_type = 1):
	if fig_size == None:
		pass
	else:
		plt.figure(figsize= fig_size)

	if title == None:
		pass
	else:
		plt.title(title)
	
	if img_type == 1:
		plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
		plt.show()
	elif img_type == 0:
		plt.imshow(image, cmap= 'gray')
		plt.show()
		
	else:
		print('1(color) 혹은 0(gray)을 선택')
