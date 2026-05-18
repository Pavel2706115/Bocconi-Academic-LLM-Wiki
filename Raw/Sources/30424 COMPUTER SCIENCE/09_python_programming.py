#!/usr/bin/env python
# coding: utf-8

# <img src="https://www.dpo.rwth-aachen.de/global/show_picture_asis.asp?id=aaaaaaaabftpwfx" width=200 height=200 align="left" /> <img src="https://www.dpo.rwth-aachen.de/global/show_picture_asis.asp?id=aaaaaaaabftpxde" width=200 height=200 align="right" />

# <h1><center> Introduction to Programming for Business Analytics </center></h1>  
# 
# <a href="mailto:ipba@dpo.rwth-aachen.de">ipba@dpo.rwth-aachen.de</a> <br>

# ## Lecture 9: Python Programming

# ### Outline    
# - Fundamentals
#     - The Python Programming Language.
#     - The Python Interpreter.
#     - Python as a Calculator: Math Operations.
#     - Assignment and Reassignment Statements.
#     - Elementary Functions
# - Elementary Data Types
#     - Integers and Floating-point Numbers.
#     - Boolean values.
# - Control Flow.
#     - The while-loop.
#     - Conditional Execution.
#     - The for-loop.
#     - Strings.
#     - Lists.
#     - Dictionaries.
# - Functions.    
#     - The Standard Form.
#     - Function Call and the Flow of Execution.
#     - Parameterized and Nullary Functions.
#     - Fruitful and Void Functions.
#     - Tuples.
#     - Important Characeristics of Functions.
#     - Recursion.
# 

# --------
# ### The Python Programming Language
# Python is a **high-level** programming language characterized by its **maturity** and **rich libraries** for scientific calculus and data science applications.
# 
# - The first step to writing Python code is to download the language.
#     - To download the language go to: https://www.python.org/downloads/.
#     - Please refer to the installation guide on the course website for a step-by-step guide on how to install Python.    

# -------
# ### The Python Interpreter
# 
# Similarly to the Julia REPL, Python has a so-called *Python interpreter* that reads and executes Python code.
# 
# To open the *Python interpreter* in:
# - **Windows:** 
#     - Press the Windows key.
#     - Type `python` and hit the return key `↵`.
# - **MacOS:** 
#     - Go to the Launchpad, and open a new Terminal.
#     - Type `python3` and hit the return key `↵`.
# 
# ![interpreter-3.png](attachment:interpreter-3.png)
# Note that the first few lines might be different for you, depending on your operating system.

# ---
# ### Python as a Calculator: Basic Maths Operations
# 
# We can use Python to perform addition (`+`), subtraction (`-`), multiplication (`*`) and division (`/`). (Note that, similarly to Julia, we can add comments using the `#` symbol.)

# In[ ]:


#addition
40+2


# In[ ]:


#subtraction
43-1 


# In[ ]:


#multiplication
6*7


# In[ ]:


#division 
84/2


# Differently from Julia, the exponentiation operator is `**` in Python.
# 
# Example: Evaluate the following mathematical expression $15000 (1 + 0.04)^5$.

# In[ ]:


15000*(1+0.04)**5


# The following tables show a summary of different arithmetic operations. 
# 
# 
# | Expression          | | Name       | | Description | | Example |                    
# |:--------------------|-|:-----------|-|:-------------------|-|:-------------|
# |`x + y`              | |binary plus | |performs addition        | |`40 + 2 = 42` |
# |`x - y`              | |binary minus| |performs subtraction        | |`43 - 1 = 42` |
# |`x * y`              | |times       | |performs multiplication        | |`6 * 7 = 42` |
# |`x / y`              | |divide      | |performs division        | |`84 / 2 = 42.0` |
# |`x // y`             | |floor divide| |$ x / y $, truncated to an integer       | |`9 // 4 = 2` |
# |`x ** y`             | |power       | |raises $x$ to the $y$th power       | |`3 ** 5 = 243` |
# |`x % y`              | |remainder   | |gives the remainder (equivalent to `rem(x,y)`)       | |`15 % 4 = 3` |

# ---
# ### Operator Precedence
# Similarly to Julia, Python also follows the mathematical convention **PEMDAS** when it comes to mathematical operators:<br>
# $\implies$ *parentheses* have the highest precedence in the evaluation order, followed by *exponentiation*, *multiplication/division*, and finally, *addition/subtraction*.

# ---
# ### Variables Assignment
# In Python, we can define variables and assign values to them using the assignment operator `=`.
# 
# Example: Let $a=15000, r=0.04$ and $t=5$. Use them to evaluate the expression $a (1+r)^t$.

