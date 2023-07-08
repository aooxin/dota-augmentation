import glob
import os


Class='W1'
folder_path = "/Users/aoxin/CODE/python/search/lables"

output_path = "/Users/aoxin/CODE/python/search/output/filenames_with_"+Class+'.txt'

txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

files_with_L1 = []

for txt_file in txt_files:
    with open(txt_file, "r") as f:
        content = f.read()
        if Class in content:
            files_with_L1.append(os.path.basename(txt_file))

with open(output_path, "w") as output_file:
    for file_name in files_with_L1:
        output_file.write(f"{file_name[:-4]}\n")

print(f"{output_path}")