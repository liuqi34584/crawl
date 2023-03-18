import jieba
import collections
import re
import matplotlib.pyplot as plt
import wordcloud
import pandas as pd
from crawl_wiki_data import crawl_wiki_data
from crawl_wiki_data import crawl_everyone_wiki_urls
from crawl_wiki_data import crawl_viewing_data
from crawl_wiki_data import parse_viewing_data


def generate_wc(string_data):
    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')       # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data)           # 将符合模式的字符去除
    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词

    object_list = []
    remove_words = []
    
    
    for word in seg_list_exact:                              # 循环读出每个分词
        if word not in remove_words:                         # 如果不在去除词库中
            object_list.append(word)                         # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(object_list)           # 对分词做词频统计
    word_counts_top20 = word_counts.most_common(20)          # 获取前20最高频的词
    print(word_counts_top20)
    # 词频展示
    wc = wordcloud.WordCloud(
        font_path='./work/simhei.ttf',                # 设置字体格式
        background_color="#000000",                          # 设置背景图
        max_words=150,                                       # 最多显示词数
        max_font_size=60,                                    # 字体最大值
        width=707,
        height=499
    )
    wc.generate_from_frequencies(word_counts)                # 从字典生成词云

    return wc



def main():
    crawl_wiki_data()  # 爬取百度百科中《隐秘而伟大》中所有演员信息，返回页面数据
    crawl_everyone_wiki_urls()  # 爬取每个演员的百度百科页面的信息，并进行保存

    viewing_table = crawl_viewing_data()  # 爬取百度百科中《隐秘而伟大》收视情况，返回html   
    parse_viewing_data(viewing_table)  # 对《隐秘而伟大》的收视情况table进行解析，并保存
     
    print("所有信息爬取完成！")


    df = pd.read_json('./work/viewing_infos.json',dtype = {'broadcastDate' : str})
    broadcastDate_list = df['broadcastDate']
    csm59_rating_list = df['csm59_rating']
    csm_rating_list = df['csm_rating']

    df = pd.read_json('./work/viewing_infos.json',dtype = {'broadcastDate' : str})
    broadcastDate_list = df['broadcastDate']
    csm59_rating_list = df['csm59_rating']

    review_df = pd.read_json('./work/actors.json')
    content_str = ""
    for row in review_df.index:
        content = review_df.loc[row,'role_escription']
        content_str += content

    wc = generate_wc(content_str) 

    plt.figure(figsize=(18, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.grid() 

    plt.subplot(1, 3, 1)
    plt.title("《隐秘而伟大》收视率变化趋势",fontsize=10) 
    plt.xlabel("播出日期",fontsize=10) 
    plt.ylabel("收视率%",fontsize=10) 
    plt.xticks(rotation=45,fontsize=5)
    plt.yticks(fontsize=10)
    plt.plot(broadcastDate_list,csm59_rating_list,label = "CSM59城市网收视率") 
    plt.plot(broadcastDate_list,csm_rating_list,label = "CSM全国网收视率") 
    plt.legend()
    plt.savefig('./work/chart02.jpg')

    plt.subplot(1, 3, 2)
    plt.title("《隐秘而伟大》CSM59城市网收视率变化趋势",fontsize=10) 
    plt.xlabel("播出日期",fontsize=10) 
    plt.ylabel("收视率%",fontsize=10) 
    plt.xticks(rotation=45,fontsize=5)
    plt.yticks(fontsize=10)
    plt.plot(broadcastDate_list,csm59_rating_list) 
    plt.savefig('./work/chart01.jpg')

    plt.subplot(1, 3, 3)
    plt.title("词云",fontsize=10) 
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.savefig('./work/wordcloud.jpg')

    plt.show()


if __name__ == '__main__': 
    main()

