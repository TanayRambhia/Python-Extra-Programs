import re

def validate_email(email):
    # Define a regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match() function to match the pattern against the email address
    if re.match(pattern, email):
        return ('Valid Email')
    else:
        return ('InValid Email')

# Test the function with some example email addresses
print(validate_email('tanayrambhia204@example.com'))   
