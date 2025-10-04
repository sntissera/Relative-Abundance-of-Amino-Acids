import matplotlib.pyplot as plt

def statistics(fasta_file) -> dict:
    '''Parses a FASTA file and returns the abundances in all the sequences'''

    stats = {}
    for line in fasta_file:
        if ">" not in line:
            for char in line.strip("\n"):
                if char not in stats:
                    stats[char] = 0
                stats [char] += 1
    return stats

def graphical_statistics(my_data:dict):
    ''' Returns relative abundances as a bar graph'''
    
    rf = {}
    total = sum(my_data.values())
    for k in my_data:
        rf[k] = my_data[k]/total
    sorted_rf = dict(sorted(rf.items()))
    
    x = [k for k in sorted_rf]
    y = [v for v in sorted_rf.values()]
    
    plt.title(input('Enter the title: '))
    plt.bar(x,y)
    return plt.show()

fasta_file = "uniprotkb_proteome_UP000005640_2025_09_24.fasta"
my_file = open(fasta_file).readlines()
stats = statistics(my_file)
rf = graphical_statistics(stats)
print(rf)