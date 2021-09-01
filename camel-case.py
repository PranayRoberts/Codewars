"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(s):
    l=list(s)
    if s=='':
        return s
    
    
    else:
        for i,x in enumerate(l):
            if x == '-' or x== '_':
                l[i]=l[i].replace(x,'')
                l[i+1]=l[i+1].upper()
            
    return "".join(l)
