# Basic email slicing programme

email = input("enter your email:")
# index = email.index("@")
username = email[:email.index("@")]
domain = email[email.index("@") + 1 :]

print(f"your username is : {username} and domain is : {domain}")