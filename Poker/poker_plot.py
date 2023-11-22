from matplotlib import pyplot as plt


def poker_plot(combinations):
    names = list(combinations.keys())
    values = list(combinations.values())
    plt.bar(range(len(combinations)), values, tick_label=names)
    plt.show()