# In[ ]:


a=15000
r=0.04
t=5
d=a*(1+r)**t


# ----
# ### Reassignment and Update Operators
# 
# Similarly to Julia, reassignment of variables to new values and using update operators (`+=`, `-=`, `*=`, etc) are also possible in Python.
# 
# Example: Let $a=20000$, increase the current value of $r$ by $0.01$, and revaluate the expression $a (1+r)^t$.

# In[ ]:


a  = 20000 # reassigning a to a new value
r += 0.01  # increasing the current value of r by 0.01

a*(1+r)**t


# ---
# ### Elementary (Built-in) Functions
# 
# Python provides many (built-in) functions which are essential for writing a program.
# 
# **Print statements:** One of the most basic built-in functions in Python is the `print` function. 
# - Note: Python's `print` function is similar to Julia's `println` function -- it adds a new line at the end of the displayed output.

# In[ ]:


print(a)
print(r)
print(t)
print(a*(1+r)**t)


# **Maths Functions:** 
# - We can also use the familiar maths functions (e.g., $\sqrt{x}$) in Python. 
# - However, (unlike Julia) many of them are not directly available for use. Instead, they are provided by the [`math` *module*](https://docs.python.org/3/library/math.html) from [Python Standard Library](https://docs.python.org/3/library/).
# 
# - To use the `math` module, we first need to load it using the following command.
#     ```python
#     import math
#     ```
# - Functions provided by the `math` module can then be used as follows.
#     ```python
#     math.function_name(p1, p2, ..., pn)
#     ```
#     - `math.` indicates that we are trying to access a function from the `math` module.
#     - `function_name` is the *name* of the function we are trying to use.
#     - `p1, p2, ..., pn` are parameters of the function `function_name` (if it has any). 
# 
# 
# - Example: Evaluate the expression $\sqrt{4}$ using the `sqrt` function provided by the `math` module. 

# In[ ]:


import math
math.sqrt(4)


# The following tables show a summary of different functions provided by [Python Standard Library](https://docs.python.org/3/library/). 
# 
# 
# 
# 
# 
# - Functions related to **powers, logs, and roots**:
# | Function | | Description | | Example |                    
# |:--------------------|-|:-----------|-|:-------------|
# | `math.sqrt(x)` | | square root ($\sqrt{x}$) of $x$ | | `math.sqrt(4) = 2.0` |
# | `math.hypot(x,y)` | | hypotenuse ($\sqrt{x^2 + y^2}$) of right-angled triangle with other sides of length $x$ and $y$ | | `x = 3`; `y = 4`; `math.hypot(x, y) = 5` |
# | `math.exp(x)` | | natural exponential function at $x$ | | `math.exp(1) = 2.718281828459045` |
# | `math.expm1(x)` | | accurate $e^x-1$ for $x$ near zero | | `math.expm1(1) = 1.718281828459045` |
# | `math.log(x)` | | natural logarithm of $x$ | | `math.log(4) = 1.3862943611198906` |
# | `math.log(x, b)` | | base $b$ logarithm of $x$ | | `math.log(8,4) = 1.5` |
# | `math.log2(x)` | | base $2$ logarithm of $x$ | | `math.log2(4) = 2.0` |
# | `math.log10(x)` | | base $10$ logarithm of $x$ | | `math.log10(4) = 0.6020599913279624` |
# | `math.frexp(x)` | | mantissa and exponent of $x$ | | `math.frexp(4) = (0.5,3)` |
# 
# 
# 
# - Functions related to **signs and absolute values**:
# | Function | | Description | | Example |                    
# |:--------------------|-|:-----------|-|:-------------|
# | `abs(x)` | | a positive value with the magnitude of $x$ | | `abs(-3) = 3` |
# | `math.copysign(x,y)` | | a value with magnitude of $x$ and sign of $y$ | | `x=1`; `y=-2`; `math.copysign(x, y) = -1` |
# 
# 
# - Functions related to **rounding values**:
# | Function | | Description | | Example |                    
# |:--------------------|-|:-----------|-|:-------------|
# | `round(x)` | | round $x$ to the nearest integer | | `round(1.7) = 2` |
# | `round(x, n)` | | round $x$ to the $n$ths digit | | `round(math.pi, 3) = 3.142` |
# | `math.floor(x)` | | round $x$ towards -Inf | | `math.floor(1.7) = 1` |
# | `math.ceil(x)` | | round $x$ towards +Inf | | `math.floor(1.7) = 2` |
# | `math.trunc(x)` | | round $x$ towards zero | | `math.trunc(1.7) = 1` |
# 
# 
# - The `math` module provides all standard **trigonometric** functions, including: `sin`, `cos`, `tan`, $\dots$.
#     - The following example finds `sin` of radians.

