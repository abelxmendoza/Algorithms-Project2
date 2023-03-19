import docx

"""
This script reads in an input Microsoft Word document (.docx) that contains
multiple paragraphs, each of which represents an array of integers. The script
extracts the arrays from the document and stores them in a dictionary, with the
array names as keys and the arrays as values. It then extracts pairs of target
terms from the arrays and prints out their indices within the first array and
their original form in the second array.

For example, if the input document contains two arrays like this:

    array 1a = [3, 4, 7, 2, 9, 5, 1]
    array 1b = [apple, banana, orange]

The script will output:

    7 11 20
    apple banana orange
"""



doc = docx.Document('in2a.docx')

# get all paragraphs from the document
paragraphs = [p.text for p in doc.paragraphs]

arrays = {}

# iterate over paragraphs and extract arrays
for p in paragraphs:
    if p.startswith('array'):
        # extract array name and contents
        name, values = p.split('=')
        # convert contents to list of words and remove whitespace and punctuation
        values = values.strip().replace('[','').replace(']','').replace('‘','').replace('’','').replace('\"','').replace(' ','').replace('\n','').split(',')
        # add array to dictionary
        arrays[name.strip()] = values

# extract target terms from arrays and print them in order
for i in range(1, len(arrays) // 2 + 1):
    # get target terms
    A = ''.join(arrays[f"array {i}a"]).lower()
    B = arrays[f"array {i}b"]
    # find indices of target terms in A
    indices = [str(A.index(b.lower())) for b in B]
    # print indices and target terms
    print(' '.join(indices))
    print(' '.join(B))



