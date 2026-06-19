import string

password = input("Enter password: ")


try:
    with open("rockyou.txt", "r", encoding="latin-1") as file:
        passwords = set(line.strip().lower() for line in file)

    if password.lower() in passwords:
        print("\n Password found in RockYou database!")
        print("Choose a different password.")
        exit()

except FileNotFoundError:
    print("rockyou.txt not found.\n")

score = 0
feedback = []


if len(password) >= 12:
    score += 1
else:
    feedback.append("Use at least 12 characters")


if any(c.isupper() for c in password):
    score += 1
else:
    feedback.append("Add uppercase letters")


if any(c.islower() for c in password):
    score += 1
else:
    feedback.append("Add lowercase letters")


if any(c.isdigit() for c in password):
    score += 1
else:
    feedback.append("Add numbers")


if any(c in string.punctuation for c in password):
    score += 1
else:
    feedback.append("Add special characters")


ratings = {
    5: "Very Strong",
    4: "Strong",
    3: "Moderate",
    2: "Weak",
    1: "Very Weak",
    0: "Very Weak"
}

print(f"\nPassword Strength: {ratings[score]}")
print(f"Score: {score}/5")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)