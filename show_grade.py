"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "c0784dc0c048aab79b14abbbea345584"
GRADE_HASH = "2e38d9e507886d251f3916b22bd47bd97a6757453548ea0e3067a5d55cacf6c7"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
