import matplotlib
import matplotlib.pyplot as plt
import numpy as np




labels = ['0', '1', '2', '3', '4']
Ori = [50, 10, 20, 15, 5]
den = [80, 15, 5,0, 0]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
plt.rcParams.update({'font.size': 30})
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(11,10),
                              gridspec_kw={'height_ratios': [5, 8]})

rects1 = ax.bar(x , Ori, width,facecolor="red", label='Original')
rects2 = ax2.bar(x , den, width,hatch = '/', label='Denoised')

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Percenatge')
# ax.set_xlabel('Number of Frames')
ax.legend()
ax2.legend()

ax.set_ylim(0, 50)
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.0%}'.format(x/100) for x in vals])

vals = ax2.get_yticks()
ax2.set_yticklabels(['{:,.0%}'.format(x/100) for x in vals])

fig.text(0.5, 0, 'Number of Frames', ha='center',fontsize=30)
fig.text(0, 0.5, 'Percenatge', va='center', rotation='vertical',fontsize=30)

plt.show()
plt.savefig('highvaluenoise.png')
plt.savefig('highvaluenoise.eps',format='eps')

