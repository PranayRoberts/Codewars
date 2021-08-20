  
"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""

def expanded_form(num):
    res=[]
    for i,dig in enumerate(str(num)[::-1]):
                           if int(dig)!=0:
                            res.append(dig + ('0' * i))
    return ' + '.join(res[::-1])
