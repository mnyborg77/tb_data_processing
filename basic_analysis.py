#!/usr/bin/env python3
from reading import read_tb_functions, read_tb_data
from utils import count_orf_clas, calc_protein_hydro
from utils import calc_relac_orfs, calc_multiple_m, show_orfcount_sw
from graphics import plot_barchart, plot_graph

if __name__ == "__main__":
    # READING FILES.
    # To read both `tb_functions.pl` and `tb_data_XX.txt` files we iterate
    # over the file object instead of using `.read()` or `readlines()` that
    # read the whole file into the memory. For the `tb_functions.pl` we store
    # every line of the file into two dictionaries, we need all of the data in
    # the exercises. For the `tb_data_XX.txt` files, we will only need to use
    # this file in Exercise 2.2. And in this exercise we only need the line that
    # starts with `tb_to_tb_evalue` and `begin`.

    # Paths to the files.
    path_tb_functions = 'data/tb_functions.pl'
    path_tb_data = 'data/orfs'

    # Call the function `read_tb_functions` and unpack the tuple.
    # Save the dictionaries as `clas` and `func`.
    clas, func = read_tb_functions(path_tb_functions)
    # Call the function `read_tb_data`.
    tb_data = read_tb_data(path_tb_data)

    # EJ 1.1
    # Call `no_orfs` to get no. per class.
    no_orfs = count_orf_clas(clas, func)

    # Plotting.
    # The best way to show the results for this exercise would be in a
    # vertical bar plot. Since we have 123 data points it would be difficult
    # to fit them all in a horizontal bar plot and for this plot it would not
    # make any sense to plot it in line graph plot.
    plot_barchart(no_orfs, 'Class', 'Number of ORFs',
                  'Number of ORFS to each class.', 7)

    # EJ 1.2
    # Call the function `show_orfcount_sw` with the searchword 'Respiration'.
    show_orfcount_sw(clas, no_orfs, 'Respiration')

    # EJ 2.1
    # Call the `calc_protein_hydro` to get number with 'hydro'/'protein'.
    data_21 = calc_protein_hydro(func)

    # Plotting.
    # Also in this exercise and in exercise 2.2 would the best way to present the
    # data in vertical bar plot. In both exercises we only have two data points
    # so use line graph plot would not be a good idea. We don't operate with
    # percentages either so a pie plot would not work.
    plot_barchart(data_21, 'Search term', 'Number of classes.',
                  'Number of classes with at least one ORF with search term.', 15)

    # EJ 2.2
    # Call the `calc_relac_orfs` to get the average number related orfs with
    # 'hydro'/'protein'
    data_22 = calc_relac_orfs(func, tb_data)

    # Plotting.
    plot_barchart(data_22, 'Search term', 'Average',
                  'Average no. of related ORFs for ORFS with search term.')

    # EJ 3
    # Call the `calc_multiple_m` to get the number of classes for each 'M'.
    data_3 = calc_multiple_m(clas)

    # Plotting.
    # For this exercises we decided to use line graph to represent the data
    # because it would easily show how the number how classes varies for
    # different values of 'M'.
    plot_graph(data_3, 'Integer M', 'Number of classes.',
               'Classes with at least 1 dimension >0 and a multiple of M')
