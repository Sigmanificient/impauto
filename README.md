# Impauto 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/44cbc17d1bfe4566b3f305ef8fe5d106)](https://app.codacy.com/gh/Sigmanificient/impauto?utm_source=github.com&utm_medium=referral&utm_content=Sigmanificient/impauto&utm_campaign=Badge_Grade_Settings)
![PyPI](https://img.shields.io/pypi/v/impauto)
![PyPI - Downloads](https://img.shields.io/pypi/dm/impauto)
![PyPI - Format](https://img.shields.io/pypi/format/impauto)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/impauto)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/impauto)
![GitHub repo size](https://img.shields.io/github/repo-size/Sigmanificient/impauto)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/impauto)

*Make your life easier with automated inputs*

## Installation
```cmd
pip install impauto
```

## How to use
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

### Thanks for using Impauto

## License
© 2020 copyright Edhyjox

This repository is licensed under the MIT License.
See LICENSE for details.
