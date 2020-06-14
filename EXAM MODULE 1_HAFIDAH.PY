print('Soal 1')
def Hashtag(string):
    x = string.split(' ')
    if len(x) > 1 :
        y = []
        for i in range(len(x)):
            y.append(x[i].capitalize())

        if len(''.join(y)) > 140:
            print(False)
        else:
            print('#'+''.join(y))
            
    else:
        print(False)

#Output check
Hashtag(" Hello there how are you doing")
Hashtag(" Hello World " )
Hashtag("") 

print('\nSoal 2')

def create_phone_number(number):
    for i in range(len(number)):
        number[i] = str(number[i])
    print('({}) {}-{}'.format(''.join(number[0:3]),''.join(number[3:6]),''.join(number[6:10])))

#Output check
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

print('\nSoal 3')

def sort_odd_even(num):
    list_odd = [number for number in num if number%2!=0] 
    list_even = [number for number in num if number%2==0]
    for i in range(len(list_odd),0,-1):
        for idx in range(0,i-1):
            if list_odd[idx] > list_odd[idx+1]:
                temp = list_odd[idx]
                list_odd[idx] = list_odd[idx+1]
                list_odd[idx+1] = temp

    for i in range(len(list_even),0,-1):
        for idx in range(0,i-1):
            if list_even[idx] < list_even[idx+1]:
                temp = list_even[idx]
                list_even[idx] = list_even[idx+1]
                list_even[idx+1] = temp
    newlist = list_odd + list_even
    return newlist
    # for i in list_odd:
    #     for j in range(len(newlist)):
    # num[num.index(5)] = list_odd[2]

#Output check
print(sort_odd_even([5, 3, 2, 8, 1, 4]))
 