import argparse
import glob
import os
import shutil
import random

basename = os.path.basename

import numpy as np

from utils import get_module_logger


def split(data_dir):
    files = glob.glob(data_dir + "/training_and_validation/*")
#     print(files)
    num_files = len(files)
    train = .6
    val = .2
    test = .2
    for i, file in enumerate(files):
        rand_num = random.random()
        if rand_num < .6:
            shutil.move(file, data_dir + "/train/" + basename(file))
        elif rand_num <.8:
            shutil.move(file, data_dir + "/val/" + basename(file))
        else:
            print(file, data_dir + "/test/" + basename(file))
            shutil.move(file, data_dir + "/test/" + basename(file))
        
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=False,
                        default="/home/workspace/data/waymo",
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)