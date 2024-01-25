
# number-to-word

number-to-word is a Python library for converting numbers into their written English or Arabic word equivalents. This library is particularly useful for financial applications, where there is a need to convert numeric values into written text. It also supports currency names.

## Features

- Convert numbers to written words in English or Arabic.
- Add currency names to the converted results.
- Lightweight and easy to integrate.

## Installation

You can install number-to-word using pip:

```bash
pip install number-to-word
```

## Usage

Here's a simple example of how to use number-to-word:

```python
from number_to_word import NumberToWord

# Convert a number to words in English
print(NumberToWord.to_word(123.5, 'SYP', "English"))  # Output: One Hundred Twenty Three Syrian Pounds and Fifty Piasters only.

# Convert a number to words in Arabic
print(NumberToWord.to_word(123.5, 'SYP', "Arabic"))  # Output: فقط مائة و ثلاثة و عشرون ليرة سورية و خمسون قرشاً لا غير.

```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing

This project is licensed under MIT License.

## Contact

For any queries or feedback, please reach out to Adel Khayata.

## Acknowledgements

- Thanks to all the contributors who have helped to shape number-to-word.