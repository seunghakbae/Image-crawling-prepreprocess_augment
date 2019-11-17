import argparse

def get_args():
    argp =argparse.ArgumentParser(description="Google Image Cralwer")

    # Image to search for
    argp.add_argument("--image_name", type=str, help="Type in the name of images that you would like to search")
    # chrome Driver path
    argp.add_argument("--chrome_driver_path", type=str, help="Type in the path to chrome Driver")

    return argp.parse_args()