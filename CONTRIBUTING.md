

We are very happy that you consider implementing algorithms and data structure for others! This repository is referenced and used by learners from all over the globe. Being one of our contributors, you agree and confirm that:

- You did your work - no plagiarism allowed
  - Any plagiarized work will not be merged.
- Your work will be distributed under [MIT License](License) once your pull request is merged
- You submitted work fulfils or mostly fulfils our styles and standards

**New implementation** is welcome! For example, new solutions for a problem, different representations for a graph data structure or algorithm designs with different complexity.

**Improving comments** and **writing proper tests** are also highly welcome.


### Contribution

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing complex algorithms. Please read this section if you are contributing your work.

#### What is an Algorithm?

An Algorithm is one or more functions (or classes) that:
* take one or more inputs,
* perform some internal calculations or data manipulations,
* return one or more outputs,
* have minimal side effects (Ex. print(), plot(), read(), write()).

Algorithms should be packaged in a way that would make it easy for readers to put them into larger programs.

Algorithms should:
* have intuitive class and function names that make their purpose clear to readers
* use Python naming conventions and intuitive variable names to ease comprehension
* be flexible to take different input values
* have Python type hints for their input parameters and return values
* raise Python exceptions (ValueError, etc.) on erroneous input values
* have docstrings with clear explanations and/or URLs to source materials
* contain doctests that test both valid and erroneous input values
* return all calculation results instead of printing or plotting them

Algorithms in this repo should not be how-to examples for existing Python packages.  Instead, they should perform internal calculations or manipulations to convert input values into different output values.  Those calculations or manipulations can use data types, classes, or functions of existing Python packages but each algorithm in this repo should add unique value.

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- Please write in Python 3.7+.  __print()__ is a function in Python 3 so __print "Hello"__ will _not_ work but __print("Hello")__ will.
- Please focus hard on naming of functions, classes, and variables.  Help your reader by using __descriptive names__ that can help you to remove redundant comments.
  - Single letter variable names are _old school_ so please avoid them unless their life only spans a few lines.
  - Expand acronyms because __gcd()__ is hard to understand but __greatest_common_divisor()__ is not.
  - Please follow the [Python Naming Conventions](https://pep8.org/#prescriptive-naming-conventions) so variable_names and function_names should be lower_case, CONSTANTS in UPPERCASE, ClassNames should be CamelCase, etc.

- We encourage the use of Python [f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python) where the make the code easier to read.

- Please consider running [__psf/black__](https://github.com/python/black) on your Python file(s) before submitting your pull request.  This is not yet a requirement but it does make your code more readable and automatically aligns it with much of [PEP 8](https://www.python.org/dev/peps/pep-0008/). There are other code formatters (autopep8, yapf) but the __black__ formatter is now hosted by the Python Software Foundation. To use it,

  ```bash
  pip3 install black  # only required the first time
  black .
  ```

- Original code submission require docstrings or comments to describe your work.

- More on docstrings and comments:

  If you used a Wikipedia article or some other source material to create your algorithm, please add the URL in a docstring or comment to help your reader.

  The following are considered to be bad and may be requested to be improved:

  ```python
  x = x + 2	# increased by 2
  ```

  This is too trivial. Comments are expected to be explanatory. For comments, you can write them above, on or below a line of code, as long as you are consistent within the same piece of code.

  We encourage you to put docstrings inside your functions but please pay attention to indentation of docstrings. The following is a good example:

  ```python
  def sum_ab(a, b):
      """
      Return the sum of two integers a and b.
      """
      return a + b
            
- Avoid importing external libraries for basic algorithms. Only use those libraries for complicated algorithms.
- If you need a third party module that is not in the file __requirements.txt__, please add it to that file as part of your submission.

#### Other Standard While Submitting Your Work

- File extension for code should be `.py`. Jupyter notebook files are acceptable in machine learning algorithms.
- Strictly use snake_case (underscore_separated) in your file_name, as it will be easy to parse in future using scripts.
- Please avoid creating new directories if at all possible. Try to fit your work into the existing directory structure.
- If possible, follow the standard *within* the folder you are submitting to.
- If you have modified/added code work, make sure the code compiles before submitting.
- If you have modified/added documentation work, ensure your language is concise and contains no grammar errors.
- Do not update the README.md or DIRECTORY.md file which will be periodically autogenerated by our Travis CI processes.
- Add a corresponding explanation to [Algorithms-Explanation](https://github.com/TheAlgorithms/Algorithms-Explanation) (Optional but recommended).
- All submissions will be tested with [__mypy__](http://www.mypy-lang.org) so we encourage to add [__Python type hints__](https://docs.python.org/3/library/typing.html) where it makes sense to do so.

- Most importantly,
  - **Be consistent in the use of these guidelines when submitting.**
  - Happy coding!
