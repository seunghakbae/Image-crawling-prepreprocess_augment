import argparse

def get_args():
    argp = argparse.ArgumentParser(description="Image Preprocessing")

    # Directory path
    argp.add_argument("--data_dir", type=str, help='path of directory')
    argp.add_argument("--image_size", type=int, default=220, help='resize image size')
    return argp.parse_args()