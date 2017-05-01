#!/usr/bin/python
# -*- coding: utf-8 -*- `
#

"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
 
#mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
#mpl.rcParams['ax.es.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#from matplotlib import rcParams
#rcParams['font.family'] = 'sans-serif'
#rcParams['font.sans-serif'] = ['Tahoma']
#rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei Mono']
#rcParams['font.sans-serif'] = ['AR PL UKai CN']

zhfont = mpl.font_manager.FontProperties(fname='C:\\Windows\Fonts\\times.ttf', size=18)

solution = (u'HybriG', u'Titan')
#y_pos = np.arange(len(solution))
y_pos = (0.3, 0.7)
titan = (465, 950)
#hbase = (0, 488)
 
#barh(bottom, width, height=0.8, left=0, **kwargs)
bar1 = plt.barh(y_pos, titan, height=0.2, align='center', hatch='xx', color='b', alpha = 0.4, edgecolor='black')
bar2 = plt.barh((0.3,), (474,), height=0.2, left=titan[0], align='center', hatch='//', color='g', alpha = 0.4, edgecolor='black')

plt.text(titan[0], 0.41, '%d' % titan[0], ha='center', fontproperties=zhfont)
plt.text(titan[1], 0.81, '%d' % titan[1], ha='center', fontproperties=zhfont)
plt.text(titan[0]+474, 0.41, '%d' % (titan[0]+474), ha='center', fontproperties=zhfont)

plt.yticks(y_pos, solution, fontproperties=zhfont)
plt.xticks(fontproperties=zhfont)
plt.ylim(ymax=1.2, ymin=0)
plt.xlabel('Total Time(ms)', fontproperties=zhfont)
#plt.title('Edge query performance', fontproperties=zhfont)
plt.legend((bar1[0], bar2[0]), ('Titan', 'HBase'), prop=zhfont)

#leg = plt.gca().get_legend()
#ltext  = leg.get_texts()
#plt.setp(ltext, fontsize=24)
 
plt.show()
#plt.savefig("edge_query_perf.pdf")
#plt.savefig("edge_query_perf.png")
#plt.savefig("edge_query_perf_1000dpi.png", dpi=1000)
