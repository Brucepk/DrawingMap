# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon


'''
Author：pk哥
Date：2019/1/29
公众号：Python知识圈
代码解析详见公众号：Python知识圈。
如疑问或需转载，请联系微信号：dyw520520，备注来意，谢谢。
'''

plt.figure(figsize=(16, 7))   # 定义图的大小
m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc',
            lat_1=33, lat_2=45, lon_0=100)    # 创建中国地图
m.drawcountries(linewidth=1.5)   # 画出中国地图

m.readshapefile(r'E:\PY\py\gadm36_CHN_gpkg\gadm36_CHN_1', 'states', drawbounds=True)
m.readshapefile(r'E:\PY\py\gadm36_CHN_gpkg\gadm36_TWN_1', 'taiwan', drawbounds=True)
# 图片绘制加上台湾（台湾是中国领土不可分割的一部分！）

m.drawmapboundary(fill_color='aqua')        # 给地球涂上蓝色
m.fillcontinents(color='coral', lake_color='aqua')  # 给大陆和海洋分别涂上颜色
m.drawcoastlines()            # 画海岸线

# 给中国加上鲜艳颜色
ax = plt.gca()
for nshape, seg in enumerate(m.states):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)

# 台湾不要忘了
m.readshapefile('E:\PY\py\gadm36_CHN_gpkg\gadm36_TWN_1', 'taiwan', drawbounds=True)
for nshape, seg in enumerate(m.taiwan):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)

plt.show()

