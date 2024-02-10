import os

X1 = 0
X2 = 0
Number_of_the_file = 0
Deep5 = 0
Add_Numbers = 0
start_bits = 0
Multiply = 0
Z = 0  # Initialize Z to 0

# Create a new folder named "Dictionary_Black_hole" if it doesn't exist
folder_name = "Dictionary_Black_hole"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create a new file named "file_name.txt" to store all numbers
file_path = os.path.join(folder_name, "file_name.txt")
with open(file_path, "w") as file:
    while X2 < 2**24:
        Number_of_the_file = 0  # Reset Number_of_the_file at the beginning of each iteration of the outer loop
        Square_of_ROOT = 2**Deep5
        Number_of_the_file = ((((Number_of_the_file * Square_of_ROOT) + Add_Numbers) // 3) * Multiply)
        start_bits = len(str(X1)) + len(str(X2))  # Calculate start_bits as the length of X1 and X2
        # Calculate lengths of X1 and X2
        N1 = len(str(X1))
        N2 = len(str(X2))
        # Write the values to the file
        file.write(f"Size of bits: {start_bits}\n")
        file.write(f"X1: {X1}, N1: {N1}\n")
        file.write(f"X2: {X2}, N2: {N2}\n")
        file.write(f"Number_of_the_file: {Number_of_the_file}\n")

        X1 += 1
        Number_of_the_file += 1  # Increment Number_of_the_file for each file created
        if X1 == 2**24:
            X1 = 0
            X2 += 1
        Deep5 += 1
        Add_Numbers += 1
        Multiply += 24
