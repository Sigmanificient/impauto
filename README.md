# Impauto
*Make your life easier with automated inputs*

## Installation
```
pip install impauto
```

## How to use it ?
```python
import impauto

# Each argument passed will be enter as a str to the input function.
impauto.Automated(154) 


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

## License
© 2020 copyright Edhyjox

This repository is licensed under the MIT License.
See LICENSE for details.