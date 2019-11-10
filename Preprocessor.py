import cv2
import os


class Preprocessor():

    def __init__(self, config):
        self.image_path = config.data_dir # directory path
        self.size = config.image_size # resize


    def preprocess(self, image_path, image_name):

        try:
            image = cv2.imread(image_path) # read image from cv2
            name = image_name #image name
        except:
            print("Can not find image : " + image_path)
            return

        # Cropping

        try:
            edged = cv2.Canny(image, 10, 250)

            # applying closing function
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
            closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

            # finding_contours
            (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            area = 0 # Max Area

            for c in cnts:
                x, y, w, h = cv2.boundingRect(c) # x,y,w,h of contour
                if w > 50 and h > 50:

                    n_area = w * h
                    if n_area > area: # if new contour has bigger area
                        area = n_area
                        cropped_image = image[y:y + h, x:x + w] #cropped image is replaced

            # for c in cnts:
            #         x, y, w, h = cv2.boundingRect(c) # x,y,w,h of contour
            #         picMax = [x, y, w, h] # contour that has Max num of w and h
            #
            #         if w > 50 and h > 50:
            #             if (picMax[2] * picMax[3]) < w*h: # if new contour has bigger area
            #                 picMax = [x,y,w,h] # picMax is changed
            #
            # x, y, w, h = picMax
            # cropped_image = image[y:y + h, x:x + w] # new cropped image

        except:
            print('Error in Cropping')
            print("File : " + name)
            return

        # Resize
        height = self.size # height
        width = self.size # widht
        dim = (height, width)

        try:
            resized_image = cv2.resize(cropped_image, dim, interpolation=cv2.INTER_LINEAR) # resize image
        except:
            print('Error in Resizing')
            print("File : " + name)
            return

        return resized_image

    def save(self):

        try:
            image_list = os.listdir(self.image_path) # image list
        except:
            print("Not a proper Directory path Error : " + self.image_path)
            print("Please type in proper directory path again")
            return

        save_path = self.image_path + "_Preprocessed" # directory path that saves all the preprocessed images
        try:
            os.mkdir(save_path) # create directory
        except:
            print("directory with same name already exists.")
            print("Please remove the directory")
            return

        for image_path in image_list:
            formats = [".jpg", ".png", ".jpeg"] # image format

            # get name by deleting format
            for format in formats:
                if format in image_path:
                    image_name = image_path.replace(format, "")

            preprocessed_image = self.preprocess(self.image_path + "\\" + image_path, image_name)
            cv2.imwrite(save_path + "\\" + image_name + ".jpg", preprocessed_image)
