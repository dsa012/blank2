import random


def validate_input(n):
    if len(n) < 1:
        assert len(n) > 1, "Incorrect format."
    if n[0] == "-":
        if n[1:].isdigit():
            return int(n)
    if n.isdigit():
        return int(n)
    assert n.isdigit(), "Incorrect format."

def generate_question(level):
    if level == 1:
        n1 = random.randint(2, 9)
        n2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        equation = f"{n1} {operator} {n2}"
        ans = 0
        if operator == '*':
            ans = n1 * n2
        elif operator == '-':
            ans = n1 - n2
        else:
            ans = n1 + n2
        return equation, ans
    elif level == 2:
        n = random.randint(11, 29)
        product = n * n
        return n, product


level = 0
lvl1_desc = "simple operations with numbers 2-9"
lvl2_desc = "integral squares 11-29"
while True:
    try:
        level = validate_input(input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n"""))
        if level not in [1, 2]:
            raise AssertionError
    except AssertionError as err:
        print(err)
    else:
        break
score = 0
for i in range(5):
    question, ans = generate_question(level)
    print(question)
    while True:
        try:
            user_ans = validate_input(input())
        except AssertionError as err:
            print(err)
        else:
            break
    if user_ans == ans:
        print("Right!")
        score += 1
    else:
        print("Wrong!")
print(f"Your mark is {score}/5.")

dosave = input("Would you like to save your result to the file? Enter yes or no.")
if dosave.lower() in ['y', 'yes']:
  username = input("What is your name?")
  description = f"{username}: {score}/5 in level {level} ({lvl1_desc if level == 1 else lvl2_desc})."
  with open("results.txt", "a") as file:
    file.write(description)
  print("The results are saved in \"results.txt\".")