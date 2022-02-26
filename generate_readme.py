import app
import exams
import login
import questions
from inspect import getmembers, isfunction
import sys

sys.stdout.write("")
modules = [app, exams, login, questions]

for module in modules:
    sys.stdout.write(f"# `{module.__name__}` endpoints\n")
    for member in getmembers(exams, isfunction):
        if member is not None:
            sys.stdout.write(f"## `{member[0]}`\n")
            sys.stdout.write(f"""```{member[1].__doc__}```""")
            sys.stdout.write("\n\n")
    # sys.stdout.write("===========\n")