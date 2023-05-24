# Python Features
Let's start with a high-level overview of Python features. 
* First off, everything in Python is declared by assignment. In Python, if you reference a variable inside a function, that variable is implicitly global. If a variable is assigned a value anywhere within the function's body, it's assumed to be a local, unless explicitly declared as global.

* Second, Python supports dynamic typing. This is a timesaver when you need to write repetitive functions quickly.

* Third, variables in Python are declared by assigning to them. So Python does not require explicit type specifiers, but sets the type implicitly by examining the value that was assigned. That means assigning a literal integer to a variable creates a variable of type int, while assigning quoted text to a variable creates a variable of type string. Once a variable is assigned to, it'll cause an error if the variable is used with an operator or function that is inappropriate for that type.

* Fourth, a variable cannot be used before it is assigned to. Now, variables must be assigned some value. A value of None may be assigned if no particular value is needed.