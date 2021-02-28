from detection.handlers.image_handler import Image_Handler
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SeaShips'
    ih = Image_Handler(dataset_dir)

    img = ih.read_image('000001.jpg')
    print(img.shape)
    print(img.shape)
    imshow(img)
    plt.show()
