import jieba 

seg_list = jieba.cut("小明1995年毕业于常州大学")
print("".join(seg_list))
