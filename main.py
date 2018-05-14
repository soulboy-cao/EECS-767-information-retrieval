from processing import processing
from indexing import indexing
from vs_model import vs_model_pre
from download_html import download_html
import pickle
import os
import time


def get_url_dic():
    with open("url_dic.dat", 'rb') as f:
        url_dic = pickle.load(f)
    return url_dic


processed_dir = "../processed_data/"
isExists = os.path.exists(processed_dir)
if not isExists:
    os.makedirs(processed_dir)

origin_dir = "../webpages/"
isExists = os.path.exists(origin_dir)
if not isExists:
    os.makedirs(origin_dir)
    
file_path = "../doc_ku/crawled.txt"

download_html(file_path,origin_dir)
print("Download html finished.")


url_dic = get_url_dic()
file_num = len(url_dic)
processing(origin_dir, processed_dir)
print("Finish processing html files.")
start = time.time()
indexing(url_dic, processed_dir)
end = time.time()
print("Finish indexing.")
print(end-start)
start = time.time()
vs_model_pre(file_num)
end = time.time()
print(end-start)
print("Finish vs model preparation.")
