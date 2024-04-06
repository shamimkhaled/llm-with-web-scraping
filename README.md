
# Data Extraction with LLM | Documentation
### Overview
Data Extraction with LLM (Language Model) is a Streamlit application designed to extract data from URLs using Langchain library and the OpenAI API. It facilitates users to input a URL link and retrieve data in JSON format from the OpenAI model.

### Live Deployment Site
The live deployment of this application can be accessed here.

### Prerequisites
Before using the Data Extraction with LLM application, ensure that you have the following prerequisites installed:
- Python 3.x
- OpenAI API key
- Streamlit
- Langchain
- Requests
- BeautifulSoup

### Setup
To set up the application, follow these steps:

- Clone the repository:
```bash
git clone https://github.com/shamimkhaled/llm-with-web-scraping.git

```
- Create and activate the virtual environment:

```bash
python -m venv venv

```
- Activate the virtual environment (In Windows):

```bash
.\venv\Scripts\activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Create a .env file in the project root and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
### Usage
Once the setup is complete, follow these steps to use the application:

Run the Streamlit app:
```bash
streamlit run main.py
```
- Enter your link in the provided input field.
- Select the option to specify which information to extract.
- Click the "Get Data" button to retrieve the extracted data in JSON format.
### Example
Here's an example usage scenario:

- User enters the URL of a news article.
- User selects to extract the article text.
- User clicks "Get Data" button.
- Application fetches the article text from the URL using Langchain and OpenAI API.
- Retrieved data is displayed in JSON format.
By following these steps, users can easily extract relevant data from URLs using the Data Extraction with LLM application.

## Troubleshooting
- If you encounter any issues during setup or usage, please refer to the GitHub repository's issue tracker or documentation for assistance.

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Authors

- [@shamimkhaled](https://www.github.com/shamimkhaled)

