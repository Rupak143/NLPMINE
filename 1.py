import re

# Sample text to search
text = """
John's email is john.doe@example.com, and Jane's email is jane_doe123@example.org.
You can also contact admin at support@example.net or call (555) 123-4567.
"""

# Example 1: Match all email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Emails found:", emails)

# Example 2: Search for phone numbers in the format (xxx) xxx-xxxx
phone_numbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', text)
print("Phone numbers found:", phone_numbers)

# Example 3: Check if a specific word exists in the text
word_to_search = "admin"
if re.search(rf'\b{word_to_search}\b', text):
    print(f"The word '{word_to_search}' is present in the text.")
else:
    print(f"The word '{word_to_search}' is not found in the text.")

# Example 4: Replace all domain names with "[REDACTED]"
redacted_text = re.sub(r'@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', '@[REDACTED]', text)
print("\nText after domain redaction:")
print(redacted_text)

# Example 5: Extract just the usernames from email addresses
usernames = re.findall(r'\b([A-Za-z0-9._%+-]+)@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("\nUsernames from emails:", usernames)

# Example 6: Match lines that start with "You"
lines_starting_with_you = re.findall(r'^You.*', text, flags=re.MULTILINE)
print("\nLines starting with 'You':", lines_starting_with_you)
