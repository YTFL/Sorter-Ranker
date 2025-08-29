# Sorter-Ranker

A simple Python tool that allows you to rank your favorite things by simply entering comma-separated values and choosing from the given options. This tool is designed to make sorting and ranking lists easy and interactive.

## Getting Started

1. **Clone the repository:**
	```
	git clone https://github.com/yourusername/Sorter-Ranker.git
	cd Sorter-Ranker
	```

2. **Run the application:**
	```
	python main.py
	```

## Usage

- Enter your list of items as comma-separated values.
- The tool will present you with pairs of items to compare.
- Choose your preferred item from each pair.
- At the end, you'll receive a ranked list based on your choices.

## Databases Available

.txt and .csv file database support available soon

## Features Planned to be Added in the Future

- Add support to take the input from a .csv file available on the machine directly (mention file name if file available in the same directory as the program or downloads, otherwise mention the file name with the path by the user)
- Export the comparison results to a .txt or .csv file (to downloads by default or path specified by the user)
- Export the comparison history to a .txt file (to downloads or path specified by the user)
- Scan for supported documents in a given path (or downloads and the program directory by default)

## Latest Features
- Added support for reading from text files directly from a specified path by the user\

## Known Issues
- The percentage being displayed is stuck at 100% for overhead comparisons instead of being adjusted dynamically

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Contribution for database is also welcome! You are welcome to add any database you wannt that is either .txt or .csv, a single column and related to entirely a single topic that are popular and can be used by anyone to rank as their wish. Please keep the database updated with the lastest info if you do decide to add one 

## License

This project is licensed under the MIT License - See the [LICENSE](LICENSE) for full details.
