Numerical Integration Tool (Trapezoidal Rule)
This repository contains a Python-based numerical integrator that estimates the definite integral of a function using the Trapezoidal Rule. This project demonstrates the application of computational mathematics to solve calculus problems programmatically.

Overview
The Trapezoidal Rule is a numerical method used to approximate the area under a curve by dividing the total area into several trapezoids rather than rectangles. This approach generally provides a more accurate approximation for smooth functions.
Features
Customizable Limits: Define the lower ($a$) and upper ($b$) bounds of integration.
Precision Control: Adjust the number of sub-intervals ($n$) to increase calculation accuracy.
Error Handling: Validates user input to ensure the program handles non-numeric data gracefully.

🛠️ How It Works
The script implements the following mathematical formula:$$\int_{a}^{b} f(x) \, dx \approx \frac{h}{2} \left[ f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b) \right]$$where $h = \frac{b-a}{n}$.

💻 How to Run
Ensure you have Python 3.x installed on your machine.
Clone this repository:Bashgit clone https://github.com/YOUR_USERNAME/Numerical-Integration-Python.git
Navigate to the directory and run the script:Bashpython integrator.py

🧪 Example Test Case
Function: $f(x) = x^2$Interval: $[0, 1]$Sub-intervals ($n$): 100Expected Result: $\approx 0.333350

$How to push this new file:
Go to the Source Control tab in VS Code.
You will see README.md under Changes.Click the + to stage it.
Type Add professional README in the message box and click Commit.
Click the Sync Changes (or Push) button.