# In[ ]:


#import math
degrees = 45
math.sin(degrees / 180 * math.pi)


# ---
# ### Python Vocabulary and Grammar
#     
# - Python has the same variable/function *naming convention* as Julia. Namely, variable/function names should follow two rules:
#     1. Start with letters (A-Z or a-z) or few other characters (e.g., `_`) but NOT digits.
#     2. Continue with letters (A-Z or a-z), digits, underscore or exclamation mark (`!`).
# 
# 
# - Python has **keywords** which are *illegal* to use as variable or function *names*.
#     - Below is a list of Python reserved keywords which are illegal as variable names.
# |      |        |        |      |        |        |
# |:-----|--------|:-------|:-----|--------|:-------|
# |False |class   |finally |raise |with    |yield   |
# |None  |continue|for     |not   |or      |pass    |
# |True  |def     |from    |is    |lambda  |nonlocal|
# |and   |del     |global  |return|try     |while   |
# |as    |elif    |if      |break |except  |in      |
# |assert|else    |import  |

# ----
# ### Elementary Data Types
# - Similarly to Julia, in Python, every value has a data type that determines how we can use it.
# - In this lecture, we discuss the following five elementary data types in Python.
#     1. **`int`:** stores (positive and negative) *whole* numbers.
#     2. **`float`:** stores (positive and negative) numbers that have potential *decimal* places.
#     3. **`bool`:** stores two possible logical (*Boolean*) values: `True` and `False`.
#     4. **`str`:** a set of characters for representing *text*.
#     5. **`list`:** a data *container* that may contain more than one value.
# - The function `type` has one parameter and returns the data type of its argument.

# In[ ]:


type(1)


# In[ ]:


type(3.14)


# In[ ]:


type(True)


# In[ ]:


type("IPBA")


# In[ ]:


type([1, 3.14, True, "IPBA", []])


# ----
# ### Numeric Data Types: `int` and `float`
# - Python has three distinct numeric types: *integers* (`int`), *floating point* numbers (`float`), and *complex* numbers (`complex`). However, we limit the discussion to *integers* and *floating point* numbers.
# - Unlike Julia, Python does not classify `int` and `float` into subgroups based on the *bit* size. In other words, in Python, there is no such thing as `int64` and `bigint` or `float64` and `bigfloat`.

# In[ ]:


print(type(2))
print(type(2**63))
print(type(2**128))


# In[ ]:


print(type(2.0))
print(type(2.0**63))
print(type(2.0**128))


# ----
# ### Overflow Behavior
# 
# **Integers:** Python `int` values can be arbitrary large, and they do not (normally) overflow.
# - The memory size of the computer is the only limitation on how large an `int` value can be.

# In[ ]:


2**256


# In[ ]:


2**512


# In[ ]:


2**1024


# **Floats:** Python `float` values, on the other hand, have a hard limit and they do overflow.

# In[ ]:


2.0**256


# In[ ]:


2.0**512


# In[ ]:


2.0**1024


# - The system module `sys` can tell us what the *maximum* representable, positive, finite `float` value is.

# In[ ]:


import sys
sys.float_info.max


# ----
# ### Inaccuracy of `float`
# 
# - Similarly to Julia, Python `float` values are also prone to inaccuracy.

# In[ ]:


0.1 + 0.2


# - The `math` module provides the function `isclose` which helps us take this inaccuracy into account.

# In[ ]:


#import math
math.isclose(0.1+0.2, 0.3)


# ----
# ### `float` Special Values
# - Similarly to Julia, in Python, the number `0.0` is represented in two ways:

# In[ ]:


print(0.0*1)
print(0.0*-1)


# - Unlike Julia, $\infty$ and $-\infty$ are not directly available in Python. However, both can be obtained from the `math` module.

# In[ ]:


#import math

print(math.inf)
print(-math.inf)


# - Although Python does not directly provide a "Not a Number" value for representing undefined results, we can obtain one from the `math` module which provides the floating point `nan` value.

# In[ ]:


math.nan


# ---
# ### The `bool` Data Type and Comparison Operators
# 
# The Python data type `bool` has two literals: `True` and `False`.
# 
# Example: Evaluate the following expressions.
# ```python
# print(-0.0      == 0.0)
# print(0.1 + 0.2 == 0.3)
# print(sys.float_info.max == sys.float_info.max + 1)
# print(type(math.inf) == int)
# ```

# In[ ]:


print(-0.0 == 0.0)
print(0.1 + 0.2 == 0.3)
print(sys.float_info.max == sys.float_info.max + 1)
print(type(math.inf) == int)


