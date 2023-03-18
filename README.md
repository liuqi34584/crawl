# 机器学习爬取网页数据

## 本地编译遇到的问题
1. 通过external_libraries的库文件完成编译
   不建议这么做，paddle环境里的包存在文件缺失问题，在自己的conda环境里安装以下包：
   *  pip install jieba
   *  pip install wordcloud
   *  pip install bs4
   *  pip install lxml
  
2. 运行代码时偶尔find_all()函数报错
  办法：问题在于翻墙，如果以下网站能够访问，就不会报错，报错请先解决网络问题。[隐秘而伟大](https://baike.baidu.com/item/%E9%9A%90%E7%A7%98%E8%80%8C%E4%BC%9F%E5%A4%A7)
  

