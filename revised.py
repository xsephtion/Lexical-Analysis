types = ["int", "char", "double", "float", "main", "void", "include", "iostream", "string", "using", "namespace", "std",
         "return"]
operators = ["=", "+", "-", "/", "*"]
symbols = ["(", ")", "{", "}", ";", "#", "<", ">"]
keywords = ["if", "else", "switch"]
numerals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
varin = ["a-zA-z"]

grammar = {'startof': '#', 'preprocessor': 'include', 'opening': '<', 'stringsyntax': '', 'closing': '>',
           'using': 'using'}
'''
#include<iostream> // preprocessing drive
using namespace std; // no usage of "std::int a;"

int main(){ // Structure: int = function return, main = function name, () = parenthesis, { = opening braces opening of a statement or a function
int a; //int = data type, a = data name 
a = a + 1; // a = data to be summed (same as a += 1) '+' = add to be recognized by parser 
return 0; // return = to be returned to 'int' ( function type) 0 = what is to be returned 
} // Closing Braces, meaning closing statement or definition of a function

; = delimiter meaning end of the line

'''
f = open("test.txt", "r")
charread = f.read()
store = []
chars = []
sym = []
numb = []
temp = []
variables = []

for char in charread:
    for ch in char:
        if ch == ";" or ch == "<" or ch == ">" or ch == "#":
            chars.append(' ')
            chars.append(ch)
            chars.append(' ')
        else:
            chars.append(ch)

for i in chars:
    if i == ' ' or i == '\n':
        store.append(''.join(temp))
        store.append(' ')
        temp.clear()
    else:
        temp.append(i)

for q in chars:
    if q == "(" or q == ")":
        sym.append(q)
    if q == "{" or q == "}":
        sym.append(q)
    if q == "<" or q == ">":
        sym.append(q)
    if q == ";":
        sym.append(q)
    if q == "#":
        sym.append(q)

for num in chars:
    if 48 <= ord(num) <= 57:
        numb.append(num)


def loop(list, store, text):
    count = 0
    for i in range(len(store)):
        for q in range(len(list)):
            if str(store[i]) == list[q]:
                print(text + str(store[i]))
                count = count + 1
    return count


total = loop(types, store, 'Identifier: ')
total = total + loop(operators, store, 'Operation: ')
total = total + loop(alph, store, "String: ")
total = total + loop(numerals, numb, 'Integers: ')
total = total + loop(symbols, sym, 'Symbols: ')
print("Total count of tokens: " + str(total))
f.close()
