# Relative abundance of amino acids

## A simple project that calulates the relative abundance of Amino acids.

### Overview

This simple project focuses on a simple workflow to parse a FASTA file using bash and Python and compute the relative abundance of amino acids in a given amino acid sequences.

It is used for
* Protein sequence analysis
* To visualise residue frequency distributions
* Identifying different types of amino acid classification groups

### Features

* Parses FASTA files via Python.
* Counts the number of the occurance of each amino acid in the file.
* Calculates the relative frequencies for each amino acid in the sequence of iterest.
* Generates a relative abundance bar graph using `matplotlib`
* Outputs a relative density graphy sorted in alphabetical order of the amino acids

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

The function `statistics` identifies each line of sequence starting with a ">" and computes the number of unique elements other than ">", header and spaces, given a FASTA file. For each line of sequence, it iterates through a for loop where for each character it checks whether the character is in the dictionary stats. If the character is not in it, it creates a key:value pair in the dictionary where the key represents the unique element and the value represents the occurance of that element. When a new key:value pair is added, the value is zero and increments to 1 considering the count. If the element already exists in the dictionary,we increment the count. The function returns this key:value count as a dictionary.

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

