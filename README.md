# CurrencyExchangeAPI

CurrencyExchangeAPI is a simple and efficient API for converting currencies. Built with Python, this API provides easy access to currency conversion rates and allows for quick conversions between different currencies.

## Features

- Retrieve a list of all available currencies.
- Convert amounts from one currency to another.
- Get the latest exchange rates for a specific currency.

## Endpoints

### Get All Available Currencies

**URL:** `https://currencyexchangeapi-cs01.onrender.com/currencyList`

**Method:** GET

**Description:** Retrieve a list of all available currencies.

### Convert Currency

**URL:** `https://currencyexchangeapi-cs01.onrender.com/latest/<currency>`

**Method:** GET

**Description:** Convert the specified amount from the source currency to the target currency. If no target currency is specified, the conversion will use the default target currency.

**Parameters:**

- `currency` (required): The source currency code.
- `target` (optional): The target currency code. If not provided, the default target currency will be used.
- `amount` (optional): The amount to convert. If not provided, the default amount will be 1.

**Examples:**

1. Get the latest exchange rates for a specific currency:
'''
GET https://currencyexchangeapi-cs01.onrender.com/latest/USD
'''
2. Convert from one currency to another:

'''
GET https://currencyexchangeapi-cs01.onrender.com/latest/USD?target=EUR
'''

3. Convert a specific amount from one currency to another:
'''
GET https://currencyexchangeapi-cs01.onrender.com/latest/USD?target=EUR&amount=100
'''

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

For any inquiries or feedback, please contact Jung Tae Cha (chonte0313).

python
Copy code

You can adjust the "username" in the GitHub repository URL and any other details as necessary.
