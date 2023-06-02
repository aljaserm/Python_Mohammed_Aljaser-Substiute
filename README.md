
### substitute.py

A Python script to perform value substitution in a dictionary based on specified depth.

#### Usage

```
python substitute.py <input_file> <depth> <output_file>
```

- `<input_file>`: The file name of the input JSON file.
- `<depth>`: An integer specifying the depth of the substitution.
- `<output_file>`: The file name to save the output JSON.

#### Example

```
python substitute.py input.json 2 output.json
```

This will perform value substitution on the `input.json` file up to a depth of 2 and save the result in `output.json`.

#### Requirements

- Python 3

#### Installation

No installation is required. Simply download the `substitute.py` script and run it using Python.

#### How it Works

The script reads a JSON file, traverses the dictionary, and performs value substitution based on the specified depth. If a value is not a dictionary, it is replaced with `{'_content': old_value, '_type': str(type(old_value))}`. If the value is a dictionary, the substitution is performed recursively up to the specified depth.

#### Command Line Arguments

- `input_file`: The path to the input JSON file.
- `depth`: An integer specifying the depth of the substitution.
- `output_file`: The path to the output JSON file.

#### Example Input JSON

```json
{
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  }
}
```

#### Example Output JSON (depth=1)

```json
{
  "name": {
    "_content": "John",
    "_type": "<class 'str'>"
  },
  "age": {
    "_content": 30,
    "_type": "<class 'int'>"
  },
  "address": {
    "_content": {
      "street": "123 Main St",
      "city": "New York"
    },
    "_type": "<class 'dict'>"
  }
}
```

#### License