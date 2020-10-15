import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 100
x = np.random.normal(mu, sigma, size=100)
chrome = np.fromstring('0.60465116 0.66666667 0.7        0.8        0.66666667 0.502 0.69565217 0.66666667 0.69767442 0.72727273 0.73913043 0.6 0.68571429 0.61904762 0.7        0.63636364 0.80851064 0.68571429 0.53658537 0.93023256 0.75       0.73684211 0.88372093 0.92307692 0.71794872 0.64864865 0.61111111 0.82352941 0.61111111 0.77272727 0.76923077 0.70967742 0.59459459 0.75       0.7        0.8 0.70588235 0.81081081 0.7826087  0.66666667 0.55       0.74418605 0.73684211 0.7        0.79166667 0.71794872 0.75       0.68571429 0.56410256 0.61111111 0.64705882 0.93023256 0.7        0.73684211 0.66666667 0.93023256 0.60465116 0.79069767 0.82352941 0.78787879 0.63636364 0.80851064 0.59459459 0.73684211 0.53658537 0.55 0.87179487 0.8372093  0.63157895 0.87179487 0.76470588 0.72727273 0.70967742 0.61111111 0.70588235 0.88888889 0.81081081 0.75 0.65       0.74285714 0.62857143 0.66666667 0.95       0.91891892 0.7826087  0.53658537 0.61538462 0.88888889 0.81818182 0.73170732 0.59459459 0.8        0.95       0.76190476 0.95238095 0.92307692 0.84210526 0.81818182 0.64705882 0.59459459', dtype=float, sep=' ')
firefox = np.fromstring('0.49        0.73170732 0.84210526 0.87804878 0.75       0.64864865 0.58536585 0.8372093  0.66666667 0.85714286 0.68181818 0.58536585 0.81081081 0.58536585 1.         0.53658537 0.72340426 0.80851064 0.70967742 0.57142857 0.85714286 0.90909091 0.58536585 0.80952381 0.66666667 0.57894737 0.89473684 0.56410256 0.63157895 0.86486486 0.76470588 0.72727273 0.7826087  0.88372093 0.81818182 0.79166667 0.68181818 0.88888889 0.90909091 0.8        0.81632653 0.74285714 0.89473684 0.86363636 0.74285714 0.59459459 0.78787879 0.63157895 0.63414634 0.89473684 0.66666667 0.66666667 0.92307692 0.80851064 0.65116279 0.62857143 0.77777778 0.85       0.92682927 0.72727273 0.72727273 0.95238095 0.61538462 0.97435897 0.82926829 0.89473684 0.88372093 0.73170732 0.75555556 0.55       0.75       0.92307692 0.58536585 0.6        0.72222222 0.72727273 0.94736842 0.85106383 0.66666667 0.8        0.76470588 0.7027027  0.77777778 0.81818182 0.79069767 0.74285714 0.88372093 0.64705882 0.65116279 0.84210526 0.64864865 0.78787879 0.66666667 0.63636364 0.75       0.97560976 0.76190476 0.79069767 0.77777778 1. ', dtype=float, sep=' ')
safari = np.fromstring('0.82926829 0.69565217 0.72340426 0.82608696 0.72340426 0.59459459 0.8        0.69565217 0.91891892 0.87179487 0.72340426 0.61111111 0.90909091 0.85714286 0.75       0.74285714 0.71111111 0.63157895 0.71794872 0.73913043 0.9047619  0.86363636 0.79166667 0.86956522 0.82608696 0.7826087  0.55       0.80851064 0.73913043 0.56410256 0.83333333 0.86956522 0.53658537 0.75       0.8        0.74418605 0.80952381 0.94736842 0.76190476 0.75675676 0.86486486 0.66666667 0.62857143 0.95238095 0.8        0.61111111 0.73684211 0.60465116 0.90909091 0.69565217 0.97560976 0.73684211 0.82608696 0.73170732 0.76595745 0.86486486 0.61538462 0.6        0.72340426 0.73170732 0.84444444 0.73913043 0.70588235 0.85714286 0.88888889 0.61904762  0.64864865 0.8        0.78947368 0.57894737 0.75       0.81632653 0.72340426 0.85106383 0.72727273 0.7826087  0.75       0.8 0.77272727 0.77777778 0.63414634 0.61904762 0.7        0.69565217 0.86956522 0.68571429 0.75       0.65116279 0.75675676 0.78947368 0.60465116 0.56410256 0.81632653 0.71428571 0.76923077 0.85106383 0.81818182 0.64864865 0.89473684 0.64705882', dtype=float, sep=' ')
plt.rcParams.update({'font.size': 26})
fig, ax = plt.subplots(figsize=(11, 10))
print("median of arr : ", np.median(chrome)) 
print("median of arr : ", np.median(firefox)) 
print("median of arr : ", np.median(safari)) 


ax.set_ylim(0.48, 1)
ax.set_xlim(0, 1)

vals = ax.get_xticks()
ax.set_xticklabels(['{:,.0%}'.format(x) for x in vals])

# plot the cumulative histogram
# n, bins, patches = ax.hist(chrome, n_bins, density=True, histtype='step',
#                            cumulative=-1, label='Chrome', linestyle = '-.', linewidth = 3)
chrome_sorted = np.sort(chrome)
p = 1. * np.arange(len(chrome)) / (len(chrome) - 1)
ax.plot(p, chrome_sorted, label='Chrome', linestyle = '-.', linewidth = 5)


firefox_sorted = np.sort(firefox)
p = 1. * np.arange(len(firefox)) / (len(firefox) - 1)
ax.plot(p, firefox_sorted, label='Firefox', linestyle = '--', linewidth = 5)

safari_sorted = np.sort(safari)
p = 1. * np.arange(len(safari)) / (len(safari) - 1)
ax.plot(p, safari_sorted, label='Safari', linestyle = ':', linewidth = 5)

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
ax.legend(loc='upper left')
# ax.set_title('Cumulative step histograms')
# ax.set_ylabel('Percenatge')
# ax.set_xlabel('')

fig.text(0.5, 0.02, 'Percenatge', ha='center',fontsize=30)
fig.text(0, 0.5, 'F1 Score', va='center', rotation='vertical',fontsize=30)

plt.show()
plt.savefig('historysnifff1.png')
plt.savefig('historysnifff1.eps',format='eps')