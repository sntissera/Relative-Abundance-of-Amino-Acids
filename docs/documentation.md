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

Note: `parser.py` and the downloaded fasta file must be in the same working directory

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



