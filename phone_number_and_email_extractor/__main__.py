import pyperclip
from functions import extract_emails, extract_phone_numbers

text = str(pyperclip.paste())
matches = extract_phone_numbers(text).extend(extract_emails(text))

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
