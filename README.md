### TEPL - Textual Educational Programming Language

TEPL is a simple educational programming language aimed at beginners to learn basic programming concepts. It provides a user-friendly interface for practicing programming. TEPL supports basic arithmetic calculations, variable support, logic operators, booleans, math operators if statements and input statements. 

### Features:
- Basic arithmetic calculations (Completed)
- Variable support (Completed)
- Basic logic operators (Completed)
- Implementation of booleans (Completed)
- Math operators and functions (e.g., sin, cos, tan) (TODO)
- If statements (Nearly Complete)
- Input statements (Completed)
- List support (TODO)
- For loops (TODO)
- While loops (TODO)
- Functions (TODO)

For more information and documentation, visit [TEPL Docs](https://tepl.vercel.app/docs.html).

Lexer can be found in the `src/lexer.py` file.
AST nodes can be found in the `src/nodes.py` file. 
Parser can be found in the `src/parser.py` file.
Transpiler can be found in the `src/transpiler.py` file.

### Version History:
- v0.75.00 update: [Release Notes](https://github.com/TEPL-Team/TEPL/releases/tag/v0.75.00)
- v1.00.00 update: [Release Notes](https://github.com/TEPL-Team/TEPL/releases/tag/v1.00.00)
- v1.35.00 update: [Release Notes](https://github.com/TEPL-Team/TEPL/releases/tag/v1.35.00)
- v1.80.00 update: [Release Notes](https://github.com/TEPL-Team/TEPL/releases/tag/v1.80.00)
- v2.0.0 update: [Release Notes](https://github.com/TEPL-Team/TEPL/releases/tag/v2.0.0)

For the license information, check [here](https://github.com/TEPL-Team/TEPL/blob/main/LICENSE).

### Code Showcases:

Number guesser game. 
```tepl
PC this is a comment, and this is an example of a basic number guessing game CP

forever do
    set guess to 'Enter a number from 0 to 100: ' expecting input and num
    set secret to random num from 0 to 100
    if guess > 100 OR guess < 0 then
        output $"Error: You inputed a number that is less than or greater than 0 or 100, it was $guess!"
    elseif guess > secret OR guess < secret then
        output $"Wrong guess! The secret number was...$secret!"
    else then 
        output $"You got it right! The secret number was $secret!"
    end
    pause 1
    exit
end
```
