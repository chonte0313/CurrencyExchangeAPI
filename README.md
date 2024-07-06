# CurrencyExchangeAPI

CurrencyExchangeAPI is a simple and efficient API for converting currencies. Built with Python, this API provides easy access to currency conversion rates and allows for quick conversions between different currencies.


## Features

- Retrieve a list of all available currencies.
- Convert amounts from one currency to another.
- Get the latest exchange rates for a specific currency.
- Get historical exchange rates for a specific date and currency.

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
```
GET https://currencyexchangeapi-cs01.onrender.com/latest/USD
```
3. Convert from one currency to another:

```
GET https://currencyexchangeapi-cs01.onrender.com/latest/USD?target=EUR
```

3. Convert a specific amount from one currency to another:
```
GET https://currencyexchangeapi-cs01.onrender.com/latest/USD?target=EUR&amount=100
```

### Get Historical Exchange Rates

**URL:** `https://currencyexchangeapi-cs01.onrender.com/<thisdate>/<currency>`

**Method:** GET

**Description:** Get historical exchange rates for a specific date and currency. Optionally, convert a specific amount from the source currency to the target currency on that date.

**Parameters:**

- `thisdate` (required): The date in `YYYY-MM-DD` format.
- `currency` (required): The source currency code.
- `target` (optional): The target currency code. If not provided, rates for all available currencies will be returned.
- `amount` (optional): The amount to convert. If not provided, the default amount will be 1.

**Examples:**

1. Get historical exchange rates for a specific date and currency:
   ```GET https://currencyexchangeapi-cs01.onrender.com/2023-02-01/USD```

2. Convert a specific amount from one currency to another on a specific date:
   ```GET https://currencyexchangeapi-cs01.onrender.com/2023-02-01/USD?target=EUR&amount=100```
   
### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Sources

- **CurrencyConverter:** `https://pypi.org/project/CurrencyConverter/`
- **European Central Bank:** `https://www.ecb.europa.eu/home/html/index.en.html`

### License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
