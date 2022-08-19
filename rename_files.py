import os

dir_name = "\poses_squat\wrongsquat"

folder_name = os.path.split(dir_name)[1]

folder = str(os.getcwd()) + dir_name

for f in os.listdir(folder):

    filename, f_ext = os.path.splitext(f)

    filename = filename.zfill(3)

    new_name = folder + f"\guy1_{folder_name}{filename}.jpg"

    old_file = folder + f"\{f}"
    os.rename(old_file, new_name)

