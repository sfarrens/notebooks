
# Native Python

In the context of Python the term "native" refers to the core commands, operators and functions that come with a default installation. The following subsections will cover some of the most essential elements provided in native Python.

## Contents

1. [Native Python](#Native-Python)

## Operators

Native python supports various [maths operators](https://docs.python.org/2/reference/lexical_analysis.html#operators) (*e.g.* addition, subtraction, multiplication, division, *etc.*) and [logic operators](https://docs.python.org/2/library/stdtypes.html?highlight=boolean) (*e.g.* and, or, not, *etc.*).

### Mathematical Operators

Some simple examples of some basic maths operations:

$$1 + 1 = 2$$


```python
1 + 1
```




    2



$$5 - 1 = 4$$


```python
5 - 1
```




    4



$$6 \times 7 = 42$$


```python
6 * 7
```




    42



$$21 \div 7 = 3$$


```python
21 / 7
```




    3



$$3^2 = 9$$


```python
3 ** 2
```




    9



$$4 \gt 3$$


```python
4 > 3
```




    True



$$9 \not< 2$$


```python
9 < 2
```




    False



### Logic Operators

Some basic logic operations:


```python
True and False
```




    False




```python
True or False
```




    True



### Scientific Notation

Larger numbers can be inputted using scientific notation with the letter **e**. For example:

$$10000 = 10^5$$


```python
1e5
```




    100000.0



## Built-in Functions

A default Python installation includes some standard [built-in functions](https://docs.python.org/2/library/functions.html). 

The following subsections will cover some of the most essential native Python functions.

### Print

The first lesson with any programming language is learing how to print output to the terminal. In python this is done with the **print** command. Text (strings of characters) are represented either by single ('') or double quotes ("") for displaying text. For example one can display the standard "Hello world!" output as follows:


```python
print 'Hello world!'
```

    Hello world!



```python
print "Hello world again!"
```

    Hello world again!


Single and double quotes can be combined to display the inner set of quotes in the text.


```python
print '"What is hell? I maintain that it is the suffering of being unable to love." ― Fyodor Dostoyevsky'
```

    "What is hell? I maintain that it is the suffering of being unable to love." ― Fyodor Dostoyevsky


The print command also can be used to output the result of an operation. A comma (**,**) is used to divide the elements in a print statement.


```python
print '1 + 1 =', 1 + 1
```

    1 + 1 = 2


### Variables

In python virtually any combination of letters, numbers and undescores can be used to define a variable. The variable must, however, start with a letter. For example to set some variable $x = 1$:


```python
x = 1

print 'x =', x
```

    x = 1


The variables can of course also be used in conjunction with operators.


```python
x = 1
y = 2

print 'x + y =', x + y
```

    x + y = 3


In the simple examples above using very short variables names such as $x$ and $y$ if perfectly adequate, but it is generally good practice to longer more expressive variable names in codes in order to avoid ambiguity and faciliate readability. For example:


```python
speed_of_light_c = 2.99e8 #m/s
mass_of_human_m = 79.5 #kg

energy = mass_of_human_m * speed_of_light_c ** 2

print 'The energy of this human is', energy, 'Joules.'
```

    The energy of this human is 7.1073795e+18 Joules.


Apart from numbers, variables can also be used to reference other Python objects such as strings of text.


```python
x = 'Bob'

print 'Hi, my name is', x
```

    Hi, my name is Bob


### Integers and Floats

The commands **int()** and **float()** can be used to convert numbers between integers (int) and floating point numbers (float, *i.e.* real numbers). Python by default sets any number with a decimal to a float and without a decimal to an int. So, the number $1$, for example, is an integer and the number $1.0$ is a float. Sometimes it 


```python
x = 1
y = 1.0

print float(x), int(y)
```

    1.0 1


### Strings

As already discussed strings of characters are defined between single or double quotes, however numberical values can also be converted to strings using the command **str()**. This is useful because in Python strings can be concatenated using the **+** operator.


```python
x = 7

print 'Have you ever watched the ' + str(x) + ' Samuari?'


```

    Have you ever watched the 7 Samuari?


### Type

The **type()** command can be used to determine the "type" of object in question. For example if a variable has been set and one wishes to find out if the object if refers to is an int, a float or a string.


```python
x = 5.6
y = 'Bob'
z = 12

print 'x is a', type(x)
print 'y is a', type(y)
print 'z is a', type(z)
```

    x is a <type 'float'>
    y is a <type 'str'>
    z is a <type 'int'>


### Boolean

A boolean is a special data type that can only have one of two possible values **True** (1) or **False** (0). This data type can be very useful when performing logic operations. The function **bool()** can be used to convert the integers values $0$ and $1$ to boolean values.


```python
x = 1
y = 0

print bool(x), bool(y)
```

    True False


The reverse process is also possible.


```python
x = True
y = False

print int(x), int(y)
```

    1 0


### Absolute Value

The function **abs()** returns the absolute value of a number.


```python
x = -16.6

print 'The absolute value of', x, 'is', abs(x)
```

    The absolute value of -16.6 is 16.6


### Lists

Lists of values can be speficied using square brackets *[]*.


```python
x = [1, 2, 3]

print x
```

    [1, 2, 3]



```python

```
