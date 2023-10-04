import os
import time 
import shutil
import threading
from code.convert import *
from code.helper.utils import *
from code.helper.imageTools import *

def multi_file_Video_convert(path):
    tic = time.perf_counter()
    path = check_full_path(path)
    proc = os.cpu_count()
    print('Number of processors: ' + str(proc))
    videos = glob.glob(path + '*.mp4')
    count = len(videos)
    print(count)
    thread_list = []
    a = 0
    cpu = 0
    while a <= len(videos):
        for cpu in range(proc):
            try:
                thread = threading.Thread(target=convertAVideoToImage, args=(videos[a], path))
                thread_list.append(thread)
                thread_list[-1].start()
            except:
                pass
            cpu += 1
            a += 1
        for i in thread_list:
            thread.join()
            cpu -= (len(videos) - a)
            if cpu <= 0:
                cpu = 0
    print('All threads finished')
