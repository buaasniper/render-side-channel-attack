import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 100
x = np.random.normal(mu, sigma, size=100)
combined = np.fromstring('0.5882352941176471, 0.9090909090909091, 0.5, 0.4, 0.76, 0.6923076923076923, 0.5625, 0.55, 0.875, 0.8125, 0.6666666666666666, 0.8666666666666667, 1.0, 0.55, 0.36363636363636365, 0.3888888888888889, 0.3684210526315789, 0.5625, 0.5789473684210527, 0.9047619047619048, 0.6923076923076923, 0.8666666666666667, 0.8888888888888888, 0.8947368421052632, 0.8947368421052632, 0.85, 0.9090909090909091, 0.3333333333333333, 0.625, 0.8666666666666667, 0.8125, 0.6875, 0.42857142857142855, 0.75, 0.6, 0.8636363636363636, 0.3125, 0.5333333333333333, 0.43478260869565216, 0.9473684210526315, 0.4, 0.631578947368421, 0.5384615384615384, 0.6470588235294118, 0.6666666666666666, 0.8421052631578947, 0.631578947368421, 0.7333333333333333, 0.9375, 0.875, 0.9047619047619048, 0.6428571428571429, 0.7647058823529411, 0.8947368421052632, 0.4, 0.875, 0.8, 0.43478260869565216, 0.3888888888888889, 0.6666666666666666, 0.8333333333333334, 0.7, 0.7, 0.5789473684210527, 0.5, 0.6666666666666666, 0.6842105263157895, 0.8235294117647058, 0.7142857142857143, 0.5, 0.6666666666666666, 0.7272727272727273, 0.5333333333333333, 0.8461538461538461, 0.7058823529411765, 0.8571428571428571, 0.5, 0.7333333333333333, 0.5833333333333334, 0.6470588235294118, 0.6, 0.8333333333333334, 0.36363636363636365, 0.6923076923076923, 0.5625, 0.8, 0.38095238095238093, 0.7058823529411765, 0.7222222222222222, 0.7692307692307693, 0.75, 0.631578947368421, 0.9285714285714286, 0.75, 0.6666666666666666, 0.42105263157894735, 0.8947368421052632, 0.6875, 1.0, 1.0', dtype=float, sep=',')
cache = np.fromstring('0.5294117647058824, 0.5909090909090909, 0.42857142857142855, 0.45, 0.76, 0.6923076923076923, 0.8125, 0.35, 0.9375, 0.5625, 0.6666666666666666, 0.8, 1.0, 0.25, 0.36363636363636365, 0.5, 0.3157894736842105, 0.5625, 0.2631578947368421, 0.8571428571428571, 0.46153846153846156, 1.0, 0.4444444444444444, 0.8947368421052632, 0.9473684210526315, 1.0, 0.8636363636363636, 0.8333333333333334, 0.5625, 0.6, 0.8125, 0.75, 0.35714285714285715, 0.7916666666666666, 0.2, 0.7727272727272727, 0.125, 0.5333333333333333, 0.043478260869565216, 0.7894736842105263, 0.5, 0.5263157894736842, 0.6153846153846154, 0.6470588235294118, 0.6666666666666666, 0.8421052631578947, 0.5789473684210527, 0.6, 1.0, 0.875, 0.7619047619047619, 0.8571428571428571, 0.4117647058823529, 0.631578947368421, 0.45, 0.8125, 1.0, 0.30434782608695654, 0.2777777777777778, 0.8333333333333334, 0.6666666666666666, 0.6, 0.8, 0.3157894736842105, 0.45, 0.6, 0.631578947368421, 0.8823529411764706, 0.7142857142857143, 0.4166666666666667, 0.6666666666666666, 0.7272727272727273, 0.4, 1.0, 0.6470588235294118, 0.9285714285714286, 0.6875, 0.8666666666666667, 0.5416666666666666, 0.47058823529411764, 0.5333333333333333, 0.8333333333333334, 0.0, 0.5384615384615384, 0.4375, 0.8, 0.23809523809523808, 0.5294117647058824, 0.7222222222222222, 0.7692307692307693, 0.875, 0.6842105263157895, 1.0, 0.25, 0.8333333333333334, 0.42105263157894735, 0.8421052631578947, 0.6875, 0.8666666666666667, 1.0 ', dtype=float, sep=',')
rendering = np.fromstring('0.5882352941176471, 0.7272727272727273, 0.21428571428571427, 0.35, 0.8, 0.5384615384615384, 0.8125, 0.7, 0.9375, 0.75, 0.8666666666666667, 0.8, 1.0, 0.55, 0.36363636363636365, 0.6111111111111112, 0.42105263157894735, 0.625, 0.2631578947368421, 0.9523809523809523, 0.6923076923076923, 1.0, 0.8333333333333334, 0.9473684210526315, 0.8421052631578947, 0.95, 0.9090909090909091, 0.5555555555555556, 0.625, 0.8, 0.9375, 0.4375, 0.35714285714285715, 0.75, 0.4, 0.8636363636363636, 0.0625, 0.6666666666666666, 0.2608695652173913, 0.9473684210526315, 0.3, 0.5789473684210527, 0.5384615384615384, 0.5882352941176471, 0.6666666666666666, 0.8947368421052632, 0.5789473684210527, 0.6666666666666666, 1.0, 0.8125, 0.9047619047619048, 0.7142857142857143, 0.7058823529411765, 0.8947368421052632, 0.5, 0.75, 0.9, 0.34782608695652173, 0.3888888888888889, 1.0, 0.8333333333333334, 0.9, 0.9, 0.47368421052631576, 0.6, 0.8, 0.6842105263157895, 0.7647058823529411, 0.7142857142857143, 0.5, 0.6666666666666666, 0.7272727272727273, 0.6, 1.0, 0.5294117647058824, 0.9285714285714286, 0.8125, 0.8666666666666667, 0.5, 0.4117647058823529, 0.7333333333333333, 0.8888888888888888, 0.36363636363636365, 0.7692307692307693, 0.5625, 0.8, 0.47619047619047616, 0.6470588235294118, 0.7222222222222222, 0.7692307692307693, 0.625, 0.5789473684210527, 0.9285714285714286, 0.4166666666666667, 0.6666666666666666, 0.3684210526315789, 1.0, 0.6875, 1.0, 1.05', dtype=float, sep=',')
plt.rcParams.update({'font.size':36})
for i in range(len(combined)):
    if combined[i] < rendering[i]:
        combined[i] = rendering[i]
    if combined[i] < cache[i]:
        combined[i] = cache[i]
