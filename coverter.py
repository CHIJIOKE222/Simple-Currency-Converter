def currency_converter():
    # This stores our exchange rates. 
    # 1 USD is used as the base for these calculations.
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "NGN": 1500.0, 
        "CAD": 1.35
    }

    print("--- Simple Currency Converter ---")
    print(f"Supported: {', '.join(rates.keys())}")

    try:
        # Get input from the user
        base = input("Convert FROM (e.g., USD): ").upper()
        target = input("Convert TO (e.g., NGN): ").upper()
        amount = float(input("Enter the amount: "))

        # Check if the currencies exist in our dictionary
        if base in rates and target in rates:
            # Logic: Convert amount to USD first, then to the target
            amount_in_usd = amount / rates[base]
            converted_amount = amount_in_usd * rates[target]
            
            print(f"\nResult: {amount} {base} = {converted_amount:.2f} {target}")
        else:
            print("\nError: Currency not supported. Please use USD, EUR, GBP, NGN, or CAD.")
            
    except ValueError:
        # This catches if a user types letters instead of numbers for the amount
        print("\nError: Please enter a numeric value for the amount.")

if __name__ == "__main__":
    currency_converter()