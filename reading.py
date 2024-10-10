#!/usr/bin/env python3
import re
import os


def read_tb_functions(path_file: str) -> tuple:
    """
    Return two dictionaries with data from `tb_functions.pl`.

    This function read the data from `tb_functions.pl` and store the data
    in two dictionaries. Dictionary `clas_dict` is of the format:
    {`class ID`: `class description`} where class ID is a string of format:
    '1,0,0,0'. The second dictionary `func_dict` is of the format:
    {`class ID`:{`orf name`: [`gene name`, `orf description`]}}.

    :param path_file: Path to where `tb_functions.pl` is located.
    :return: Tuple of two dictionaries.
    """
    clas_dict = {}
    func_dict = {}
    # Regex to extract data between two brackets.
    rx = r"\[([^]]+)"
    with open(path_file)as f_obj:
        for line in f_obj:
            # Extract the class ID from inside the brackets.
            # Store it in the `cl_id` variable.
            cl_id = re.search(rx, line).group(1)
            # If the line starts with class stores `cl_id` as key of the
            # `clas_dict` and split the line string on `"` and stores the
            # the second element of the list as the value in `clas_dict`.
            if line.startswith('class'):
                clas_dict.setdefault(cl_id, line.split('"')[1])
            # If the line starts with `function` stores the `cl_id` as key
            # of the `func_dict` dictionary. To extract the ORF name, slices
            # the line from the 10th until 3rd last element and split the
            # string by `,` and picks the first element of the the list and
            # stores it as the key of the inner dictionary. To get the gene
            # name split on `'` and pick the second element of the list and
            # store it as the first element of the list that is inside the
            # inner dictionary. To get the orf description data we split the
            # line on `"` and pick the second element and store it as the
            # second element in the list inside the inner dictionary.
            elif line.startswith('function'):
                func_dict.setdefault(cl_id, {})
                orf = line[9:-3].split(',')[0]
                gene = line.split("'")[1]
                orf_descr = line[9:-3].split('"')[1]
                func_dict[cl_id].setdefault(orf, [gene, orf_descr])
    return clas_dict, func_dict


def read_tb_data(path_dir: str) -> dict:
    """
    Return a dictionary based on data in `tb_data_xx.txt`.

    This function will return a dictionary based on data from the
    `tb_data_xx.txt` files. The dictionary is of the format:
    {`orf name`: {`related to orf name`: `E-value`}}.

    :param path_dir: Path to the directory for the `tb_data_xx.txt`.
    :return: Dictionary.
    """
    data = {}
    # List all the files inside the directory.
    dirs = os.listdir(path_dir)
    # Iterate over all the files.
    for file in dirs:
        # Join path between given path in parameter and file listed
        # in dirs, then open the file.
        with open(os.path.join(path_dir, file)) as f:
            for line in f:
                # If the line starts with begin, slices the string to
                # get the name of the orf and store it as the key of the
                # `data` dictionary.
                if line.startswith('begin'):
                    k_dict = line[12:-4]
                    data.setdefault(k_dict, {})
                # If the line starts with `tb_to_tb_evalue`, extract
                # everything inside the parenthesis by slicing, then
                # split on `,` and store the first element (name of
                # related orf) as the key of the inner dictionary and the
                # second element (E-value) as the the value of the inner
                # dictionary.
                elif line.startswith('tb_to_tb_evalue'):
                    to_dict = line[16:-3].split(',')
                    data[k_dict].setdefault(to_dict[0], to_dict[1])
    return data
