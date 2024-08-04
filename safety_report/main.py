import sys
import os

sys.path.append(os.path.dirname(__file__))

import __init__ as config

if __name__ == "__main__":
    print(config.API_KEY_PATH)