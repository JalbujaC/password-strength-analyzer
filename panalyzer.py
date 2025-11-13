import re
import math
import argparse
from pathlib import Path
from colorama import init, Fore, Style

parser = argparse.ArgumentParser(description="Password Analyzer - Evaluate the strength of a password.")
parser.add_argument("--p", type=str, help="The password you wish to evaluate.")
args = parser.parse_args()

inputted_password = args.p

init(autoreset=True)

score = 0
feedback = []


def load_wordlists():
    base_dir = Path(__file__).parent
    file_path = base_dir / "Data" / "english3.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().splitlines()
    
dictionary = load_wordlists()


def password_strength(inputted_password: str) -> dict:

    global score
    global feedback

    # Check use of character types
    if re.search(r'[a-z]', inputted_password):
        score += 1
    else: 
        feedback.append("Add lowercase letters to your password.")
    if re.search(r'[A-Z]', inputted_password):
        score += 1
    else: 
        feedback.append("Add uppercase letters to your password.")
    if re.search(r'\d', inputted_password):
        score += 1
    else: 
        feedback.append("Add numbers to your password.")
    if re.search(r"[^A-Za-z0-9]", inputted_password):
        score += 1
    else: 
        feedback.append("Add special characters to your password.")
    
    # Check length of password
    length = len(inputted_password)
    if length >= 8:
        score += 1
    else:
        feedback.append("Your password is too short. Recommend at least 8 characters.")
    
    return {
        "password": inputted_password,
        "score": score,
        "feedback": feedback,
    }


# Calculate entropy of password
def entropy(inputted_password: str):
    pool = 0
    lowercase = False
    uppercase = False
    digits = False
    special = False
    if re.search(r'[a-z]', inputted_password):
        pool += 26
        lowercase = True
    if re.search(r'[A-Z]', inputted_password):
        pool += 26
        uppercase = True   
    if re.search(r'\d', inputted_password):
        pool += 10
        digits = True
    if re.search(r'[^A-Za-z0-9]', inputted_password):
        pool += 32
        special = True


    entropy_value = math.log2(pool ** len(inputted_password)) if pool > 0 else 0 
    return {
        "entropy_bits": round(entropy_value, 2)
    }

# Check password against common passwords list and patterns
def commonality(inputted_password, dictionary):
    global score

    for word in dictionary:
        if inputted_password.lower() == word.lower():
            return {
                "common": True,
                "message": "Your password is too common. Choose a less common password."
            }
        else:
            score += 1
    return False



strength_result = password_strength(inputted_password)
entropy_result = entropy(inputted_password)
commonality_result = commonality(inputted_password, dictionary)

print("\n")
print("\n")
print("\n")

print("\n=== Password Analysis ===")
print(f"Password: {strength_result['password']}")
if strength_result['score'] >= 5:
    print(Fore.GREEN + f"Score: {strength_result['score']}")
elif strength_result['score'] == 4:
    print(Fore.YELLOW + f"Score: {strength_result['score']}")
elif strength_result['score'] <= 3:
    print(Fore.RED + f"Score: {strength_result['score']}")

if entropy_result['entropy_bits'] >= 60:
    print(Fore.GREEN + f"Entropy: {entropy_result['entropy_bits']} bits")
elif 40 <= entropy_result['entropy_bits'] < 60:
    print(Fore.YELLOW + f"Entropy: {entropy_result['entropy_bits']} bits")
elif entropy_result['entropy_bits'] < 40:
    print(Fore.RED + f"Entropy: {entropy_result['entropy_bits']} bits")

if commonality_result:
    print(Fore.YELLOW + commonality_result["message"])

if strength_result["feedback"]:
    print("\nFeedback:")
    for f in strength_result["feedback"]:
        print(Fore.YELLOW + f"- {f}")