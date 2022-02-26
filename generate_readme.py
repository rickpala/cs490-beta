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
    for name, func in getmembers(module, isfunction):
        if name is not None:
            sys.stdout.write(f"## `{name}`\n")
            sys.stdout.write(f"```\n"
                             f"{func.__doc__}\n"
                             f"```")
            sys.stdout.write("\n\n")
    # sys.stdout.write("===========\n")