# Impauto
*Make your life easier with automated inputs*

## Installation
```
pip install impauto
```

## How to use it ?
The Basic way to use this module
```python
from impauto import Automated

# Each argument passed will be enter as a str to the input function.
Automated(154) 


# use your script as normal
def syracuse(x):
    step = 0

    while x != 1:
        x = (3 * x + 1) if x % 2 else (x // 2)
        step += 1

    return step

n = int(input("Enter a number: "))
print(syracuse(n))
```
You can also hide terminal input messages
```python
from impauto import Automated

# Each argument passed will be enter as a str to the input function.
Automated(1, 2, 3, show_message=False)
```

By default, It will raise a exception if there is more input than value given.
To make input repeats indefinitely, you can use this code
```python
from impauto import Automated

# Each argument passed will be enter as a str to the input function.
Automated("a", "b", forever=True)
```

### Thanks for using Impauto !


## License
© 2020 copyright Edhyjox

This repository is licensed under the MIT License.
See LICENSE for details.