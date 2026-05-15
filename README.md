# LOGIC BOX


A simple Python console application that allows users to:

- Generate a star (`*`) pattern
- Analyze numbers in a given range
- Identify whether numbers are even or odd
- Calculate the sum of numbers in a range

---

## Features

### 1. Pattern Generator
Generates a right-angled triangle star pattern based on the number of rows entered by the user.

### Example
```text
*
**
***
****
*****
```

---

### 2. Number Analyzer
Analyzes numbers within a user-defined range and:

- Determines whether each number is **Even** or **Odd**
- Displays the result for every number
- Calculates the total sum of the range

### Example
```text
Number 1 is Odd
Number 2 is Even
Number 3 is Odd

Sum of all numbers from 1 to 3 is: 6
```

---

## Technologies Used

- Python 3

---

## How to Run

1. Install Python 3 on your system.
2. Save the program file as `main.py`
3. Open terminal or command prompt.
4. Run the following command:

```bash
python main.py
```

---

## Program Menu

```text
1. Generate a pattern
2. Analyze a Range of numbers
3. Exit
```

---

## Code Overview

### Pattern Generation Logic

```python
for i in range(1, rows + 1):
    print("*" * i)
```

### Even/Odd Analysis

```python
label = "Even" if num % 2 == 0 else "Odd"
```

### Sum Calculation

```python
total_sum += num
```

---

## Sample Run

```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a pattern
2. Analyze a Range of numbers
3. Exit

Enter your choice: 1
Enter the number of rows for pattern: 5

Pattern:
*
**
***
****
*****
```

---

## Future Improvements

- Add more pattern types
- Include prime number checking
- Add menu looping enhancements
- Add graphical interface (GUI)

---

## Author

Created using Python for learning loops, conditionals, and user input handling.
