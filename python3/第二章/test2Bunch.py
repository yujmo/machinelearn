# Bunch类提供一种key,value的对象形式
# target_name:所有分类集名称列表
# label:每个文件的分类标签列表
# filenames:文件路径
# contents:分词后文件词向量形式	
import os 
import jieba
import pickle
from sklearn.datasets.base import Bunch
	
def readfile(path):
    with open(path) as fp:
        return fp.read()
	
bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])	
wordbag_path = "test_word_bag/test_set.dat"  # 未分词分类语料库路径
seg_path = "test_corpus_seg/"      # 分词后分类语料库路径
bunch.target_name.extend(os.listdir(seg_path))

for mydir in os.listdir(seg_path):
    class_path = seg_path+mydir+"/"    # 拼出分类子目录的路径
    file_list = os.listdir(class_path)    # 获取class_path下的所有文件
    for file_path in file_list:           # 遍历类别目录下文件
        fullname = class_path + file_path   # 拼出文件名全路径
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())

#对象持久化                                                                                     
file_obj = open(wordbag_path,"wb")
pickle.dump(bunch,file_obj)                      
file_obj.close()
print("构建文本对象结束！！！")
