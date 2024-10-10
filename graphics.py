#!/usr/bin/env python3
from matplotlib import pyplot as plt


def plot_barchart(data: dict, xlab: str, ylab: str, title: str, ticfntsz=15) -> None:
    """
    Plot a barchart based on data from a dictionary.

    This function creates a bar chart plot based on
    the data from the dictionary parameter. The labels of the plot
    must be set with the parameter xlabx (x-axis), ylab (y-axis) and
    title.

    :param data: Dictionary with the data to be plotted.
    :param xlab: Label for x-axis for the plot.
    :param ylab: Label for y-axis for the plot.
    :param title: Title for the plot.
    :param ticfntsz: Font size of the tic. Default value 15.
    :return: None.
    """
    # Set figure size.
    plt.figure(figsize=(20, 10))

    # Set tick label size.
    plt.tick_params(labelsize=ticfntsz)

    # Set plot data.
    plt.bar(data.keys(), data.values(), color='blue')

    # Customize the labels.
    plt.xlabel(xlab, fontsize=20, color='purple')
    plt.xticks(rotation=60)
    plt.ylabel(ylab, fontsize=20, color='purple')
    plt.title(title, fontsize=25, color='blue')

    # Set grid.
    plt.grid(True)

    # Plot.
    plt.show()


def plot_graph(data: dict, xlab: str, ylab: str, title: str, ticfntsz=15) -> None:
    """
    Plot a line graph based on data from a dictionary.

    This function creates a line graph plot based on
    the data from the dictionary parameter. The labels of the plot
    must be set with the parameter xlabx (x-axis), ylab (y-axis) and
    title.

    :param data: Dictionary with the data to be plotted.
    :param xlab: Label for x-axis for the plot.
    :param ylab: Label for y-axis for the plot.
    :param title: Title for the plot.
    :param ticfntsz: Font size of the tic. Default value 15.
    :return: None.
    """
    # Set figure size.
    plt.figure(figsize=(20, 10))

    # Set tick label size.
    plt.tick_params(labelsize=ticfntsz)

    # Set plot data.
    plt.plot(data.keys(), data.values(), color='red')

    # Customize the labels.
    plt.xlabel(xlab, fontsize=20, color='purple')
    plt.ylabel(ylab, fontsize=20, color='purple')
    plt.title(title, fontsize=25, color='blue')

    # Set grid.
    plt.grid(True)

    # Plot.
    plt.show()
