"""Session 1.5 demo — dictionaries (labeled key->value data)."""

user = {"name": "Ada", "email": "ada@example.com", "age": 36}

# Look up by key
print(user["name"])

# .get() avoids an error if the key is missing
print(user.get("phone", "no phone on file"))

# Add or update
user["age"] = 37
user["city"] = "London"

# Loop over key/value pairs
for key, value in user.items():
    print(f"{key}: {value}")
