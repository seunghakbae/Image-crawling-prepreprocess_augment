from Config import get_args
from Augmentator import Augmentator

def main():
    config = get_args()
    augmentator = Augmentator(config)
    augmentator.save()

if __name__ == "__main__":
    main()