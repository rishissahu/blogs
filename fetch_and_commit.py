import os
import random
import string
import subprocess
import time
from datetime import datetime

# Generate random text
def generate_random_text():
    length = random.randint(50, 200)  # Random length between 50 and 200 characters
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

# Write the text to a file
def write_to_file(file_name="random_text.md"):
    random_text = generate_random_text()
    with open(file_name, 'w') as file:
        file.write(f"# Random Text Generated at {datetime.now()}\n\n")
        file.write(random_text + "\n")
    print(f"Written random text to {file_name}")

# Commit and push changes to GitHub
def commit_and_push():
    try:
        # Configure Git (replace with your name/email)
        subprocess.run(["git", "config", "--global", "user.name", "Rishi Sahu"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "l.rishissahu@gmail.com"], check=True)

        # Add changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit with a random message
        commit_message = f"Random commit at {datetime.now()}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(f"Committed and pushed: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error during commit/push: {e}")

if __name__ == "__main__":
    while True:
        # Perform commit and push every 10 seconds
        write_to_file()
        commit_and_push()
        print("Waiting for 10 seconds before the next commit...")
        time.sleep(10)  # Wait for 10 seconds
