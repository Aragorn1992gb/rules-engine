# rules-engine

This project implement a rules-engine. 

### Example of rules:


```
Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000
```

### Requirements

These rules need to be configurable and variable in several ways:
- The number of comparisons
- The variables referenced (e.g. replacing `credit_rating` with something else)
- The constant values being compared against
- The operators being used (e.g. greater than, less than, equals)
- The structure of the boolean composition (i.e where AND/OR/etc are, and where the parentheses are)


### Implementation

The imput should be like this:

```python
EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}
```

And the output, following the rules above, in this case will return:

```python
True
```

### Technologies

- Python3
- pytest

### Data Structure

- Binary Tree

### Init

To install the dependences, open a terminal from the main folder.

Create a virtual env:
```py -m venv env```

Acrivate the virtual env.
Linux:
```source env/bin/activate```
Windows:
```source env/bin/activate```

Install the dependencies:
```pip install -r requirements.txt```
If problems, try eith:
```python -m pip install -r requirements.txt```

The only dependency to be installed is pytest. I chose it because it is the most commonly used Python library for tests.

To run the program, you can just run (outside env) the main.py.
To run the tests (outside env):
```pytest test.py```

There is a default Rule but you can change it. To change, when you run main .py, answer with "y" to the question about changing the rule. The Role data structure is a binary tree, so you have to  put the right side and left side of the comparision. When you define a rule, need to define the operator or comparator, variable name end value of the comparator. 
Operator can be AND, OR or XOR defined as follows:
    and_ -> AND
    or_ -> OR
    xor -> XOR
Comparator can be <, <=, ==, !=, >=, > defined as follows:
    lt -> <
    le -> <=
    eq -> ==
    ne -> !=
    ge -> >=
    gt -> >

So, if you want to define a rule like:

```
Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000
```

You will follow those steps:
Do you want to change the rule? (y or n) 
```y```
Insert new Rule operator or comparator:
```or_```
Insert left side
    Insert new Rule operator or comparator:
    ```and_```
        Insert left side
        Insert new Rule operator or comparator:
        ```gt```
            Insert left side
            ```credit_rating```
            Insert right side
            ```50```
        Insert right side
        Insert new Rule operator or comparator:
        ```lt```
            Insert left side
            ```flood_risk```
            Insert right side
            ```10```
Insert right side:
Insert new Rule operator or comparator:
```gt```
    Insert the left Side
    ```revenue```
    Insert the right side
    ```1000000```

Then, need to define data. The system will ask you if do you want to add a new variable. For this variable you need the put name and value.
For example, if you want to put input data like those:

```
EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}
```
You will follow those steps:

Put your data
Variable name: 
```credit_rating```
Variable value: 
```55```
Do you want to add other variables? (y or n)
```y```
Variable name: 
```flood_risk```
Variable value: 
```5```
Do you want to add other variables? (y or n)
```y```
Variable name: 
```revenue```
Variable value: 
```1000```

Missing variables are considered with value = 0.
