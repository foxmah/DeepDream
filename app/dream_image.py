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


We could probably come up with some sort of formula. The
deeper the layer is, the more iterations and
repeats you will want.

Layer 3: 20 iterations, 0.5 rescale, and 8 repeats is decent start
Layer 10: 40 iterations and 25 repeats is good. 
'''
def processing(filename):
    from deepdreamer import model, load_image, recursive_optimize
    import numpy as np
    import PIL.Image

    layer_tensor = model.layer_tensors[1]
    img_result = load_image(filename='{}'.format(filename))

    img_result = recursive_optimize(layer_tensor=layer_tensor, image=img_result,
                    # how clear is the dream vs original image        
                    num_iterations=5, step_size=1.0, rescale_factor=0.5,
                    # How many "passes" over the data. More passes, the more granular the gradients will be.
                    num_repeats=5, blend=1)

    img_result = np.clip(img_result, 0.0, 255.0)
    img_result = img_result.astype(np.uint8)
    result = PIL.Image.fromarray(img_result, mode='RGB')
    filename = filename.split(".")
    filename = str(filename[0]) + "_out." + str(filename[1])
    result.save(f'{filename}')
    #print("filename: " , filename)
    #result.show()



