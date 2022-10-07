
def function(*params):
    res: str = ''
    for i in params:
        res+=i
    return res

x = input('вв')
function(x)