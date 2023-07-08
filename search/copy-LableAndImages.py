import os
import glob
import shutil

file_path = "/Users/aoxin/CODE/python/search/output/filenames_with_W1.txt"
image_path = "/Users/aoxin/CODE/python/search/images"
lable_path = "/Users/aoxin/CODE/python/search/lables"
output_path = "/Users/aoxin/CODE/python/search/output"

# read lines in file_path and return a list
def read_file(file_path):
    with open(file_path, "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content
    
# copy filename in list to output_path
def copy_file(file_path, output_path):
    for file_name in file_path:
        shutil.copy(os.path.join(image_path, file_name+'.tif'), output_path+'/images/')
        shutil.copy(os.path.join(lable_path, file_name+'.txt'), output_path+'/lables/')


if __name__ == "__main__":
    file_name = read_file(file_path)
    copy_file(file_name, output_path)
    print("Done!")


