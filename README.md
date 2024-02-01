TEPL 
====

⚠️ This compiler is currently in development so it might have breaking changes with each update

💬 Got some questions or feedback? Just open an issue and we'll be glad to respond!

```tepl
INPUT EXPECTING NUM "Enter a number: " IS num
IF num % 2 == 0 THEN
  OUTPUT num+" is a even number!"
ELSE THEN
  OUTPTUT num+" is a odd number!"
END
```

<p>TEPL is a scripting programming language in development 
that strives to make coding simple, easy, and fun to learn. 
It comes with many features, including: <p>

- 




Documentation
====
### Table of Contents
- [Introduction](/README.md/Documentation/Introduction)
- Installation
- Files and the command line
- `OUTPUT`
- Math operations
- Strings
- Logical operations
- `SET`
- Running files using `RUN`
- NONE values
- Conca- what?
- Logic gates
    - `IF`!
    - What `ELSE`?
    - `ELSEIF`...?
    - Nested if statements
    - `AND` what?
    - `OR` or `NOT`
- `FUNCTION`



### Introduction 



FAQ
====

## When will TEPL be ready to use?
We will hopefully have it ready by the end of 2024 or possibly 
sooner. Currently, we're starting on building the base syntax. 
After we're done with that we will move on to more advanced
functionalities and important features. Eventually, we will
add libraries and frameworks. 

## Why use TEPL?
I know you are probably thinking, "And yet another programming 
language?" I understand that there are many, many(around 
10,000) programming languages in the world today. So what makes 
TEPL(a new programming language) worth using? TEPL is built for 
beginners and is a backend development programming language. It 
contains no frontend features for now, but in the near future 
we will add VEPL(a library for TEPL, also known as: visually 
educational programming language) which will add some frontend 
development. TEPL is a great place to start if your new to 
programming because its grammar is like English. For example, 
in order to build a function you write:
```
FUNCTION add a b MEANS
RETURN a+b
END 
```
(Disclaimer: the syntax shown above is not yet available 
and may be changed, but the idea of functions is something we 
look to add later on) 
Simple, right? Yes it is! If you want to get a jump-start into
programming TEPL is the choice for you.

## License
TEPl was originally licensed under GNU, but for more security I 
set the license to the Apache license. In the end, I hope that 
this piece of software may inspire other projects and may 
improve the quality of new and existing software.
