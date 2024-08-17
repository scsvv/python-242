# products_dict = {
#     "banan": {
#         "price": 32.2, 
#         "count": 123
#     },

#     "apple": {
#         "price": 12.2, 
#         "count": 23
#     },

#     "orange": {
#         "price": 23.2, 
#         "count": 54
#     }, 
# }

# for key in products_dict:
#     data = products_dict.get(key)
    
#     price = data.get('price')
#     count = data.get('count')
#     result = price * count

#     products_dict[key]["total"] = result

# print(products_dict)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict()
for i in range(3):
    result[keys[i]] = values[i]

print(result)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

for key, value in dict2.items():
    dict1[key] = value

print(dict1)


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 300 in list(sample_dict.values()): print('200 is in list')