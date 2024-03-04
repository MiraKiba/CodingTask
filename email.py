class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# Initialize an empty list to store emails
inbox = []

# Function to populate the inbox with sample emails
def populate_inbox():
    # Sample data
    sample_emails = [
        {"email_address": "sender1@example.com", "subject_line": "Welcome to HyperionDev!", "email_content": "Content of the first email."},
        {"email_address": "sender2@example.com", "subject_line": "Great work on the bootcamp!", "email_content": "Content of the second email."},
        {"email_address": "sender3@example.com", "subject_line": "Your excellent marks!", "email_content": "Content of the third email."}
    ]
    # Create Email objects and add them to the inbox list
    for email_data in sample_emails:
        email = Email(email_data["email_address"], email_data["subject_line"], email_data["email_content"])
        inbox.append(email)

# Function to list emails
def list_emails():
    print("Inbox:")
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")

# Function to read an email
def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} with subject '{email.subject_line}'")
        print("Content:")
        print(email.email_content)
    else:
        print("Invalid email index.")

# Main function to simulate email application
def main():
    populate_inbox()

    while True:
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            index = int(input("Enter the index of the email to read: "))
            read_email(index)
        elif choice == '2':
            list_emails()
        elif choice == '3':
            print("Quitting application...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()