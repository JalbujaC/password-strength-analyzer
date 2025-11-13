# Password Strength Analyzer

A Python-based **command-line tool** to evaluate the strength of passwords.
The analyzer considers:

* Character diversity (uppercase, lowercase, numbers, special characters)
* Password length
* Entropy estimation (in bits)
* Common password detection (against a dictionary file)
* Color-coded output and feedback for easy interpretation

This tool is ideal for learning about password security and building practical cybersecurity utilities.

---

## Project Structure

password-strength-analyzer/
│
├── panalyzer.py           # Main Python CLI program
├── Data/
│   └── english3.txt      # Common password / dictionary file
├── requirements.txt      # External dependencies
└── README.md             # This file


---

## Installation

1. Clone the repository:

```bash
git clone git clone https://github.com/JalbujaC/password-strength-analyzer.git
cd password-strength-analyzer
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the analyzer from the command line:

```bash
python panalyzer.py --p "MySecurePassword123!"
```

### Example Output:

**Strong password example:**

```
=== Password Analysis ===
Password: MySecurePassword123!
Entropy: 113.75 bits
Score: 6
```

**Weak password example:**

```
=== Password Analysis ===
Password: password123
Entropy: 45.47 bits
Score: 3
Your password is too common. Choose a stronger one.

Feedback:
- Add uppercase letters.
- Add special characters.
```

> The score and feedback are color-coded using `colorama` for easy interpretation:
>
> * Red → Weak
> * Yellow → Moderate
> * Green → Strong
> * Yellow → Feedback

---

## How It Works

1. **Character Diversity:**
   Checks if the password contains lowercase, uppercase, numbers, and special characters.

2. **Length Check:**
   Passwords shorter than 8 characters receive a lower score.

3. **Entropy Estimation:**
   Calculates entropy in bits based on the variety of characters and length.

4. **Common Password Check:**
   Compares against a dictionary file (`english3.txt`) to flag easily guessable passwords.

5. **Feedback:**
   Provides actionable suggestions for improving password strength.

---

## Dependencies

* Python 3.8+
* `colorama` (for color-coded CLI output)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the **MIT License** – see `LICENSE` for details.

---

## Acknowledgements

Inspired by common password security principles and cybersecurity learning projects. 
