from main import list_generator

def unique(default_list):
    unique_list = []
    for el in default_list:
        if default_list.count(el) > 1 and unique_list.count(el) == 0 or default_list.count(el) == 1:
            unique_list.append(el)
        
    return unique_list

    

number = list_generator(
    max=10, 
    min=0, 
    N=10)
print(f'Before: {number}\nAfter: {unique(number)}')


def test(a, *args, **kwargs):
    print(a, args, kwargs)

test(1, 2, 3, 4, 5, 6, s=1, b=2, u=3)