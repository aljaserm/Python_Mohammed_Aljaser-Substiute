import json
import sys

def substitute_dict(input_dict, depth):
    output_dict = {}

    # Check if the depth is 0 to determine if further substitution should be performed
    if depth == 0:
        for key, value in input_dict.items():
            if isinstance(value, dict):
                # Recursively substitute values in nested dictionaries
                output_dict[key] = substitute_dict(value, depth)
            else:
                # Replace non-dictionary values with {'_content': old_value, '_type': str(type(old_value))}
                output_dict[key] = {'_content': value, '_type': str(type(value))}
    else:
        for key, value in input_dict.items():
            if isinstance(value, dict):
                # Recursively substitute values in nested dictionaries up to the specified depth
                output_dict[key] = substitute_dict(value, depth - 1)
            else:
                output_dict[key] = {'_content': value, '_type': str(type(value))}
    return output_dict

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python substitute.py <input_file> <depth> <output_file>")
        return

    # Get the command line arguments
    input_file = sys.argv[1]
    depth = int(sys.argv[2])
    output_file = sys.argv[3]

    # Load the input JSON data from the file
    with open(input_file, 'r') as file:
        input_data = json.load(file)

    # Perform substitution on the input dictionary
    output_data = substitute_dict(input_data, depth)

    # Write the output dictionary to the file
    with open(output_file, 'w') as file:
        json.dump(output_data, file, indent=4)

if __name__ == '__main__':
    main()