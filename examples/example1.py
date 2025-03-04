from svg_sampler import sample_from_svg
from matplotlib import pyplot as plt

X, y = sample_from_svg("test.svg", 5000, normalize=True, sample_setting="based_on_area", overlap_mode="upper_only")
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
