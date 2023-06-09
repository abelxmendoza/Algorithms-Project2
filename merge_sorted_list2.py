import docx
import re

""" 
This script merges multiple arrays from a Word document 
into a single sorted list. The arrays in the document should 
be labeled with the prefix "Array_" and enclosed in square 
brackets []. The script extracts the array strings using regex, 
converts them into Python lists, merges them, sorts them, and 
returns the final list. Note that this script uses eval(), which 
can be a security risk with untrusted input.
"""


def parse_array(array_str):
    matches = re.findall(r"\[.*?\]", array_str, re.DOTALL)
    array = []
    for match in matches:
        print(match)
        array.append(eval(match))
    return array



def merge_arrays_from_docx(docx_file):
    document = docx.Document(docx_file)
    arrays = []
    for paragraph in document.paragraphs:
        if "Array_" in paragraph.text:
            array = parse_array(paragraph.text.strip())
            arrays.append(array)
    merged_array = []
    for array in arrays:
        merged_array.extend(array)
    merged_array.sort()
    return merged_array

if __name__ == "__main__":
    merged_array = merge_arrays_from_docx("in2C.docx")
    print(merged_array)


