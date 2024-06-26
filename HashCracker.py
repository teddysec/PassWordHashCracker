import hashlib
import os


def hash_cracker(password_hash, password_list):
    """Password hash crack using a common password list."""
    for password in password_list:
        # Hash the password using MD5
        hashed_password_md5 = hashlib.md5(password.encode()).hexdigest()
        if hashed_password_md5 == password_hash:
            return password

        # Hash the password using SHA-256
        hashed_password_sha256 = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password_sha256 == password_hash:
            return password

    # Return None if password is not found
    return None


if __name__ == "__main__":
    # Check if the password file exists
    if not os.path.isfile("Password.txt"):
        print("Password file not found.")
        exit()

    # Read the password file with 'utf-8' encoding
    with open("Password.txt", "r", encoding="utf-8") as file:
        password_list = [line.strip() for line in file]

    password_hash = input("Enter a password hash to crack: ")

    # Attempt to crack the password hash
    cracked_password = hash_cracker(password_hash, password_list)

    # Print result
    if cracked_password:
        print("Password cracked:", cracked_password)
    else:
        print("Failed to crack the hashed password.")
