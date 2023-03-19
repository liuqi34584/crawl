# 机器学习爬取网页数据

## 本地编译遇到的问题

### 1.如何external_libraries的库文件完成编译

因为paddle环境里的包存在文件缺失问题，不建议这么做

#### 本地编译：
在自己的conda环境里安装以下包：
*   pip install jieba
*   pip install wordcloud
*   pip install bs4
*   pip install lxml

#### paddle编译：
进入paddle环境后，打开Notebook旁边的终端窗口，依次输入以下命令，安装缺失的包：
*   pip install jieba
*   pip install wordcloud
*   pip install bs4
*   pip install lxml

### 2.运行代码时偶尔find_all()函数报错
办法：这个问题在于翻墙，如果以下网站能够访问，就不会报错。[点击这里《隐秘而伟大》](https://baike.baidu.com/item/%E9%9A%90%E7%A7%98%E8%80%8C%E4%BC%9F%E5%A4%A7) 报错请先自行解决网络问题。

### 3.字体问题
#### 字体文件如何下载
1.你可以使用本项目的字体文件[字体STZHONGS.TTF](https://github.com/liuqi34584/crawl/blob/main/work/STZHONGS.TTF)

2.利用windows自带的字体，在你的电脑文件路径 C:\Windows\Fonts 中，复制一款你想要的字体到项目中即可。
#### 运行时的字体问题：
1.词云字体问题

首先，我们已经找到了上面的字体文件。然后添加以下代码给词云配置字体路径，即font_path

```python
wc = wordcloud.WordCloud(
    font_path= './work/STZHONGS.TTF',  # 设置字体格式
    background_color="#ffffff",  # 设置背景图
    max_words=150,  # 最多显示词数
    max_font_size=120,  # 字体最大值
    width=707,
    height=499
)
```
1.paddle环境中plt字体问题

paddle中的matplotlib字体不能显示中文

这里利用修改matplotlib字体配置路径修改字体

配合使用
```python
# 引入自定义字体包
import matplotlib.font_manager as fm  

# 设置字体---myfont
myfont = fm.FontProperties(fname=r'./work/STZHONGS.TTF') 

# plot时设置字体属性---myfont
plt.figure(figsize=(10, 6))
plt.xlabel("播出日期",fontsize=10,fontproperties=myfont) 
plt.ylabel("收视率%",fontsize=20,fontproperties=myfont) 
plt.show()
```