# Below is a list of common *comparison operators* in Python.
# 
# |Name                 | | Maths symbol| |Python syntax| |Example      |                     |
# |:--------------------|-|:------------|-|:-----------|-|:-------------|:--------------------|
# |Equality             | |$=$          | |`==`        | |`-0.0 == 0.0` |$\rightarrow$ `True` |
# |Inequality           | |$\neq$       | |`!=`        | |`-0.0 != 0.0` |$\rightarrow$ `False`|
# |Less than            | |$<$          | |`<`         | |`-0.0 < 0.0`  |$\rightarrow$ `False`|
# |Less than or equal   | |$\leq$       | |`<=`        | |`-0.0 <= 0.0` |$\rightarrow$ `True` |
# |Greater than         | |$>$          | |`>`         | |`-0.0 > 0.0`  |$\rightarrow$ `False`|
# |Greater than or equal| |$\geq$       | |`>=`        | |`-0.0 >= 0.0` |$\rightarrow$ `True` |

# ---
# ### Control Flow Generic Form
# 
# In Python, control flow statements have the following *generic form*.
# 
# ```
# HEADER:
#     BODY
# ```
# 
# - Similarly to Julia, in Python:
#     - `HEADER` declares the start, and the specifics, of the statement.
#     - `BODY` contains the part of the program being controlled.
#     
# - Differently to Julia, in Python:
#     - The `HEADER` **ends** with a *colon* (`:`).
#     - Expressions in `BODY` **must be** *indented* (i.e., indentation is necessary and not just for readability. 
#     - Control flow statement **do NOT** have a *termination expression* (i.e., `end` keyword).

# ----
# ### The `while`-loop Statement
# 
# A `while`-loop statement in Python has the following generic form.
# ```python
# while BOOLEAN_EXPRESSION:
#     BODY
# ```
# 
# Example: Recall the Julia code for the *Simple Countdown* example from Lecture 3 using a `while`-loop. 
# ```julia
# countdown = 10
# while countdown > 0
#     println(countdown)
#     countdown -= 1       
# end
# ```
# Here's how we do the same in Python.

# In[ ]:


countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1     


# ------
# ### Conditional Execution
# 
# Similarly to Julia, conditional execution in Python is done using an `if`-statement which has the following generic form.
# 
# ```Python
# if BOOLEAN_EXPRESSION:
#     BODY
# ```
# 
# - The header consists of the *keyword* `if`, followed by a *Boolean expression* (`BOOLEAN_EXPRESSION`), followed by *colon* (`:`).
# - The Boolean expression is the *condition* that determines whether the body of the statement is executed or not.
#     - `BOOLEAN_EXPRESSION` is `True` $\;\; \implies$ `BODY` will be executed.
#     - `BOOLEAN_EXPRESSION` is `False` $\implies$ `BODY` will NOT be executed.
# 
# 
# In the following example, we check *if* the value of `countdown` is even by using the modulus operator `%`.

# In[ ]:


countdown = 10
if countdown%2 == 0:
    print("countdown is even.")


# In[ ]:


countdown = 9
if countdown%2 == 0:
    print("countdown is even.")


# #### Alternative execution:
# 
# - Alternative execution (i.e., conditional execution with two possibilities) is done using the *keyword* `else` followed by a *colon* (`:`).

# In[ ]:


countdown = 10
if countdown%2 == 0:
    print("countdown is even.")
else:
    print("countdown is odd.")


# In[ ]:


countdown = 9
if countdown%2 == 0:
    print("countdown is even.")
else:
    print("countdown is odd.")


# #### Chained Conditional Execution 
# 
# - Chained conditional execution (i.e., conditional execution with more than two possibilities) is done using the *keyword* `elif`, followed by a `BOOLEAN_EXPRESSION`, followed by a *colon* (`:`).
# - The value of the `BOOLEAN_EXPRESSION` determines whether or not the respective branch is executed or not.

# In[ ]:


countdown = 10
while countdown > 0:
    if countdown%3 == 0:
        print(f"{countdown} is divisible by 3")
    elif countdown%2 == 0:
        print(f"{countdown} is divisible by 2")
    else:
        print(f"{countdown} is not divisible by 2 nor divisible by 3.")
    countdown -= 1


# #### Nested Conditional Execution 
# 
# Exercise.

