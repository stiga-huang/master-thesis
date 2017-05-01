#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   注释
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

N = 3
raw = (33.88, 88.508, 202.486)
scopa = (7.328, 14.966, 20.544)

ind = np.arange(N)  # the x locations for the groups
data_set_width = 0.35       # the width of the bars
rect_width = data_set_width * 0.8

fig, ax = plt.subplots()
rects1 = ax.bar(ind + rect_width, raw, rect_width, color='b', alpha = 0.4, edgecolor='black', hatch='xx')
rects2 = ax.bar(ind + rect_width * 2, scopa, rect_width, color='g', alpha = 0.4, edgecolor='black', hatch='//')

ubuntu_zh_font='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
#times_font='C:\Windows\Fonts\times.ttf'
simsun_font='E:\share\py_graphs\SimSun.ttf'

zhfont = mpl.font_manager.FontProperties(fname=simsun_font, size=24)
zhfont22 = mpl.font_manager.FontProperties(fname=simsun_font, size=22)

# add some text for labels, title and axes ticks
ax.set_ylabel('Time per Vertex(ms)', fontproperties=zhfont)
#ax.set_xlabel('Datasets')
#ax.set_title(u'LocalCC calculattion performance', fontproperties=zhfont)

ax.set_xticks(ind + rect_width * 2)
ax.set_xticklabels((u'小邻域点集', u'随机点集', u'大邻域点集'), fontproperties=zhfont)

#data_set_height = -550
#ax.text(rect_width, data_set_height, u'小邻域点集', fontproperties=zhfont)
#ax.text(1 + rect_width * 1.2, data_set_height, u'随机点集', fontproperties=zhfont)
#ax.text(2 + rect_width, data_set_height, u'大邻域点集', fontproperties=zhfont)

ax.legend((rects1[0], rects2[0]), ('Titan', 'HybriG'), prop=zhfont)
plt.ylim(ymax=270)
plt.yticks(fontproperties=zhfont22)
plt.xlim(xmax=N+rect_width)

leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize=24)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 5 +  height+rect.get_y(),
                '%d' % int(rect.get_y() + height),
                ha='center', va='bottom', fontproperties=zhfont22)

autolabel(rects1)
autolabel(rects2)

#plt.savefig('abc.pdf')
plt.show()

