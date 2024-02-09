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

while X2 < 2**24:
    Number_of_the_file = 0  # Reset Number_of_the_file at the beginning of each iteration of the outer loop
    Square_of_ROOT = 2**Deep5
    Number_of_the_file = ((((Number_of_the_file * Square_of_ROOT) + Add_Numbers) // 3) * Multiply)
    start_bits = len(str(X1)) + len(str(X2))  # Calculate start_bits as the length of X1 and X2
    for i in range(1, 2**24 + 1):
        # Create new filename based on Z
        filename = f"filename_Z_{Z}.txt"
        
        # Write something to the file including size of bits, X1, X2, and Z
        with open(os.path.join(folder_name, filename), "w") as file:
            file.write(f"Size of bits: {start_bits}\n")
            file.write(f"X1: {X1}\n")
            file.write(f"X2: {X2}\n")
            file.write(f"Z: {Z}\n")
            file.write(f"Number_of_the_file: {Number_of_the_file}\n")
        
        X1 += 1
        Z += 1  # Increment Z for each file created
        Number_of_the_file += 1  # Increment Number_of_the_file for each file created
        if X1 == 2**24:
            X1 = 0
            X2 += 1
    Deep5 += 1
    Add_Numbers += 1
    Multiply += 24
