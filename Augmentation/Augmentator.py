from PIL import Image
import PIL
import os
import matplotlib as plt

class Augmentator():

    def __init__(self, config):
        self.path = config.image_directory_path

    def augment(self, image_path):

        try:
            image =Image.open(image_path)
        except:
            print("Can not find image : " + image_path)
            return

        # Augmentation

        # Flip Left_Right
        flipped_image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)

        # Rotate
        rotated_image_90 = image.transpose(PIL.Image.ROTATE_90)
        rotated_image_180 = image.transpose(PIL.Image.ROTATE_180)
        rotated_image_270 = image.transpose(PIL.Image.ROTATE_270)

        return image, flipped_image, rotated_image_90, rotated_image_180, rotated_image_270

    def save(self):

        try:
            image_list =os.listdir(self.path)
        except:
            print("Not a proper Directory path Error : " + self.image_path)
            print("Please type in proper directory path again")
            return

        save_path =self.path + "_Augmentated"

        try:
            os.mkdir(save_path) # create directory
        except:
            print("directory with same name already exists.")
            print("Please remove the directory")
            return

        image_index = 1

        for image_path in image_list:
            image, flipped_image, rotated_image_90, rotated_image_180, rotated_image_270 = self.augment(self.path + "\\" + image_path)

            image.save(save_path + "\\" + str(image_index) + ".jpg")
            image_index += 1

            flipped_image.save(save_path + "\\" + str(image_index) + ".jpg")
            image_index += 1

            rotated_image_90.save(save_path + "\\" + str(image_index) + ".jpg")
            image_index += 1

            rotated_image_180.save(save_path + "\\" + str(image_index) + ".jpg")
            image_index += 1

            rotated_image_270.save(save_path + "\\" + str(image_index) + ".jpg")
            image_index += 1