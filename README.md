# Daily Fantasy Sports Article Sentiment Analyzer

Welcome to the Daily Fantasy Sports (DFS) Article Sentiment Analyzer! This program is designed to help you analyze daily fantasy sports articles by extracting named entities and their sentiment scores. To use the program, simply copy and paste your DFS article of choice into the `dfs_test.txt` file, and the program will generate a CSV file containing the named entities and their sentiment scores.

## Table of Contents

- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Requirements

Make sure you have the following installed:

- Python 3.6 or higher
- Required Python packages:
  - nltk
  - pandas
  - textract

## How to Use

Follow these simple steps to use the DFS Article Sentiment Analyzer:

1. Clone or download this repository to your local machine.
2. Locate the `dfs_test.txt` file within the repository.
3. Open the `dfs_test.txt` file with a text editor of your choice.
4. Copy and paste the content of your daily fantasy sports article into the `dfs_test.txt` file.
5. Save the `dfs_test.txt` file.
6. Run the main program: `python dfs_article_sentiment_analyzer.py`

After running the program, you will find the analysis results in a newly generated CSV file named `dfs_test3.csv`. Open this file to view the extracted named entities and their sentiment scores.

## Features

The DFS Article Sentiment Analyzer includes the following features:

- Named Entity Recognition to extract player and team names
- Sentiment analysis for each unique entity
- Merging single-named entities with the same sentiment score
- Exporting results to a CSV file

## Contributing

We welcome contributions to improve the DFS Article Sentiment Analyzer. Please feel free to submit issues, feature requests, and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
