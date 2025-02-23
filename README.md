# Lox Language Implementation

This is an implementation in python of the Lox Language, a basic programming language described in the book [Crafiting Interpreters](https://craftinginterpreters.com/).

## Usage 

```shell
# Create new venv (for runing the tests)
$ python3 -m venv venv

# Running the REPL
$ python3 main.py

# Running a .lox script
$ python3 main.py <path/to/script.lox>
```

## Script Example

```csharp
var str = "lox";
var number = 1234.67;

func do_something(a, b) {
    return a * b;
}

print do_something(number, 2);
print str;
```

## Tests

```shell
$ pytest
```