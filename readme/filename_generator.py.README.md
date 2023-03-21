# TARP
This code defines a function called new_filename that takes in two parameters: mode and filename (which has a default value of None). The function generates a random 5-digit number and concatenates it with a string that depends on the value of mode to create a new filename in the ./Images/ directory. If a file with that filename already exists, the function generates another random number and tries again until it finds a unique filename. Finally, the function returns the unique filename.
Example for working of the code:
new_filename_e = new_filename('e')  # generates a new filename for encryption
new_filename_d = new_filename('d', 'encrypted-123.png')  # generates a new filename for decryption based on an existing filename
