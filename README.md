# Image Crawling, Preprocessing, Augmentation Code

Python code for Image Crawler, Preprocesser and Augmentation.

Threre are three separate python program for each image crawling, image preprocessing and image augmentation. 

## How to use Image Crawler

1. Before using this Image cralwer, you need to install Chrome Driver.

2. Type in the name of image you would like to search for.

3. Type in the path to chrome driver

usage: Main.py [-h] [--image_name IMAGE_NAME]
               [--chrome_driver_path CHROME_DRIVER_PATH]

##### optional arguments:
  -h, --help            show this help message and exit

--image_name IMAGE_NAME
                        Type in the name of images that you would like to search

--chrome_driver_path CHROME_DRIVER_PATH
                        Type in the path to chrome Driver

##### usage example :
--image_name pancake --chrome_driver_path C:\Users\ASUS\Pictures\Desktop\Chromedriver


## How to use Image Preprocessor

It crops out the center image and discards unnecesary image segment such as letters and it resizes the images to predefined image size.

1. Type in the path to the directory where all the images are saved.

3. Type in the image size you would like to resize (default is 220 x 220)

usage: Main.py [-h] [--data_dir DATA_DIR] [--image_size IMAGE_SIZE]

##### optional arguments:
  -h, --help            show this help message and exit
  
  --data_dir DATA_DIR   path of directory
  
  --image_size IMAGE_SIZE
                        resize image size

##### usage example :
--data_dir C:\Users\ASUS\Programming\Deep_learning\Image_preprocessing\code\Crawler\pumpkin --image_size 220


## How to use Image Augmentator

It flips the image left to right and rotates it by 90, 180, and 270 degree.

1. Type in the path to the directory where all the images are saved.

3. Type in the image size you would like to resize (default is 220 x 220)

usage: Main.py [-h] [--image_directory_path IMAGE_DIRECTORY_PATH]

##### optional arguments:

  -h, --help            show this help message and exit

  --image_directory_path IMAGE_DIRECTORY_PATH
                        Type in the path to the directory of images

##### usage example :
--image_directory_path C:\Users\ASUS\Programming\Deep_learning\Image_preprocessing\code\Crawler\pumpkin