# ----
# ### Propositional Logic Truths Tables
# 
# 
# 
# - In Python, the symbol for logical operator:
#     - ∨ (OR) is `or`.
#     - ∧ (AND) is `and`.
#     - ¬ (NOT) is `not`.
#     
# 
# - The following table shows the truth table for ∨, ∧, and ¬ using `or`, `and`, and `not`.
# 
# 
# |`p`    |`q`    |`p or q`| `p and q`| `not p`|
# |:------|:------|:-------|:---------|:-------|
# |`True` |`True` | `True` | `True`   | `False`|
# |`True` |`False`| `True` | `False`  | `False`|
# |`False`|`True` | `True` | `False`  | `True` |
# |`False`|`False`| `False`| `False`  | `True` |

# In[ ]:


p = [True, True, False, False]
q = [True, False, True, False]

for i in range(0, len(p)):
    print(p[i] or q[i], p[i] and q[i], not p[i])  


# In the following example, we display `countdown` only if it is:
# - divisible by `2` AND divisible by `3` $\implies$ `countdown%2 == 0 and countdown%3 == 0`.

# In[ ]:


countdown = 10
while countdown > 0:
    if countdown%2 == 0 and countdown%3 == 0: 
        print(countdown)
    countdown -= 1


# - divisible by `2` OR divisible by `3` $\implies$ `countdown%2 == 0 or countdown%3 == 0`.

# In[ ]:


countdown = 10
while countdown > 0:
    if countdown%2 == 0 or countdown%3 == 0: 
        print(countdown)
    countdown -= 1   


# ---
# ### Strings
# 
# Textual data in Python is handled with string literals (i.e., the data type `str`).
# 
# - Unlike Julia, Python does not support character types. Single characters, defined using *single*-quotes delimiters (`''`), are strings with length one.

# In[ ]:


type('a')


# There are in fact several ways to define a string literal.
# 
# - Using *single*-quotes delimiters (`''`):
# ```Python
# 'IPBA'
# ```
# - Using *double*-quotes delimiters (`""`):
# ```Python
# "IPBA"
# ```
# - Using *triple single*-quotes delimiters (`''''''`):
# ```Python
# '''IPBA'''
# ```
# 
# - Using *triple double*-quotes delimiters (`""""""`):
# ```Python
# """IPBA"""
# ```

# In[ ]:


print(type('IPBA'))
print(type("IPBA"))
print(type('''IPBA'''))
print(type("""IPBA"""))


# In[ ]:


'IPBA' == "IPBA" == '''IPBA''' == """IPBA""" 


# - Strings defined using triple single/double-quotes delimiters may span multiple lines.

# In[ ]:


my_multiple_line_str1 = '''
I am a string literal.
I am defined using triple single-quotes delimiters.
I span multiple lines.
'''


# In[ ]:


my_multiple_line_str2 = """
I am a string literal.
I am defined using triple double-quotes delimiters.
I span multiple lines.
"""


# In[ ]:


print(my_multiple_line_str1)
print(my_multiple_line_str2)


# - String literals defined using triple single/double-quotes are sometimes used like a comment to document specific segment of code. In such cases, the string literal is referred to as a **docstring**.

# #### Escape sequences
# 
# - The delimiters `'` and `"` are not part of the `str`'s value.
# - To have `'` and/or `"` as part of the `str`'s value, we must *escape* them.
# - Python's *escape character* is the backslash `\`.

# In[ ]:


print("I am a string that contains \' as a character.")
print("I am a string that contains \" as a character.")


# - Note that we can also *escape* the escape character (`\`) using the escape character itself.

# In[ ]:


print("I am a string that shows how to escape the escape character \\.")


# In[ ]:


print("In the Python code of the above examples, \"\\\"")
print("and \"\\\\\" are examples of what is known as an")
print("escape sequence.")


# - We can also use `\n` to create a linebreak,
# - and `\t` to create the tab whitespace `'	'`. 

# In[ ]:


print("We can use \"\\n\" to create a linebreak,\nand \"\\t\" to create the tab whitespace '\t'.")


# #### Converting to and from a `str` value
# - **`str` $\gets$:** We can use the built-in function `str` to convert other Python value to a `str`.

# In[ ]:


# str ← int
str(1)


# In[ ]:


# str ← float
str(3.14)


# In[ ]:


# str ← bool
str(-0.0 == 0.0)


# - **`str` $\to$:** We can convert a `str` value into other types.

# In[ ]:


# str → int
int('1')


# In[ ]:


# str → float
float("3.14")


# In[ ]:


# str → bool
bool("""True""")


# #### `str` values and print statements
# We can use `str` values in print statements.

# In[ ]:


x = 3;
y = 1;
print("x+y =", x+y)
print("x+y =", x+y, " and ", "x-y =", x-y)


