import sys
sys.path.append('./external-libraries')
import jieba
import collections
import re
import matplotlib.pyplot as plt
from paddle.external_libraries import wordcloud
import pandas as pd

def generate_wc(string_data):
    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')       # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data)           # 将符合模式的字符去除
    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词

    object_list = []
    remove_words = []
    
    # #读取停用词
    # with open("./paddle/work/停用词库.txt",'r',encoding='utf-8') as fp:
    #     for word in fp:
    #         remove_words.append(word.replace("\n",""))
    
    for word in seg_list_exact:                              # 循环读出每个分词
        if word not in remove_words:                         # 如果不在去除词库中
            object_list.append(word)                         # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(object_list)           # 对分词做词频统计
    word_counts_top20 = word_counts.most_common(20)          # 获取前20最高频的词
    print(word_counts_top20)
    # 词频展示
    wc = wordcloud.WordCloud(
        font_path='./paddle/work/simhei.ttf',                # 设置字体格式
        background_color="#000000",                          # 设置背景图
        max_words=150,                                       # 最多显示词数
        max_font_size=60,                                    # 字体最大值
        width=707,
        height=499
    )
    wc.generate_from_frequencies(word_counts)                # 从字典生成词云

    plt.imshow(wc)                                           # 显示词云
    plt.axis('off')                                          # 关闭坐标轴
    plt.savefig('./result/wordcloud.jpg')
    plt.show()   


review_df = pd.read_json('./paddle/work/actors.json')

content_str = ""
for row in review_df.index:
    content = review_df.loc[row,'role_escription']
    content_str += content

generate_wc(content_str) 

