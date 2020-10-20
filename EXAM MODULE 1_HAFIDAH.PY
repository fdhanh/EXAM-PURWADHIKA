## Number 1

def Hashtag(string):
    string = [x.capitalize() for x in string.split()]
    out = ''.join(string)
    if len(out) > 140 or len(out) == 0:
        return False
    else:
        return '#'+out
    
print(Hashtag(' Hello there how are you doing'))
print(Hashtag('  Hello  World  '))
print(Hashtag(''))

## Number 2

def create_phone_number(number):
    output = '(xxx) xxx-xxxx'
    for num in number:
        output = output.replace('x', str(num), 1)
    return output

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

## Number 3

def sort_odd_even(num):
    odd = [x for x in num if (x % 2) != 0]
    even = [x for x in num if (x % 2) == 0]
    odd_idx = [num.index(x) for x in odd]
    even_idx = [num.index(x) for x in even]
    for i in [odd,odd_idx,even_idx]:
        i.sort()
    even.sort(reverse=True)
    odd_idx = list(zip(odd, odd_idx))
    even_idx = list(zip(even, even_idx))
    for number, idx in odd_idx:
        num[idx] = number
    for number, idx in even_idx:
        num[idx] = number
    return num

print(sort_odd_even([5,3,2,8,1,4]))
