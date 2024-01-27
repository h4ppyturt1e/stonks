# GPT-4 Based Sentiment Analysis for Stock Trading
---
Author(s): 
- Ryan Nicholas Permana (Jan 2024)


## Introduction
Welcome to our **GPT-4 based sentiment analysis project**. This tool is designed to assist users in making informed decisions about buying or selling stocks. It aims to analyze sentiment from various news outlets and financial data sources to provide insights into the potential performance of popular company stocks. 

Eventually, the project's goal is to include a simulated "portfolio" feature, allowing users to experiment with stock trading in a risk-free environment.

## Features
- **Sentiment Analysis:** Utilizes OpenAI's GPT-4 to analyze news data and evaluate the sentiment towards various stocks.
- **Stock Data Integration:** Fetches real-time data from popular stock market APIs.
- **Intuitive Dashboard:** A user-friendly interface to view stock sentiments, portfolio performance, and other relevant data.

Future goals:
- **Simulated Portfolio:** Users can manage a fake portfolio to test trading strategies based on the sentiment analysis.

## Example
After running `py main.py positive.txt`, with `positive.txt` containing the following text:

```
Booble Inc. Unveils Innovative Solar Technology
January 26, 2024 - Booble Inc., a prominent tech firm, today announced a new solar panel technology with an
industry-leading 40% efficiency rate. CEO Dr. Alex Hartman highlighted the potential of this technology to
revolutionize renewable energy accessibility and reduce costs.

Following the announcement, Booble's stock surged, signaling strong investor confidence. The company plans to
collaborate with governments and NGOs to distribute this technology globally, particularly in energy-scarce regions.
```

The following output is generated:
```
Sentiment: {
  "sentiment_score": 9,
  "sentiment_emotion": "positive"
}
```

<!-- ## Getting Started
### Prerequisites
- Python 3.8 or higher
- API keys for OpenAI's GPT-4 API
- API keys for news outlet APIs
- API keys for stock market data providers

### Installation
1. Clone the repository: `git clone https://github.com/h4ppyturt1e/stonks`

2. Navigate to the project directory: `cd stonks`

3. Install the required packages: `pip install -r requirements.txt`

### Configuration
- Place your API keys in a `.env` file in the root directory.
- Configure your preferred news sources and stock market APIs in the `config.json` file.

### Running the Application
To start the application, run: `python main.py`

This will launch the sentiment analysis engine and the user interface for portfolio management.

## Usage
- **View Sentiment Analysis:** The dashboard displays the latest sentiment analysis results for various stocks.
- **Manage Portfolio:** Use the simulated portfolio feature to buy and sell stocks based on sentiment data.
- **Monitor Performance:** Keep track of your portfolio's performance over time.

## Contributing
Contributions to improve the functionality and efficiency of this tool are welcome. Please follow the standard fork and pull request workflow.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Disclaimer
This tool is for educational and entertainment purposes only. It should not be used as the sole basis for real-world trading decisions.

## Acknowledgements
- OpenAI for the GPT-4 API
- News outlets and stock market data providers for their APIs -->

