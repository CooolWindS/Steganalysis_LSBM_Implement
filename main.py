
import os
import sys
import numpy as np

from steg_analysis_lib import read_file
from steg_analysis_lib import image_process
from steg_analysis_lib import math_process

NAME = 'name'
NAME_WITH_DIR = 'namedir'
EMBEDDING_RATE = 1

def main():
	
	# error input
	if len(sys.argv)<3:
		print("\n", sys.argv[0], "<cover_data_dir> <stego_data_dir>\n")
		sys.exit(0)
	##
	
	# read file
	# 
	file_cover_list = read_file.read_file_name(sys.argv[1], NAME_WITH_DIR)
	file_stego_list = read_file.read_file_name(sys.argv[2], NAME_WITH_DIR)
	#
	##
	
	image = read_file.read_img('../5000_SOURCE/01-source-00001.bmp')
	(image_r, image_g, image_b) = image_process.extract_img_rgb(image)
	
	hist_r = image_process.caculate_img_hist(image_r)
	
	local_max_r = np.array(math_process.find_local_max(hist_r))
	local_min_r = np.array(math_process.find_local_min(hist_r))
	local_extreme_r = np.concatenate([local_max_r, local_min_r])
	print(local_max_r)
	print(local_min_r)
	print(local_extreme_r)
	
	
	


if __name__ == "__main__":
    main()
