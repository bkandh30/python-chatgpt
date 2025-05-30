# Python ChatGPT

A simple Python script for interacting with OpenAI's ChatGPT API using user input from the terminal.

## Features

- Interactive command-line interface for chatting with OpenAI's language model.
- Session-based conversation handling.
- Environment variable support for secure API key management.

## Prerequisites

- Python 3.7 or above
- An OpenAI API key

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/bkandh30/python-chatgpt.git
cd python-chatgpt
```

4. **Configure environment variables:**

Rename `.envExample` to `.env` and add your OpenAI API key:

```
CLIENT_SECRET = your_openai_api_key
```

## Usage

Run the script using:

```bash
python pychatgpt.py
```

You will be prompted to enter messages, and the assistant will reply using the OpenAI API. Type `exit` to end the session.

## File Structure

```
├── pychatgpt.py       # Main script
├── .envExample        # Example environment file for API key
└── README.md          # Project documentation
```

## License

This project is licensed under the MIT License.

## Disclaimer

This tool uses OpenAI's API and may incur usage costs based on your API plan. Read the OpenAI API documentation for any changes made to the API.