# ----
# ### Lists
# - In Python, a `list` is a data *container* that may contain more than one value of any data type.
# - A `list` literal is a comma-separated (`,`) list of values inside the delimiters `[` and `]`.
# 
# Examples:

# In[ ]:


# an empty list
my_list1 = []


# In[ ]:


# a list containing 3 elements of the same type (int)
my_list2 = [1, 2, 3]


# In[ ]:


# a list containing 5 elements of different types
my_list3 = [1, 3.14, "IPBA", my_list2, []]


# ----
# ###  `str` vs. `list`: Similarities and Differences
# 
# 
# #### Similarities : 
# 
# - Python's `str` and `list` values share many characteristics. 
# - Values inside of lists and strings are stored sequentially.

# In[ ]:


my_string = "Hello, world!";
my_list = [6, 5, 4, 3, 2, 1]


# - To retrieve a value from a `str` or a `list`, we pass the index of the position to the *bracket operator* `[]`.
# - An **important** difference between Julia and Python is that Julia uses `1`-based indexing while Python uses **`0`-based indexing**.

# In[ ]:


print(my_string[0])
print(my_string[1])


# In[ ]:


print(my_list[0])
print(my_list[1])


# - The function `len` can tell us the number of elements in a `str` or a `list` value.

# In[ ]:


print(len(my_string))
print(len(my_list))


# - Since Python uses `0`-based indexing, the last position of a `str` or a `list` value (e.g., `x`) can be obtained by `len(x)-1`. 

# In[ ]:


print(my_string[13-1])
print(my_list[6-1])


# - The last position of a `str` or a `list` value also  has the index `-1`.
#     - Indexing from the end starts from `-1`, `-2`, and so on.

# In[ ]:


print(my_string[-1])
print(my_string[-2])


# In[ ]:


print(my_list[-1])
print(my_list[-2])


# - We can obtain a *slice* of a `str` or a `list` by passing a *range*.

# In[ ]:


print(my_string[0:3])
print(my_list[0:3])


# - Note that the range `0:3` does not return a `str` or a `list` containing the elements in positions `0`, `1`, `2` and `3` (i.e., `Hello` and `[6, 5, 4, 3]`, respectively). Instead, it returns the first `3`$-$`0` elements, starting from `0` (i.e., `Hel` and `[6, 5, 4]`, respectively).
# 
# - Passing the range `start:stop` returns a `str` or `list` slice containing the first |`stop`$-$`start`| elements starting from position number `start`.

# In[ ]:


print(my_string[7:12])
print(my_string[-6:-1])


# In[ ]:


print(my_list[2:5])
print(my_list[-4:-1])


# - Not specifying the `start` value assumes `start=0`.
# - Not specifying the `stop` value assumes `stop=len(x)`, where `x` is the `str` or `list` value we are slicing. 

# In[ ]:


print(my_string[:7])
print(my_string[7:])


# In[ ]:


print(my_list[:3])
print(my_list[3:])


# 
# #### Differences: 
# Similarly to Julia's `Vector` and `String` values, we can change the values contained in a Python `list`, but not the values contained in a `str` value.
# 
# - a `str` is an **immutable** data type.

# In[ ]:


word1 = "Hello, ";
word2 = "vorld!";


# In[ ]:


word2[0] = 'w'


# - a `list` is a **mutable** data type.

# In[ ]:


list_we_mutate = [3, 9]
print("list_we_mutate before we mutate = ", list_we_mutate)
list_we_mutate[1] = 4
print("list_we_mutate after we mutate  = ", list_we_mutate)


# ----
# ### `String` Concatenation and Interpolation
# 
# **Concatenation:** We can *concatenate* two `str` values in Python using the `+` operator.

# In[ ]:


word1 = "Hello, ";
word2 = "vorld!";
greeting = word1 + "w" + word2[1:]
print(greeting)


# In[ ]:


part1 = "We have said \"Hello, world!\" "
part2 = str(3) 
part3 = " times in this lecture!"
print(part1 + part2 + part3)


# **Interpolation:** We can *interpolate* into an `str` value in Python using `f`-strings.

# In[ ]:


print(f"Here is the 4th time: {greeting}")


# - In the above example, the literal prefix `f` tells Python that expressions inside the curly brackets `{}` are variables, and we want to use their values.
# - `f`-strings are powerful as we can use them to embed arbitrary Python expressions (including arithmetic) in an `str` value.

# In[ ]:


a = 3;
b = 4;
print(f"{a} * {b} = {a * b}.")


# ---
# ### The `append` and `extend` Methods
# 
# In certain situations, functions in Python are referred to as *methods*. We will discuss this in more details in the future. For now, you can simply view them as functions.
# 
# 
# 
# - **Append:** To insert one item at the end of a list, we use the `append` method.

