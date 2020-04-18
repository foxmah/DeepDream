import cv2
import os

x = 1125
y = 2436
dream_name = "milkyway(1)"
dream_path = "Dreams/{}".format(dream_name)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('{}.mp4'.format(dream_name) , fourcc , 20 , (x , y))
for i in range(99999999):
	if os.path.isfile('Dreams/{}/img_{}.jpg'.format(dream_name, i+1)):
		print('{} already exists, continuing along...'.format(i+1))

	else:
		dream_lenght = i
		break

for i in range(dream_lenght+1):
	img_path = os.path.join(dream_path, "img_{}.jpg".format(i))
	print(img_path)
	frame = cv2.imread(img_path)
	out.write(frame)

out.release()