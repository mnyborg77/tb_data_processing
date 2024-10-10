# Data analysis of Mycobacterium tuberculosis.

This package does a basic analysis of data of Mycobacterium tuberculosis.  
The data for this analysis comes originally from [UCI Machine Learning](https://archive.ics.uci.edu/ml/datasets/m.+Tuberculosis+Genes)
and is of the datalog format.

The package includes the following analysis:

1. Calculate the number of ORFs that belongs to each class.
2. Calculate how many ORFs the class that contains the word 'Respiration' in the description has.
3. Calculate the number of classes the contain at least one ORF with the word 'protein' or 'hydro' in the ORF description.
4. Calculate the average number related ORFs for ORFs that contain the word 'hydro' or 'protein' in the ORF description.
5. Calculate the number of classes that have at least one dimension that is greater than 0 and at the same time is a
 multiple of an integer 'M', where 'M' is between 2 and 9.
   
## Dependencies

matplotlib~=3.3.3

## Set up.

First you have to enter the package folder:
```shell
cd pec4
```

Then you have to set up a virtual environment:
```shell
virtualenv venv
```

Then you have to activate the virtual environment:
```shell
source venv/bin/activate
```

Now you have to install the dependencies:
```shell
pip install -r requirements.txt
```

## Run the package.

To run the package you have to first enter the package folder.
Then you can run with the following command in the terminal:
```shell
python3 basic_analysis.py
```

Or:
```shell
./basic_analysis.py
```

## Run the test.
To run all the tests at once, you have to enter the pec4 folder and run following command:
```shell
python3 -m unittest
```

Or to run the tests individual:
```shell
python3 -m unittest test.name_of_the_test_file
```