# In[ ]:


list_we_append_to = [3,4];
print("list_we_append_to before we append to = ", list_we_append_to)

list_we_append_to.append(7)
print("list_we_append_to after we append 7 to = ", list_we_append_to)


# - **Extend:** To insert more than one item at the end of a list, we use the `extend` method.

# In[ ]:


list_we_extend_to = [3,4];
print("list_we_extend_to before we extend to = ", list_we_extend_to)

list_we_extend_to.extend([11, 18, 29])
print("list_we_extend_to after we extend [11, 18, 29] to = ", list_we_extend_to)


# #### Dictionaries (`dict`)
# Syntactically, dictionaries in Python are defined using *curly brackets* `{}`.
# - Similarly to Julia, we can initialize a dictionary to be empty and add key-value pairs to it one-by-one.

# In[ ]:


eng2de = {}

eng2de["one"] = "eins"
print(eng2de)

eng2de["two"] = "zwei"
print(eng2de)


# - We can initialize a dictionary with multiple key-value pairs. In particular:
#     - Differently from Julia, Python uses a colon (`:`) between every key and the associated value.
#     - Similarly to Julia, Python uses a comma (`,`) between every key-value pair.

# In[ ]:


eng2de = {"one":"eins", "two":"zwei", "three":"drei"}
print(eng2de)


# In[ ]:


eng2de["two"]


# In[ ]:


eng2de["four"]


# To get a collection of elements with the keys or values of a dictionary, we use the `keys()` or `values()` method, respectively.

# In[ ]:


print(eng2de.keys())
print(eng2de.values())


# ---
# ### Functions: Standard Form
# 
# - Python's user-defined functions, declared in the *standard form* have the following generic form.
# 
# ```Python
# def function_name(parameter1, parameter2, ...):
#     BODY
# ```
# 
# - The `Header` starts with keyword `def` and is followed by:
#     - the function *name* (`function_name`);
#     - the *delimiters* `()` -- which has the *parameters* `parameter1, parameter2, ...`;
#     - and a *colon* (`:`).
# 
# 
# - Example: Recall the function `concatenate_and_print` we defined in Lecture 4 using the Julia syntax.
#     - The function takes two string values (`first_string` and `second_string`) as parameters, *concatenates* them and *prints* the result.
# 
# ```julia
# function concatenate_and_print(first_string, second_string)
#     concatenated_string = first_string*second_string
#     print(concatenated_string)
# end
# ```
# 
# - Here's how we create a similar function in Python.

# In[ ]:


def concatenate_and_print(first_string, second_string):
    concatenated_string = first_string+second_string
    print(concatenated_string)


# In[ ]:


concatenate_and_print("water", "melon")


# ----
# #### Parameterized and Nullary Functions
# 
# Exercise.
# 
# #### User Input:
# - To obtain a user *input*, we use the function `input`.

# In[ ]:


print("What's your name?")
name = input()
print("My name is", name) 


# - Note that, similarly to Julia, the Python function `input` reads the user input as a string (`str` value).

# In[ ]:


type(name)


# #### Fruitful and Void functions:
# 
# - In Python, the value/s *returned* by a **fruitful** function must be declared explicitly using the `return` keyword.

# In[ ]:


def square(x):
    return x**2


# In[ ]:


result = square(5)
print(result)


# - Functions that do not contain the `return` keyword, or that only perform an action but do not return a value, are considered as **void** functions.

# In[ ]:


# Example of a void function that does not contain the return keyword
def square_void_1(x):
    x**2


# In[ ]:


# Example of a void function that only perform an action but do not return a value
def square_void_2(x):
    return print(x**2)


# - In particular, Python's void functions return the value `None`, which is a value of type `NoneType`. 

# In[ ]:


result_void_1 = square_void_1(5)
print(result_void_1)
type(result_void_1)


# #### The `return` keyword:
# 
# - The `return` keyword can also be used to:
#     1. Exit the function immediately. 
#     2. If the `return` keyword is followed by an expression, the value of the expression is returned.
#     3. We could also return multiple values by using a comma (`,`) between the expressions we want to return.
#   
#   
# - Example: Recall the Newton's method which is used to calculate the square root of `a` given a value `x ≠ 0` as the initial guess.

# In[ ]:


# the return keyword is used to exit the while-loop,

def newtons_square_root_1(a,x):
    y = (x + a/x) / 2
    while True:
        x = y
        y = (x + a/x) / 2
        if y == x:
            return


# In[ ]:


# the return keyword is used to
# (1) exit the while-loop,
# (2) return the value of x (√a)

