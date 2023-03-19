def run_encoding(S):
    """
    This function takes a string 'S' as input and returns a run-length encoded string 'C',
    where each run of repeated characters in the input string is replaced with the string
    'kx', where 'k' is the number of repetitions and 'x' is the repeated character.
    """
    C = ''      # Initialize an empty string to store the encoded output
    k = 1       # Initialize a counter to keep track of the number of repetitions
    x = S[0]    # Initialize a variable to store the current character being counted
    for i in range(1, len(S)):
        if S[i] == x:   # If the current character is the same as the previous character
            k += 1      # Increment the counter
        else:           # If the current character is different from the previous character
            if k > 1:   # If the counter is greater than 1, append the run length and character to the output string
                C += str(k) + x
            else:       # If the counter is 1, append only the character to the output string
                C += x
            k = 1       # Reset the counter to 1
            x = S[i]    # Set the current character to the new character being counted
        if i == len(S) - 1:     # If we have reached the end of the string
            if k > 1:           # If the counter is greater than 1, append the final run length and character to the output string
                C += str(k) + x
            else:               # If the counter is 1, append only the final character to the output string
                C += x
    return C    # Return the run-length encoded string


# Sample inputs and outputs
print(run_encoding("ddd"))  # Output: "3d"
print(run_encoding("heloooooooo there"))  # Output: "hel8o there"
print(run_encoding("choosemeeky and tuition-free"))  # Output: "ch2osem2eky and tuition-fr2e"
print(run_encoding("a"))  # Output: "a"
print(run_encoding("abc"))  # Output: "abc"


