# SetValues.py for Star Wars Empire at War Value Changer

This Python script is part of the Star Wars Empire at War Value Changer project. It is designed to set the values for a specific faction in all XML files as specified by the user.

## Features

- Scans a directory for XML files, either recursively or non-recursively.
- Cleans XML files that have anything before the XML declaration.
- Changes the value of an element in an XML file based on the affiliation and element name.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `SetValues.py` file.
3. Set the variables at the top of the script to match your requirements.
4. Run the script from the command line as follows:

## Variables

- `fileDir`: The directory where the XML files are located.
- `populationVal`, `buildCostVal`, `buildTimeVal`, `addPopulationVal`: The values to set in the XML files.
- `affiliationVal`: The affiliation to filter the XML files.
- `recurse`: Whether to scan the directory recursively or not.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)