# Relative abundance of nucleotides and amino acids

## A simple project that calulates the relative abundance of Nucleotides and Amino acids.

### Overview

This simple project focuses on a simple workflow to parse a FASTA file using bash and Python and compute the relative abundance of nucleotides or amino acids in a given sequence.

It is used for
* nucleotide sequence analysis
* Protein sequence analysis
* To visualise residue frequency distributions

### Features

* Parses FASTA files via Python.
* Counts the number of the occurance of each nucleotide/ amino acid in the file.
* Calculates the relative frequencies for each nucleotide/ amino acid in the sequence of iterest.
* Generates a relative abundance bar graph using `matplotlib`.
* Outputs a relative density graphy sorted in alphabetical order of the nucleotide/ amino acids.

### Requirements

* Python 3
* Linux like terminal to run bash codes
* `matplotlib`

Install libraries:
``` bash
pip install matplotlib
```

### Usage

#### Preparing FASTA files

Using linux like terminal:

1. Download the FASTA file.

``` bash
wget ftp://ftp.expasy.org/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000005640/UP000005640_9606.fasta.gz
```

2. Unzip the FASTA file if it is compressed.

``` bash
gunzip UP000005640_9606.fasta.gz
```
#### Running the code

Open `parser.py` Python file in any IDE of preference. Then run the code. (Note: `parser.py` and the downloaded fasta file must be in the same working directory, else it will raise an error -> ```FileNotFoundError```)

The code starts by importing the `matplotlib` module which is going to help us to visualise the relative abundances of the amino acids. It is imported as plt for easy use.

```python
import matplotlib.pyplot as plt
```

The function `statistics` identifies each line of sequence starting with a ">" and computes the number of unique elements other than ">", header and spaces, given a FASTA file. For each line of sequence, it iterates through a for loop where for each character it checks whether the character is in the dictionary called stats. If the character is not in it, it creates a key:value pair in the dictionary where the key represents the unique element and the value represents the occurance of that element. When a new key:value pair is added, the value is zero and increments to 1 considering the count. If the element already exists in the dictionary, we increment the count. The function returns this key:value count as a dictionary.

```python
def statistics(fasta_file) -> dict:
    '''Returns the abundances in all the sequences'''
    
    stats = {}
    for line in fasta_file:
        if ">" not in line:
            for char in line.strip("\n"):
                if char not in stats:
                    stats[char] = 0
                stats [char] += 1
    return stats
```
The function `graphical_statistics` computes the relative abundances using the results we obtained from the previous function and displays the results as a bar graph. First, it obtain the abundances from the `statistics` function and calculates the relative abundance iteratively. These values are stored as a key value pair in the dictionary rf where the keys are the amino acids or nucleotides and the values are their relative abundances. Then the bar graph is plotted using `matplotlib`. Here, option is provided to enter the title for the bar graph based on the user preference.

``` python
def graphical_statistics(my_data:dict):
     ''' Returns relative abundances as a bar graph'''

    rf = {}
    total = sum(my_data.values())
    for k in my_data:
        rf[k] = my_data[k]/total
    sorted_rf = dict(sorted(rf.items()))
    
    x = [k for k in sorted_rf]
    y = [v for v in sorted_rf.values()]
    
    plt.title(input('Enter the title: ))
    plt.bar(x,y)
    return plt.show()
```
#### Main Program
 
 The main program runs first by assigning the file name to the variable `fasta_file` via a while loop. The user is allowed to enter the file name. The program provides a warning if the file is not found and allows the user to re enter the correct file name. This continues as a loop until the user enters the correct file name.
 
 ```python
while True:
    fasta_file = input('Enter file name: ')
    if os.path.isfile(fasta_file):
        break  
    else:
        print('No file is found')
```
![Alt text](file not found.png)
 Then the file is opened and each line in the file is read. 

 ```python 
 my_file = open(fasta_file).readlines()
 ```

 Once done, the function `statistics` is applied to calculate the abundance and then the function `graphical_statistics` is applied to obtained the relative density graph.

```python
stats = statistics(my_file)
rf = graphical_statistics(stats)
print(rf)
```
### Results

Once the code is executed, the program returns a bar graph with the relative abundances of nucleotides or amino acids based on the type of FASTA file provided.

Reminder: And example and test files