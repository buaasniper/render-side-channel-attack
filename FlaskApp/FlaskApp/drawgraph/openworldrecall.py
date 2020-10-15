import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 100
x = np.random.normal(mu, sigma, size=100)
combined = np.fromstring('0.7692307692307693, 0.8695652173913043, 0.4117647058823529, 0.8, 1.0, 0.75, 0.6428571428571429, 0.9166666666666666, 0.8235294117647058, 0.7647058823529411, 0.7142857142857143, 0.7222222222222222, 0.8823529411764706, 0.7333333333333333, 0.3333333333333333, 0.5384615384615384, 0.5384615384615384, 0.8181818181818182, 0.44, 0.7916666666666666, 0.6923076923076923, 0.9285714285714286, 0.5, 0.7083333333333334, 0.7083333333333334, 0.9444444444444444, 0.8333333333333334, 1.0, 0.9090909090909091, 0.52, 0.8666666666666667, 0.7333333333333333, 0.375, 0.5806451612903226, 0.6923076923076923, 0.6551724137931034, 0.7142857142857143, 0.7272727272727273, 0.5882352941176471, 0.72, 0.8, 0.75, 0.35, 0.7857142857142857, 0.5555555555555556, 0.8421052631578947, 0.631578947368421, 0.7857142857142857, 0.8823529411764706, 0.8235294117647058, 1.0, 0.6428571428571429, 0.8125, 0.68, 0.47058823529411764, 0.5833333333333334, 0.7272727272727273, 0.6666666666666666, 0.4375, 0.7058823529411765, 0.8333333333333334, 0.875, 0.7, 0.4782608695652174, 0.47619047619047616, 0.9090909090909091, 0.65, 0.875, 0.6666666666666666, 0.6, 0.8, 1.0, 0.7272727272727273, 1.0, 0.8, 0.631578947368421, 1.0, 0.6875, 0.7, 0.55, 0.6428571428571429, 0.7894736842105263, 0.2, 0.5294117647058824, 0.6, 0.7619047619047619, 0.4444444444444444, 0.6666666666666666, 0.5909090909090909, 0.5555555555555556, 0.6666666666666666, 0.6, 0.8125, 0.5, 0.47058823529411764, 0.5333333333333333, 0.8095238095238095, 0.7857142857142857, 0.7142857142857143, 0.8888888888888888', dtype=float, sep=',')
cache = np.fromstring('0.6428571428571429, 0.7647058823529411, 0.4, 0.47368421052631576, 0.95, 0.6428571428571429, 0.6842105263157895, 0.7777777777777778, 0.7142857142857143, 0.8181818181818182, 0.625, 0.48, 0.8823529411764706, 0.8333333333333334, 0.2857142857142857, 0.5294117647058824, 0.375, 0.5294117647058824, 0.29411764705882354, 0.75, 0.8571428571428571, 0.8823529411764706, 0.47058823529411764, 0.7083333333333334, 0.6666666666666666, 0.8695652173913043, 0.76, 0.7142857142857143, 0.75, 0.6428571428571429, 0.7647058823529411, 0.8, 0.3333333333333333, 0.6333333333333333, 0.375, 0.8095238095238095, 0.11764705882352941, 0.27586206896551724, 0.14285714285714285, 0.75, 0.8333333333333334, 0.47619047619047616, 0.34782608695652173, 0.8461538461538461, 0.7692307692307693, 0.8888888888888888, 0.9166666666666666, 0.8181818181818182, 0.9411764705882353, 0.8235294117647058, 1.0, 0.8571428571428571, 0.875, 0.75, 0.5625, 0.6842105263157895, 0.5555555555555556, 0.4666666666666667, 0.19230769230769232, 0.6521739130434783, 0.8571428571428571, 1.0, 0.8, 0.6666666666666666, 0.6428571428571429, 0.6923076923076923, 0.46153846153846156, 0.9375, 0.8333333333333334, 0.38461538461538464, 0.7272727272727273, 0.8888888888888888, 0.6, 0.9285714285714286, 0.5789473684210527, 0.6190476190476191, 0.7857142857142857, 0.65, 0.4482758620689655, 0.4444444444444444, 0.4, 0.75, 0.0, 0.4666666666666667, 0.35, 0.7619047619047619, 0.5555555555555556, 0.6428571428571429, 0.38235294117647056, 0.47619047619047616, 0.8235294117647058, 0.5652173913043478, 0.6666666666666666, 0.25, 0.43478260869565216, 0.4444444444444444, 0.7619047619047619, 0.8461538461538461, 0.9285714285714286, 0.9411764705882353', dtype=float, sep=',')
rendering = np.fromstring('0.8333333333333334, 0.6666666666666666, 0.3333333333333333, 0.6363636363636364, 0.9523809523809523, 0.7, 0.8666666666666667, 0.7777777777777778, 0.9375, 0.631578947368421, 0.7222222222222222, 0.8, 0.8823529411764706, 0.6111111111111112, 0.5, 0.44, 0.5, 0.5555555555555556, 0.5555555555555556, 0.8, 0.5294117647058824, 0.8823529411764706, 0.625, 0.782608695652174, 0.7272727272727273, 0.95, 0.7407407407407407, 0.9090909090909091, 0.9090909090909091, 0.5454545454545454, 0.6818181818181818, 0.875, 0.5, 0.72, 0.6666666666666666, 0.8260869565217391, 0.16666666666666666, 0.45454545454545453, 0.46153846153846156, 0.8181818181818182, 0.5, 0.6875, 0.7, 0.7692307692307693, 0.7692307692307693, 0.7727272727272727, 0.5238095238095238, 0.8333333333333334, 0.9411764705882353, 0.9285714285714286, 1.0, 0.5882352941176471, 0.8, 0.8095238095238095, 0.5, 0.75, 0.75, 0.5, 0.23333333333333334, 0.72, 0.8333333333333334, 1.0, 0.6428571428571429, 0.6923076923076923, 0.8, 0.9230769230769231, 0.7222222222222222, 0.8125, 0.6666666666666666, 0.35294117647058826, 0.7272727272727273, 0.8888888888888888, 0.5, 0.9285714285714286, 0.75, 0.65, 0.8125, 0.4482758620689655, 0.7058823529411765, 0.6363636363636364, 0.5238095238095238, 0.6956521739130435, 0.14285714285714285, 0.625, 0.45, 0.7619047619047619, 0.6666666666666666, 0.9166666666666666, 0.52, 0.5882352941176471, 0.7142857142857143, 0.7333333333333333, 0.8666666666666667, 0.625, 0.6666666666666666, 0.5, 0.7916666666666666, 0.6470588235294118, 1.0, 0.8888888888888888', dtype=float, sep=',')
plt.rcParams.update({'font.size': 36})
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
ax.plot(p, rendering_sorted, label='Macroscale Rendering Channel', linestyle = '--', linewidth =5)

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
fig.text(0, 0.5, 'Recall', va='center', rotation='vertical',fontsize=40)

plt.show()
plt.savefig('openworldrecall.png')
plt.savefig('openworldrecall.eps',format='eps')