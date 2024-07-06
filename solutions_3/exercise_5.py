data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]

for amount, currency, target_currency, exchange_rate in data:
    converted_amount = amount * exchange_rate
    print(f"{amount} {currency} = {converted_amount:.2F} {target_currency}")