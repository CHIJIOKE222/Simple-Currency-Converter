Simple Currency Converter
A lightweight, user-friendly Python application that performs real-time currency conversions using a base-reference exchange rate system. This project demonstrates core programming concepts like data mapping, user input validation, and error handling.

🚀 Overview
This tool allows users to quickly convert between major global currencies (USD, EUR, GBP, CAD) and the Nigerian Naira (NGN). It is designed to be a foundation for a more complex financial application involving live API integrations.

Key Features
Dictionary-Based Mapping: Uses Python dictionaries to store and retrieve exchange rates efficiently.

Bidirectional Conversion: Convert from any supported currency to another (not just to/from USD).

Input Validation: Includes try-except blocks to catch non-numeric inputs and prevent program crashes.

Case Insensitivity: Automatically handles user input whether typed in lowercase or uppercase.

🛠️ Technical Stack
Language: Python 3.x

Key Concepts: Functions, Dictionaries, Conditional Logic, String Formatting.

💻 How to Use
Clone the Repository:

Bash
git clone https://github.com/YOUR_USERNAME/Simple-Currency-Converter.git
Run the Script:
Navigate to the folder and run:

Bash
python converter.py
Interact:
Follow the on-screen prompts to enter your source currency, target currency, and the amount you wish to convert.

📋 Example Output
Plaintext
--- Simple Currency Converter ---
Supported: USD, EUR, GBP, NGN, CAD
Convert FROM: USD
Convert TO: NGN
Enter the amount: 50

Result: 50.0 USD = 75000.00 NGNS