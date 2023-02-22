import subprocess
import os
import shutil

input_folder = "/Users/akshay.khanna/Documents/Content/Courses/AsyncJS/throttle/"
output_folder_name = "trimmed"
output_folder = input_folder + output_folder_name 
script_path = "/Users/akshay.khanna/prj/practice/jumpcutter/jumpcutter.py"
temp_dir = "/Users/akshay.khanna/prj/practice/jumpcutter/TEMP"
video_file_extension = ".mp4";

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        # os.rmdir(temp_dir)

# Get a list of all the files in the input folder
files = os.listdir(input_folder)

# Loop through the files and run the script on each one
for file in files:

    print(file)
    if not file.endswith(video_file_extension):
        continue

    # Build the input and output paths
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)
    print(output_path)

    

    # Run the script on the file
    process = subprocess.Popen(["python", script_path, "--input_file", input_path, "--output_file", output_path, "--sounded_speed", "1", "--silent_speed", "999999", "--frame_margin", "2", "--frame_rate", "25"])
    process.wait()

    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)


# python jumpcutter.py --input_file input.mp4 --output_file output.mp4 --sounded_speed 1 --silent_speed 999999 --frame_margin 2 --frame_rate 30

# replace spaces with _ in filenames of all files in folders & nested folder using terminal
# find ./ -depth -name '* *' -execdir rename 's/ /_/g' "{}" \;