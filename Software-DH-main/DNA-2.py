import paq

def compress_value(value):
    if value == 0:
        return 99
    return value - 1

def decompress_value(value):
    if value == 99:
        return 0
    return value + 1

def compress_16_bits(input_data):
    compressed_data = []
    space_count = 0  # Counter for the spaces
    for char in input_data:
        value = int(char)
        if value == 0:
            space_count += 1
        compressed_value = compress_value(value)
        compressed_data.append(compressed_value)
    return compressed_data, space_count

def decompress_16_bits(input_data):
    decompressed_data = []
    space_count = 0  # Counter for the spaces
    for char in input_data:
        value = int(char)
        if value == 99:
            space_count += 1
        decompressed_value = decompress_value(value)
        decompressed_data.append(decompressed_value)
    return decompressed_data, space_count

def main():
    try:
        input_file = input("Enter the input file name: ")
        output_file = input("Enter the output file name: ")
        option = int(input("Enter the option: 1. Compress 2. Extract: "))

        with open(input_file, 'rb') as file:
            data = file.read()

        if option == 1:
            compressed_data, space_count = compress_16_bits(data)
            compressed_data = bytes(compressed_data)
            compressed_data = paq.compress(compressed_data)
            with open(output_file, 'wb') as file:
                file.write(compressed_data)
            print(f"Data compressed successfully. Spaces compressed: {space_count}")
        elif option == 2:
            decompressed_data = paq.decompress(data)
            decompressed_data = [int(byte) for byte in decompressed_data]
            decompressed_data, space_count = decompress_16_bits(decompressed_data)
            with open(output_file, 'wb') as file:
                file.write(bytes(decompressed_data))
            print(f"Data extracted successfully. Spaces extracted: {space_count}")
    except FileNotFoundError:
        print("The specified file was not found.")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()