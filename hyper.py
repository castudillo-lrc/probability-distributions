from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np
[M, n, N] = [52, 5,26]
rv = hypergeom(M, n, N)
x = np.arange(0, n + 1)
pmf_dogs = rv.pmf(x)
print(sum(pmf_dogs))
print(x)
print(pmf_dogs)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, pmf_dogs, 'bo')
ax.vlines(x, 0, pmf_dogs, lw=2)
ax.set_xlabel('# of dogs in our group of chosen animals')
ax.set_ylabel('hypergeom PMF')
plt.show()