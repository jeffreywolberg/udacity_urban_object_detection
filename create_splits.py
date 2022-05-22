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
    for i, file in enumerate(files):
        rand_num = random.random()
        if rand_num < .80:
            shutil.move(file, data_dir + "/train/" + basename(file))
        else:
            shutil.move(file, data_dir + "/val/" + basename(file))

def undo_split(data_dir):
    tf_test_records = ["segment-10072231702153043603_5725_000_5745_000_with_camera_labels.tfrecord", "segment-12012663867578114640_820_000_840_000_with_camera_labels.tfrecord", "segment-12200383401366682847_2552_140_2572_140_with_camera_labels.tfrecord"]
    for name in ["/train", "/val", "/test"]:
        files = glob.glob(data_dir + name + "/*")
        num_files = len(files)
        print(f"{num_files} files in {name} folder")
        for file in files:
            if name == "/test" and basename(file) in tf_test_records:
                continue
            shutil.move(file, data_dir + "/training_and_validation/" + basename(file))

    
    
        
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
#     undo_split(args.data_dir)