def newtons_square_root_2(a,x):
    y = (x + a/x) / 2
    while True:
        x = y
        y = (x + a/x) / 2
        if y == x:
            return x


# In[ ]:


# the return keyword is used to
# (1) exit the while-loop,
# (2) return the value of x (√a) and `iteration`

def newtons_square_root_3(a,x):
    y = (x + a/x) / 2
    iteration = 0
    while True:
        x = y
        y = (x + a/x) / 2
        if y == x:
            return x, iteration
        else:
            iteration += 1


# In[ ]:


square_root_1 = newtons_square_root_1(81,0.00001)
print(square_root_1)


# In[ ]:


square_root_2 = newtons_square_root_2(81,0.00001)
print(square_root_2)


# In[ ]:


square_root_3 = newtons_square_root_3(81,0.00001)
print(square_root_3)


# Note that we could also assign the returned value of `newtons_square_root_3` into two separate variables.

# In[ ]:


square_root, number_of_iterations = newtons_square_root_3(81,0.00001)
print(square_root)
print(number_of_iterations)


# #### The Returned Value of Fruitful Functions:
# 
# - Similarly to Julia, the returned value of a fruitful function in Python does not have to be numeric.
# - The following shows an example of a fruitful *Boolean* (i.e., a function that returns a value of type `bool`).

# In[ ]:


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


# In[ ]:


print( is_divisible(10, 2) )
print( is_divisible( 9, 3) )
print( is_divisible( 8, 4) )
print( is_divisible( 7, 5) )
print( is_divisible( 6, 6) )


# ----
# ### Advanced Data Types
# 
# #### Tuples (`tuple`):
# 
# Similarly to Julia, tuples in Python have the followig properties:
# 
# - Syntactically, a tuple is a *comma-separated* list of values of any type (commonly enclosed in parentheses).

# In[ ]:


my_tuple = 'a', 'b', 'c', 'd', 'e'  


# - Tuples are indexed by integers.

# In[ ]:


print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[2:4])


# - Tuples are immutable.

# In[ ]:


my_tuple[2] = 'f'


# - Tuples store the output of fruitful functions that return multiple values.

# In[ ]:


q, r = divmod(7,3)
print(q)
print(r)


# ----
# ### Recursive Functions
# - It is also possible to define *recursive* functions in Python.

# In[ ]:


def my_factorial(n):
    if n == 0:
        return 1
    else:
        return n * my_factorial(n-1)


# In[ ]:


my_factorial(3)


# ---
# ### Summary: Looking Back and Looking Forward
# 
# **Looking Back:**
# - Python is a high-level programming language characterized by its maturity and rich libraries for scientific calculus and data science applications.
# - Similarly to the Julia REPL, Python has a so-called Python interpreter that reads and executes Python code.
# - We can use Python to perform addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`**`).
# - Python provides many (built-in) functions which are essential for writing a program such as the `print` function. 
# - Math functions: Many familiar maths functions (e.g., $\sqrt{x}$) are provided by the [`math` *module*](https://docs.python.org/3/library/math.html).
# - Python has two numeric data types for real numbers `int` and `float`, and they are not classified into further subgroups based on the bit size.
# - The data type `bool` has two possible logical (Boolean) values: `True` and `False`.
# - Control flow statements have the same generic form as in Julia except that 
#     - The `HEADER` **ends** with a *colon* (`:`).
#     - Expressions in `BODY` **must be** *indented*. 
#     - They **do NOT** have a *termination expression*.
# - Conditional execution: The keyword `elif` indicates chained execution.
# - Logical operators:
#     - ∨ (OR) is `or`
#     - ∧ (AND) is `and`
#     - ¬ (NOT) is `not`.
# - `str`: a set of characters for representing text. 
# - We can define an `str` value using single-quotes (`''`), double-quotes (`""`), triple single-quotes (`''''''`), and triple double-quotes (`""""""`).
# - We can concatenate two strings using the `+` operator and interpolate using an `f`-string.
# - To insert one item or more than one item at the end of a list, we use the `append` or `extend` method, respectively.
# -  Python dictionaries are defined using curly brackets `{}` where:
#     - every key-value pair is coupled with a colon (`:`)
#     - different key-value pairs are separated with a comma (`,`).
# - Tuples in Python have the same properties as in Julia.
# - Python uses `0`-based indexing.
# - Python's user-defined functions are declared using the keyword `def`.
# - The value/s returned by a fruitful function must be declared explicitly using the `return` keyword.
# - The `return` keyword can also be used to exit the function immediately.
# 
# 
# 
# **Looking Forward:**
# Lbraries: NumPy, Pandas, Matplotlib
