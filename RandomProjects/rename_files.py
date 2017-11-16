# # Renaming a list of files in a folder.
#
# """
# The names have hours, minutes, and seconds.
# Input
# 01h02m02s.wav
# 01h02m13s.wav
# 01h02m24s.wav
# Rename them with the durations above converted to seconds
# Output
# 3722s.wav
# 3733s.wav
# 3744s.wav

import os
import shutil


def rename_files(fldr):

    for file in os.listdir(fldr):
        hours = int(file[:2])
        minutes = int(file[3:5])
        seconds = int(file[6:8])
        print(hours)
        total_time = (hours*60*60) + (minutes*60) + seconds
        shutil.move(fldr+file, fldr+str(total_time)+'s.wav')


print(rename_files('music/'))
