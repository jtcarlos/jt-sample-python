# Sample Python Code

A sample Python code that demonstrates the creation of a package with two (2) modules, named `basic` and `physics`.

This practice code also demonstrates unit testing using the built-in `unittest` library of Python as well as showcasing a Python code that follows PEP8 linting through `PyLint`.

### Running the unit test

To run the test cases specified in the unit test file `mathlib.test.py`, you may execute the following command

```
python mathlib.test.py
```

### Linting the code

To validate if the code follows the PEP8 Python coding guidelines, you may execute the following commands.

```
> pip install pylint           // NOTE: optional depending if you have PyLint installed

> pylint mathlib               // Lints the 'mathlib' package and its modules
> pylint mathlib.test.py       // Lints the 'mathlib.test.py' file
> pylint main.py               // Lints the 'main.py' file
```

### Running the `main.py` file

To run the `main.py` file you may execute the following command

```
python main.py
```
