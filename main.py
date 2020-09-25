
import os
import sys

from steganalysislib import readfile

NAME = 'name'
NAMEWITHDIR = 'namedir'

def main():
	
	# error input
	if len(sys.argv)<3:
		print("\n", sys.argv[0], "<cover_data_dir> <stego_data_dir>\n")
		sys.exit(0)
	##
	
	# read file
	# 
	fileCoverList = readfile.read_file_name(sys.argv[1], NAMEWITHDIR)
	fileStegoList = readfile.read_file_name(sys.argv[2], NAMEWITHDIR)
	#
	##
	
	#readfile.read_img('./lena.jpg')
	
	


if __name__ == "__main__":
    main()
