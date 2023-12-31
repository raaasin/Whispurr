# Whispurr

Whispurr is a WhatsApp chat bot that automates the process of reading and responding to unread messages using Selenium and a custom chatbot powered by the pGPT model.

## Features

- Automatically reads and responds to unread messages on WhatsApp Web.
- Utilizes the pGPT chatbot model to generate responses.
- Customizable bot personality and facts.

## Prerequisites

Before running Whispurr, make sure you have the following prerequisites installed:

- Python 3.10
- Selenium
- Transformers library (for pGPT)
- Chrome WebDriver

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/raaasin/Whispurr
   cd Whispurr

   ```
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Download the Chrome WebDriver and specify its path in `bot.py`.

## Usage

1. Run the `bot.py` script:

   ```bash
   python bot.py
   ```
2. Scan the QR code to log in to WhatsApp Web.
3. Whispurr will continuously check for unread messages, respond to them using the pGPT chatbot, and close the chat after processing.

## Configuration

You can customize Whispurr's personality and facts by modifying the `personas` variable in `pGPT.py`. Add your own persona traits to make Whispurr unique.

## Credits

- [Selenium](https://www.selenium.dev/) - Web automation framework
- [Transformers library](https://huggingface.co/transformers/) - Natural language processing models

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
