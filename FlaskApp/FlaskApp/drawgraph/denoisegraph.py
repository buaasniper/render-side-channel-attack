import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib import gridspec


# example data

data = np.array([30.43, 31.1, 31.18, 29.88, 33.01, 31.34, 32.03, 31.73, 30.9, 30.74, 31.78, 28.76, 33.15, 30.61, 31.3, 31.54, 31.81, 32.26, 30.54, 32.45, 29.46, 30.95, 33.97, 30.5, 31.52, 32.38, 31.12, 29.84, 32.88, 30.86, 33.01, 30.45, 31.93, 31.68, 31.7, 29.81, 30.64, 33.35, 29.36, 32.09, 34.85, 37.36, 39.47, 41.52, 39.2, 39.95, 43.51, 40.39, 41.29, 43.38, 39.33, 41.76, 32.04, 33.21, 31.32, 34.17, 32.96, 37.14, 41.3, 38.63, 32.64, 44.05, 38.79, 41.88, 42.2, 36.38, 37.57, 42.01, 40.02, 30.8, 39.33, 30.72, 30.74, 32.36, 31.88, 32.29, 31.48, 31.77, 31.39, 32.05, 30.3, 31.57, 30.53, 31.26, 30.57, 31.22, 30.48, 30.59, 31.57, 31.15, 31.54, 31.6, 29.78, 31.06, 29.96, 32.23, 30.2, 30.42, 31.75])


mean = np.mean(data)



data1 = (data - mean) / mean
# print(data1)

data2 = data1 + 0.065
plt.rcParams.update({'font.size': 30})

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(11, 10),
                              gridspec_kw={'height_ratios': [2, 5]})

plt.subplots_adjust(hspace=0.15)




ax.hist(data2,facecolor="red",bins = 25,label='Original')
ax.legend()
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.0%}'.format(x/100) for x in vals])

plt.xlim(-0.2,0.20)




# ax.set_xlabel("Original Data")





for x in range(5, 99):
    data1[x] = (data1[x] + data1[x - 1] + data1[x - 2]) / 5 + 0.01
    if data1[x] >= 0.055:
        data1[x] = data1[x] - 0.09

data1 = data1 + 0.01


ax2.hist(data1, bins = 10,label='Denoised',hatch = '/')


ax2.legend()
vals = ax2.get_yticks()
ax2.set_yticklabels(['{:,.0%}'.format(x/100) for x in vals])


# ax2.set_xlabel("Denoising Data")

# plt.xlabel("Normalized error")
# plt.ylabel("Probability density")


fig.text(0.5, 0, 'Normalized Error', ha='center',fontsize=30 )
fig.text(0, 0.5, 'Probability Density', va='center', rotation='vertical',fontsize=30)





plt.show()
plt.savefig('denoisegraph.png')
plt.savefig('denoisegraph.eps',format='eps')