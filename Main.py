from Config import get_args
from Preprocessor import Preprocessor

def main():
    config = get_args()
    preprocessor = Preprocessor(config)
    preprocessor.save()

if __name__ == '__main__':
	main()