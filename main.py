from flask import Flask, request, jsonify
import json
from currency_converter import CurrencyConverter, RateNotFoundError


app = Flask(__name__)

#returns either a list of convertible currencies with each rate according to the user's base currency
@app.route("/latest/<currency>")
def getLatestConversion(currency): 
    c = CurrencyConverter()
    data = []
    amount = 1
    otheramount = request.args.get("amount")
    if otheramount : 
        amount = float(otheramount)
    first_date, last_date = c.bounds[currency]
    print(last_date)
    extra = request.args.get("target")
    if extra : 
        try: 
                    
            a = c.convert(amount, currency, extra) 

            t = {
                "target" : extra,
                "amount" : a
            }
            value = {
                "amount" : amount,
                "updated_at" : last_date,
                "rate" : t
            }    
            return value, 200
        except RateNotFoundError:
            print(extra + " rate not found")
            t = {
                "target" : extra,
                "amount" : 0,
                "error" : "Rate not found on database"
            }
            value = {
                "amount" : amount,
                "updated_at" : last_date,
                "rate" : t
            }    
            return value, 200

    else :     
        for i in c.currencies : 
            if i != currency:
                try: 
                    
                    a = c.convert(amount, currency, i) 

                    t = {
                        "target" : i,
                        "amount" : a
                    }
                    data.append(t)
                except RateNotFoundError:
                    print(i + " rate not found")
                    t = {
                        "target" : i,
                        "amount" : 0,
                        "error" : "Rate not found on database"
                    }

                    data.append(t)

    data.sort(key=lambda x: x["target"])
    value = {
        "amount" : amount,
        "updated_at" : last_date,
        "rates" : data
    }    
    return value, 200



#returns a list of currency available for the api
@app.route("/currencyList")
def getAllCurrencies(): 
    c = CurrencyConverter()
    print(c.currencies)
    list = c.currencies
    a = []
    for i in list:
        a.append(i)
    a.sort()
    return a
    #return list, 200

if __name__ == "__main__": 
    app.run(port=8000,debug=True)

