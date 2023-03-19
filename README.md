# README

This repository contains three Python scripts that perform various tasks:

## Algorithm 1: Target Terms or Substrings

`targetterms.py` is a script that extracts arrays of integers from a Microsoft Word document `in2a.docx` and stores them in a dictionary. It then extracts pairs of target terms from the arrays and prints out their indices within the first array and their original form in the second array.

To use the script, simply run it with an input Microsoft Word document (.docx) that contains the arrays. The output will be printed to the console.

## Algorithm 2: Run Encoding Problem

`run_encoding.py` is a script that performs run-length encoding on a string. It replaces each run of repeated characters in the input string with the string 'kx', where 'k' is the number of repetitions and 'x' is the repeated character.

To use the script, simply call the `run_encoding()` function with a string as its argument. The encoded string will be returned.

## Algorithm 3: Merging Techniques

`merge_sorted_list2.py` is a script that extracts arrays from a Microsoft Word document and merges them into a single, sorted array.

`merge_sorted_list.py` is a script that does the same thing as `merge_sorted_list2.py` , but does not take input from a file, and is instead hardcoded in the script.

To use the script `merge_sorted_list2.py`, simply run it with an input Microsoft Word document (.docx) `in2C.docx` that contains the arrays. The merged array will be printed to the console.

Please note that all three scripts require the `docx` library to be installed. You can install it using pip: `pip install python-docx`.

---

**See Doc for more info on these algorithms:**

https://docs.google.com/document/d/1NXwfwyuRSTHYBsN6AlteyLhei0LPCzdkv3VSGWKcXJs/edit?usp=sharing
