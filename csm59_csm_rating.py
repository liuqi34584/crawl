import matplotlib.pyplot as plt
import numpy as np 
import json
import matplotlib.font_manager as font_manager
import pandas as pd
#显示matplotlib生成的图形
%matplotlib inline


df = pd.read_json('work/viewing_infos.json',dtype = {'broadcastDate' : str})
#print(df)

broadcastDate_list = df['broadcastDate']
csm59_rating_list = df['csm59_rating']
csm_rating_list = df['csm_rating']

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.figure(figsize=(15,8))
plt.title("《隐秘而伟大》收视率变化趋势",fontsize=20) 
plt.xlabel("播出日期",fontsize=20) 
plt.ylabel("收视率%",fontsize=20) 
plt.xticks(rotation=45,fontsize=20)
plt.yticks(fontsize=20)
plt.plot(broadcastDate_list,csm59_rating_list,label = "CSM59城市网收视率") 
plt.plot(broadcastDate_list,csm_rating_list,label = "CSM全国网收视率") 
plt.legend()
plt.grid() 
plt.savefig('/home/aistudio/work/chart02.jpg')
plt.show()