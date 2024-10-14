# Pandas Data Analysis

## Overview

Pandas is a powerful data manipulation and analysis library for Python. It provides data structures like DataFrames and Series, which allow for efficient handling of structured data. This project focuses on analyzing cryptocurrency data, specifically from Coinbase and Bitstamp.

## Features

- Load data from CSV files
- Calculate descriptive statistics
- Handle missing values
- Visualize data trends
- Perform data transformations and aggregations

## Installation

To use this project, ensure you have Python 3 and the required libraries installed. You can install the necessary libraries using pip:

```bash
pip install pandas matplotlib seaborn
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/davyleroy/alu-machine-learning.git
   cd alu-machine-learning/pipeline/pandas
   ```

2. Place your CSV data files in the `Data` directory.

3. Run the analysis scripts:
   - To calculate descriptive statistics:
     ```bash
     python 13-analyze.py
     ```
   - To prune the DataFrame by removing rows with missing values:
     ```bash
     python 8-prune.py
     ```
   - To visualize the data:
     ```bash
     python 14-visualize.py
     ```

## Example

Here is a brief example of how to load data and calculate descriptive statistics:

```python
from_file = import('2-from_file').from_file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
stats = df.describe()
print(stats)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
