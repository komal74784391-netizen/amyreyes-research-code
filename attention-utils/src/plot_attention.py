import matplotlib.pyplot as plt


def plot_map(matrix, path):
    plt.imshow(matrix)
    plt.savefig(path)
