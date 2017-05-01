#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   注释
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

N = 3
#raw = (1145.8, 2019.2, 3661.8)
#scopa_titan = (229.2, 287.8, 354.8)
#scopa_hbase = (617.4, 1563, 3260.8)
raw = (6210.641667, 15968.90833, 33096.03333)
scopa_titan = (1780.716667, 1929.416667, 2121.175)
scopa_hbase = (4775.433333, 12712.475, 26406.325)

raw_yerr = (251.1243605, 582.0756793, 71.07645649)
scopa_titan_yerr = (41.50653764, 82.28527005, 11.09268903)
scopa_hbase_yerr = (172.5400002, 837.7412439, 96.20914588)
scopa_yerr = (207.146902, 919.8561303, 103.9923459)

ind = np.arange(N)  # the x locations for the groups
data_set_width = 0.35       # the width of the bars
rect_width = data_set_width * 0.8

fig, ax = plt.subplots()
rects1 = ax.bar(ind + rect_width, raw, rect_width, #yerr=raw_yerr,
        color='b', alpha = 0.4, edgecolor='black', hatch='x')
rects2 = ax.bar(ind + rect_width * 2, scopa_titan, rect_width, #yerr=scopa_titan_yerr,
        color='b', alpha = 0.4, edgecolor='black', hatch='x')
rects3 = ax.bar(ind + rect_width * 2, scopa_hbase, rect_width, bottom=scopa_titan, #yerr = scopa_yerr,
        color='g', alpha = 0.4, edgecolor='black', hatch='/')

ubuntu_zh_font='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
#times_font='C:\Windows\Fonts\times.ttf'
simsun_font='E:\share\py_graphs\SimSun.ttf'

zhfont = mpl.font_manager.FontProperties(fname=simsun_font, size=24)
zhfont22 = mpl.font_manager.FontProperties(fname=simsun_font, size=22)

# add some text for labels, title and axes ticks
ax.set_ylabel('Total Time(ms)', fontproperties=zhfont)
#ax.set_xlabel('Datasets')
#ax.set_title('GetEdges query performance', fontproperties=zhfont)

ax.set_xticks(np.concatenate([ind + rect_width * 1, ind + rect_width * 2.05]))
ax.set_xticklabels(['Titan']*3 + ['HybriG']*3, fontproperties=zhfont)

data_set_height = -4000
ax.text(rect_width * 0.8, data_set_height, u'小邻域点集', fontproperties=zhfont)
ax.text(1 + rect_width * 1, data_set_height, u'随机点集', fontproperties=zhfont)
ax.text(2 + rect_width * 0.8, data_set_height, u'大邻域点集', fontproperties=zhfont)

ax.legend((rects1[0], rects3[0]), ('Titan', 'HBase'), prop=zhfont)
plt.ylim(ymax=45000)
plt.yticks(fontproperties=zhfont22)
plt.xlim(xmax=N+rect_width)

leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize=24)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 500+height+rect.get_y(),
                '%d' % int(rect.get_y() + height),
                ha='center', va='bottom', fontproperties=zhfont22)
def labelAtRight(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*1.1, height+rect.get_y(),
                '%d' % int(height),
                va='bottom', fontproperties=zhfont22)

autolabel(rects1)
autolabel(rects3)
labelAtRight(rects2)

#plt.savefig('abc.pdf')
plt.show()

