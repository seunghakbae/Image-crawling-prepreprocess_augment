import argparse

def get_args():
    argp = argparse.ArgumentParser(description="Image Augmentator")

    argp.add_argument("--image_directory_path", type=str, help="Type in the path to the directory of images")

    return argp.parse_args()