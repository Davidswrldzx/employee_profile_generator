# Employee Profile Generator

I built this project in Python while working through an employee card workshop. It helped me practice working with text, numbers, and variables.

## What the program does

The program puts together an employee's name, address, age, work experience, job title, and salary. It prints an employee card and pulls the department, year, initials, and ID from an employee code.

The details are sample values stored in the code. You can change them in `employee_profile.py`.

## How to run it

You need Python 3.6 or newer. You do not need to install any extra packages.

Download the project, open a terminal in the project folder, and run:

```bash
python employee_profile.py
```

If your computer uses `python3`, run:

```bash
python3 employee_profile.py
```

## Output

```text
John
Doe
John Doe
123 Main Street, Apartment 4B
John Doe is 28 years old
Experience: 5 years
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
DEV
2026
JD
001
```

## What I learned

I used variables to store text and numbers. I joined strings with `+` and used `+=` to add the apartment number to the address.

I learned that Python cannot join a string and an integer directly with `+`. When I tried adding the employee's age to a sentence, I got a `TypeError`. I fixed it by using `str(employee_age)`.

Later, I used formatted strings to put several values into the employee card. This made the code easier to read.

I also practiced string slicing. For example, `employee_code[0:3]` gets the department, and `employee_code[-3:]` gets the last three characters for the ID.

## Files

`employee_profile.py` contains the program.

`LEARNING_LOG.md` records the 17 workshop steps.

`.gitignore` keeps Python cache files and local environments out of the project.
