#!/usr/bin/env python3
import re


# EX 1.1
def count_orf_clas(clas_dict: dict, func_dict: dict) -> dict:
    """
    Return the number of ORFs for each class.

    This function will take two arguments; the two dictionaries created
    in the `read_tb_functions`. Out from their data it will count the
    number of orfs for each class.

    :param clas_dict: Dictionary with class id and descripcion of class.
    :param func_dict: Dictionary with class id and info about the belonging
     ORFs.
    :return: Dictionary with class id as key and number of ORFs as value.
    """
    orf_clas = {}
    # Since the func_dict only contains the classes that have orfs and not
    # all the classes have orfs we have to iterate over the clas_dict.
    for key in clas_dict:
        # Initiate the dictionary `orf_class` that will store the data of
        # the counting of orfs. Set the default of the count to zero.
        orf_clas.setdefault(key, 0)
        # If the `func_dict` contains the class, we calculate the number of
        # orfs this class has by the taking the `len()` function on the inner
        # dictionary of the `func_dict`.
        if key in func_dict:
            orf_clas[key] = len(func_dict[key])
    return orf_clas


# EX 1.2
def show_orfcount_sw(clas_dict: dict, cnt_orfs, search_wrd: str) -> None:
    """
    Print the number of ORFs belonging to the class that contains the
    search word in the descripcion.

    :param clas_dict: Dictionary with class id and descripcion of class.
    :param cnt_orfs: Dictionary of counted orfs per class from function
        count_orf_clas.
    :param search_wrd: The word to search for in the descripcion of the class.
    :return: None
    """
    for key in clas_dict:
        # Check if the search word is in the descripcion string of the class.
        if search_wrd in clas_dict[key]:
            # If it is print a message with the number of ORFS.
            print(f"Class {key} has '{search_wrd}' in description and " +
                  f"has {cnt_orfs[key]} ORFs.")


# EX 2.1
def orfs_w_protein_hydro(func_dict: dict) -> tuple:
    """
    Return ORFs that have the word 'hydro' or 'protein' in descipcion.

    This function will return a tuple of two dictionaries; `hydro_dic` and
    `protein_dic`. `protein_dic` will contain all ORFs has the word `protein`
    in its descripcion, while `hydro_dic` will contain all ORFS that have the
    word `hydro` and this word is 13 letter long in its descripcion.

    :param func_dict: Dictionary with class id and info about the belonging
     ORFs.
    :return: Tuple of two dictionaries.
    """
    hydro_dic = {}
    protein_dic = {}
    # Iterate over the keys of outer dictionary.(class id)
    for key in func_dict:
        # Iterate over the keys for the inner dictionary.(ORF name)
        for k in func_dict[key]:
            # Stores the orf-descripcion-string in the variable `str_descr`.
            str_descr = func_dict[key][k][1]
            # If the descripcion contains `protein` store it in protein_dic.
            # With key being the orf name and the value the class id.
            if 'protein' in str_descr:
                protein_dic.setdefault(k, key)
            # Look for descripcion strings that contain the word `hydro`.
            if 'hydro' in str_descr:
                # Split the string on " " or "-", and iterate over it.
                for i in re.split('[ -]', str_descr):
                    # Check if any element of the string is 13 letters long
                    # and contains `hydro`.
                    if len(i) == 13 and 'hydro' in i:
                        # If it does, store it in hydro_dic. With key being the
                        # orf name and the value the class id.
                        hydro_dic.setdefault(k, key)
    return protein_dic, hydro_dic


def calc_protein_hydro(func_dic: dict) -> dict:
    """
    Calculate the number of classes that contain `hydro` or `protein.

    :param func_dic: Dictionary with class id and info about the belonging
     ORFs.
    :return: Dictionary with number classes.
    """
    # Call the function `orfs_w_protein_hydro` and unpack the tuple.
    prot, hyd = orfs_w_protein_hydro(func_dic)
    # Get the values of the two dictionaries. Find the distinct classes by
    # using `set()` and count the amount of classes with `ln()` method.
    return {'protein': len(set(prot.values())), 'hydro': len(set(hyd.values()))}


# EX 2.2
def calc_relac_orfs(func_dict: dict, tb_data_dic: dict) -> dict:
    """
    Calculate the average number of realated orfs to orfs that have
    descripcion containing the words 'hydro' or 'protein'.

    :param func_dict: Dictionary with class id and info about the belonging
     ORFs.
    :param tb_data_dic: Dictionary with name of ORFs and related ORFs.
    :return: Dictionary with average number of related orfs.
    """
    # Call the function `orfs_w_protein_hydro` and unpack the tuple.
    prot, hyd = orfs_w_protein_hydro(func_dict)
    # Set counters.
    cnt_prot = 0
    cnt_hydro = 0
    # Iterate over ORF name that have 'protein' in descripcion.
    for key in prot:
        # Add to the counter for proteins the number of related ORFs.
        cnt_prot += len(tb_data_dic[key])
    # Iterate over ORF name that have 'hydro' in descripcion and is 13
    # letters long.
    for key in hyd:
        # Add to the counter for hydro the number of related ORFs.
        cnt_hydro += len(tb_data_dic[key])
    # Calculate the average by dividing the counters on the total numbers
    # of ORFs and round to two decimals with the `round()` method.
    return {'protein': round(cnt_prot/len(prot), 2),
            'hydro': round(cnt_hydro/len(hyd), 2)}


# EX 3
def calc_multiple_m(clas_dict: dict) -> dict:
    """
    Calculate the number of classes that has at least one dimension >0 and
    at the same time a multiple of M. M is an iteger betwen 2 and 9.

    :param clas_dict: Dictionary with class id and descripcion of class.
    :return: Dictionary with number of classes as values and the integer M
        as the key.
    """
    cnt_m = {}
    # Iterate over the class id.
    for key in clas_dict:
        # First we have to transfer the class id from a string to a list of
        # integers to be able to work with it. We split the class id string on
        # comma and make them all integer by mapping the `int()` function
        # using `map()`.
        clas_lst = list(map(int, key.split(',')))
        # We iterate over the differen values for `M`.
        for m in range(2, 10):
            # The class is a multiple of `M` if it is divisble by `M`.
            # We use `filter()` to filter away class dimension that
            # are not greater than 0 and divisble by `M`.
            if list(filter(lambda x: x > 0 and not x % m, clas_lst)):
                # If the class is a multiple of `M` and >0 we count it.
                cnt_m.setdefault(m, 0)
                cnt_m[m] += 1
    return cnt_m