fig, ax = plt.subplots(figsize=(15, 12))
print("median of arr : ", np.median(combined)) 
print("median of arr : ", np.median(rendering)) 
print("median of arr : ", np.median(cache)) 


ax.set_ylim(0, 1)
ax.set_xlim(0, 1)

vals = ax.get_xticks()
ax.set_xticklabels(['{:,.0%}'.format(x) for x in vals])

# plot the cumulative histogram
# n, bins, patches = ax.hist(chrome, n_bins, density=True, histtype='step',
#                            cumulative=-1, label='Chrome', linestyle = '-.', linewidth = 3)
combined_sorted = np.sort(combined)
p = 1. * np.arange(len(combined)) / (len(combined) - 1)
ax.plot(p, combined_sorted, label='Combined', linestyle = '-.', linewidth = 5)


rendering_sorted = np.sort(rendering)
p = 1. * np.arange(len(rendering)) / (len(rendering) - 1)
ax.plot(p, rendering_sorted, label='Macroscale Rendering Channel', linestyle = '--', linewidth = 5)

cache_sorted = np.sort(cache)
p = 1. * np.arange(len(cache)) / (len(cache) - 1)
ax.plot(p, cache_sorted, label='Cache Occupancy Channel', linestyle = ':', linewidth = 5)

# # Add a line showing the expected distribution.
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# y = y.cumsum()
# y /= y[-1]

# ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')


# ax.hist(firefox, n_bins, density=True, histtype='step',
#                            cumulative=-1, label='Firefox', linestyle = '--', linewidth = 3)
# ax.hist(safari, n_bins, density=True, histtype='step',
#                            cumulative=-1, label='Safari',linestyle = ':', linewidth = 3)
# # Add a line showing the expected distribution.
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# y = y.cumsum()
# y /= y[-1]

# ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')

# Overlay a reversed cumulative histogram.
# ax.hist(x, bins=bins, density=True, histtype='step', cumulative=-1,
#         label='Reversed emp.')

# tidy up the figure
ax.grid(True)
ax.legend(loc='lower right')
# ax.set_title('Cumulative step histograms')
# ax.set_ylabel('Percenatge')
# ax.set_xlabel('')

fig.text(0.5, 0.02, 'Percenatge', ha='center',fontsize=40)
fig.text(0, 0.5, 'Precesion', va='center', rotation='vertical',fontsize=40)

plt.show()
plt.savefig('openworldprecesion.png')
plt.savefig('openworldprecesion.eps',format='eps')