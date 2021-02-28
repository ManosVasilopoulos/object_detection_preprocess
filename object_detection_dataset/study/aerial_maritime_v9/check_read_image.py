from detection.handlers.image_handler import Image_Handler
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Aerial Maritime v9'

    ih = Image_Handler(dataset_dir)

    img = ih.read_image('DJI_0258_JPG.rf.0c4380c012e940ff668b008ffe35a52c.jpg')
    print(img.shape)
    imshow(img)
    plt.show()

