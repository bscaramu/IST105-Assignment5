#!/usr/bin/python3
import cgi
import random
import math

# Retrieve user input from form
form = cgi.FieldStorage()
number = int(form.getvalue("number"))
text = form.getvalue("text")

# Task 1: Number Puzzle
if number % 2 == 0:
    number_result = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
else:
    number_result = f"The number {number} is odd. Its cube is {number ** 3}."

# Task 2: Text Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

# Task 3: Treasure Hunt
secret_number = random.randint(1, 100)
attempts = []
for attempt in range(1, 6):
    guess = random.randint(1, 100)
    if guess == secret_number:
        attempts.append(f"Attempt {attempt}: {guess} (Correct!!!)")
        break
    elif guess < secret_number:
        attempts.append(f"Attempt {attempt}: {guess} (Too low!!!)")
    else:
        attempts.append(f"Attempt {attempt}: {guess} (Too high!!!)")

# HTML output
print("Content-type: text/html\n")
print("<html><head><title>Results</title></head><body>")
print(f"<h2>Number Puzzle</h2><p>{number_result}</p>")
print(f"<h2>Text Puzzle</h2><p>Binary: {binary_text}</p>")
print(f"<p>Vowel Count: {vowel_count}</p>")
print("<h2>Treasure Hunt</h2>")
print("<p>The secret number was: " + str(secret_number) + "</p>")
print("<ul>")
for attempt in attempts:
    print(f"<li>{attempt}</li>")
print("</ul>")
print("</body></html>")
