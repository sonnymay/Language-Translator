# Language Translator with Python and Googletrans

This repository contains a simple language translator implemented with Python and the `googletrans` library. This program translates a given text from English to a specified language using the Google Translate's Ajax API.

## Installation

1. Make sure you have Python 3 installed. If not, you can download it from [here](https://www.python.org/downloads/).
2. Clone this repository by running `git clone https://github.com/sonnymay/language-translator.git` in your command line.
3. Navigate into the project directory with `cd language-translator`.
4. Create a virtual environment using `python3 -m venv venv`.
5. Activate the virtual environment using `source venv/bin/activate` for Unix or Linux systems or `venv\Scripts\activate` for Windows.
6. Install the required dependencies with `pip install -r requirements.txt`.

## Running the Application

To run the application:

1. Make sure you're in the project's root directory and the virtual environment is activated.
2. Run `python translator.py` in the terminal.

## Customizing the Translation

To translate your own text and specify a language, modify the following lines in `translator.py`:

```python
text_to_translate = "Hello, how are you?"
destination_language = "fr"  # French
```

Replace `"Hello, how are you?"` with your text and `"fr"` with the desired language's ISO 639-1 code. A list of all supported languages and their codes can be found [here](https://cloud.google.com/translate/docs/languages).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out. My GitHub profile is [@sonnymay](https://github.com/sonnymay).

---
