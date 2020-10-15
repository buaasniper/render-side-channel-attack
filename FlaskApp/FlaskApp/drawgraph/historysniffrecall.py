import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 100
x = np.random.normal(mu, sigma, size=100)
chrome = np.fromstring('0.65 0.5 0.7  1.   0.65 0.55 0.8  0.75 0.75 0.8  0.85 0.6  0.6  0.65 0.7  0.7  0.95 0.6  0.55 1.   0.6  0.7  0.95 0.9  0.7  0.6  0.55 0.7 0.55 0.85 0.75 0.55 0.55 0.6  0.7  0.8  0.6  0.75 0.9  0.55 0.55 0.8 0.7  0.7  0.95 0.7  0.75 0.6  0.55 0.55 0.55 1.   0.7  0.7  0.6  1. 0.65 0.85 0.7  0.65 0.7  0.95 0.55 0.7  0.55 0.55 0.85 0.9  0.6  0.85 0.65 0.6  0.55 0.55 0.6  0.8  0.75 0.6  0.65 0.65 0.55 0.65 0.95 0.85 0.9  0.55 0.6  0.8  0.9  0.75 0.55 0.9  0.95 0.8  1.   0.9  0.8  0.9 0.55 0.55', dtype=float, sep=' ')
firefox = np.fromstring('0.6  0.75 0.8  0.45  0.75 0.6  0.6  0.9  0.55 0.9  0.75 0.6  0.75 0.6 1.   0.55 0.85 0.95 0.55 0.6  0.9  1.   0.6  0.85 0.75 0.55 0.85 0.55 0.6  0.8  0.65 0.6  0.9  0.95 0.9  0.95 0.75 1.   1.   0.8  1.   0.65 0.85 0.95 0.65 0.55 0.65 0.6  0.65 0.85 0.55 0.7  0.9  0.95 0.7  0.55 0.7  0.85 0.95 0.6  0.8  1.   0.6  0.95 0.85 0.85 0.95 0.75 0.85 0.55 0.75 0.9  0.6  0.6  0.65 0.6  0.9  1.   0.75 0.7  0.65 0.65 0.7  0.9 0.85 0.65 0.95 0.55 0.7  0.8  0.6  0.65 0.6  0.7  0.75 1.   0.8  0.85 0.7  1.  ', dtype=float, sep=' ')
safari = np.fromstring('0.85 0.8  0.85 0.95 0.85 0.50 1.   0.8  0.85 0.85 0.85 0.55 1.   0.75 0.6  0.65 0.8  0.6  0.7  0.85 0.95 0.95 0.95 1.   0.95 0.9  0.55 0.95 0.85 0.55 1.   1.   0.55 0.6  1.   0.8  0.85 0.9  0.8  0.7  0.8  0.75 0.55 1.   0.7  0.55 0.7  0.65 1.   0.8  1.   0.7  0.95 0.75 0.9  0.8 0.6  0.6  0.85 0.75 0.95 0.85 0.6  0.9  1.   0.65 0.6  1.   0.75 0.55 0.75 1.   0.85 1.   0.8  0.9  0.75 0.8  0.85 0.7  0.65 0.65 0.7  0.8 1.   0.6  0.6  0.7  0.7  0.75 0.65 0.55 1.   0.75 0.75 1.   0.9  0.6 0.85 0.55', dtype=float, sep=' ')
plt.rcParams.update({'font.size': 26})
fig, ax = plt.subplots(figsize=(11, 10))
print(len(safari))
ax.set_ylim(0.44, 1)
ax.set_xlim(0, 1)


vals = ax.get_xticks()
ax.set_xticklabels(['{:,.0%}'.format(x) for x in vals])

chrome_sorted = np.sort(chrome)
p = 1. * np.arange(len(chrome)) / (len(chrome) - 1)
ax.plot(p, chrome_sorted, label='Chrome', linestyle = '-.', linewidth = 5)


firefox_sorted = np.sort(firefox)
p = 1. * np.arange(len(firefox)) / (len(firefox) - 1)
ax.plot(p, firefox_sorted, label='Firefox', linestyle = '--', linewidth = 5)

safari_sorted = np.sort(safari)
p = 1. * np.arange(len(safari)) / (len(safari) - 1)
ax.plot(p, safari_sorted, label='Safari', linestyle = ':', linewidth = 5)

# plot the cumulative histogram
# n, bins, patches = ax.hist(chrome, n_bins, density=True, histtype='step',
#                            cumulative=-1, label='Chrome', linestyle = '-.', linewidth = 3)


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
ax.legend(loc='upper left')
# ax.set_title('Cumulative step histograms')
# ax.set_ylabel('Percenatge')
# ax.set_xlabel('Recall')

fig.text(0.5, 0.02, 'Percenatge', ha='center',fontsize=30)
fig.text(0, 0.5, 'Recall', va='center', rotation='vertical',fontsize=30)

plt.show()
plt.savefig('historysniffrecall.png')
plt.savefig('historysniffrecall.eps',format='eps')