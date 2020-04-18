'''
Some info on various layers, so you know what to expect
depending on which layer you choose:


layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles?
layer 5: eyes
layer 6: dogs, bears, cute animals.
layer 7: faces, buildings
layer 8: fish begin to appear, frogs/reptilian eyes.
layer 10: Monkies, lizards, snakes, duck

Choosing various parameters like num_iterations, rescale,
and num_repeats really varies on which layer you're doing.
'''

from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import cv2
import random
import os

layer_tensor = model.layer_tensors[3]
num_iterations = 5
step_size = 1
rescale_factor = 0.37
num_repeats = 5
blend = 0.5

dream_name = 'milkyway(1)' #where your picture is (Directory)
x_size = 1125
y_size = 2436

for i in range(0, 600):
    #for generate picture, you have to name your default picture (img_0)
    if os.path.isfile('Dreams/{}/img_{}.jpg'.format(dream_name, i+1)):
        print('{} already exists, continuing along...'.format(i+1))

    else:
        img_result = load_image(filename='Dreams/{}/img_{}.jpg'.format(dream_name, i))

        # this impacts how quick the "zoom" is
        x_trim = 2
        y_trim = 1                                             

        img_result = img_result[0+x_trim:y_size-y_trim, 0+y_trim:x_size-x_trim]
        img_result = cv2.resize(img_result, (x_size, y_size))

        # Use these to modify the general colors and brightness of results.
        # results tend to get dimmer or brighter over time, so you want to
        # manually adjust this over time.

        # +2 is slowly dimmer
        # +3 is slowly brighter
        
        img_result[:, :, 0] += random.choice([2 , 2.5 , 3])  # reds
        img_result[:, :, 1] += random.choice([2 , 2.5 , 3])  # greens
        img_result[:, :, 2] += random.choice([2 , 2.5 , 3])  # blues
        
        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)

        img_result = recursive_optimize(layer_tensor=layer_tensor,
                                        image=img_result,
                                        num_iterations=num_iterations,
                                        step_size=step_size,
                                        rescale_factor=rescale_factor,#downscaling
                                        num_repeats=num_repeats,#it's better to keep it one because every frame will change gradually
                                        blend=blend)#how much filter effects on picture

        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)
        result = PIL.Image.fromarray(img_result, mode='RGB')
        result.save('dreams/{}/img_{}.jpg'.format(dream_name, i+1))