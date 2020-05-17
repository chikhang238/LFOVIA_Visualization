from mat4py import loadmat
import os
import sys
sys.path.append("..")

def load_data(databasename, video_index):

    entries = os.listdir(databasename)

    file_path = databasename + '/' + entries[video_index] #video index starts with 0
        
    data = loadmat(file_path)

    return data
