import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 100
x = np.random.normal(mu, sigma, size=100)
chrome = np.fromstring('0.56521739 0.84615385 0.455        0.66666667 0.68421053 0.49 0.61538462 0.6        0.65217391 0.66666667 0.65384615 0.6 0.8        0.59090909 0.7        0.58333333 0.7037037  0.8 0.52380952 0.86956522 1.         0.77777778 0.82608696 0.94736842 0.73684211 0.70588235 0.6875     1.         0.6875     0.70833333 0.78947368 1.         0.64705882 1.         0.7        0.8 0.85714286 0.88235294 0.69230769 0.84615385 0.55       0.69565217 0.77777778 0.7        0.67857143 0.73684211 0.75       0.8 0.57894737 0.6875     0.78571429 0.86956522 0.7        0.77777778 0.75       0.86956522 0.56521739 0.73913043 1.         1. 0.58333333 0.7037037  0.64705882 0.77777778 0.52380952 0.55 0.89473684 0.7826087  0.66666667 0.89473684 0.92857143 0.92307692 1.         0.6875     0.85714286 1.         0.88235294 1. 0.65       0.86666667 0.73333333 0.68421053 0.95       1. 0.69230769 0.52380952 0.63157895 1.         0.75       0.71428571 0.64705882 0.72       0.95       0.72727273 0.90909091 0.94736842 0.88888889 0.75       0.78571429 0.64705882', dtype=float, sep=' ')
firefox = np.fromstring('0.6        0.71428571 0.88888889 0.85714286 0.75       0.70588235 0.57142857 0.7826087  0.84615385 0.81818182 0.625      0.57142857 0.88235294 0.57142857 1.         0.52380952 0.62962963 0.7037037 1.         0.54545455 0.81818182 0.83333333 0.57142857 0.77272727 0.6        0.61111111 0.94444444 0.57894737 0.66666667 0.94117647 0.92857143 0.92307692 0.69230769 0.82608696 0.75       0.67857143 0.625      0.8        0.83333333 0.8        0.68965517 0.86666667 0.94444444 0.79166667 0.86666667 0.64705882 1.         0.66666667 0.61904762 0.94444444 0.84615385 0.63636364 0.94736842 0.7037037 0.60869565 0.73333333 0.875      0.85       0.9047619  0.92307692 0.66666667 0.90909091 0.63157895 1.         0.80952381 0.94444444 0.82608696 0.71428571 0.68       0.55       0.75       0.94736842 0.57142857 0.6        0.8125     0.92307692 1.         0.74074074 0.6        0.93333333 0.92857143 0.76470588 0.875      0.75 0.73913043 0.86666667 0.82608696 0.78571429 0.60869565 0.88888889 0.70588235 1.         0.75       0.58333333 0.75       0.95238095 0.72727273 0.73913043 0.875      1. ', dtype=float, sep=' ')
safari = np.fromstring('0.80952381 0.48 0.62962963 0.73076923 0.62962963 0.64705882 0.66666667 0.61538462 1.         0.89473684 0.62962963 0.6875 0.83333333 1.         1.         0.86666667 0.64       0.66666667 0.73684211 0.65384615 0.86363636 0.79166667 0.67857143 0.76923077 0.73076923 0.69230769 0.55       0.7037037  0.65384615 0.57894737 0.71428571 0.76923077 0.52380952 1.         0.66666667 0.69565217 0.77272727 1.         0.72727273 0.82352941 0.94117647 0.6 0.73333333 0.90909091 0.93333333 0.6875     0.77777778 0.56521739 0.83333333 0.61538462 0.95238095 0.77777778 0.73076923 0.71428571 0.66666667 0.94117647 0.63157895 0.6        0.62962963 0.71428571 0.76       0.65384615 0.85714286 0.81818182 0.8        0.59090909 0.70588235 0.66666667 0.83333333 0.61111111 0.75       0.68965517 0.62962963 0.74074074 0.66666667 0.69230769 0.75       0.8 0.70833333 0.875      0.61904762 0.59090909 0.7        0.61538462 0.76923077 0.8        1.         0.60869565 0.82352941 0.83333333 0.56521739 0.57894737 0.68965517 0.68181818 0.78947368 0.74074074 0.75       0.70588235 0.94444444 0.78571429', dtype=float, sep=' ')
plt.rcParams.update({'font.size': 26})
fig, ax = plt.subplots(figsize=(11, 10))
print(len(safari))
ax.set_ylim(0.45, 1)
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
# ax.set_xlabel('Precision')

fig.text(0.5, 0.02, 'Percenatge', ha='center',fontsize=30)
fig.text(0, 0.5, 'Precision', va='center', rotation='vertical',fontsize=30)

plt.show()
plt.savefig('historysniffprecesion.png')
plt.savefig('historysniffprecesion.eps',format='eps')