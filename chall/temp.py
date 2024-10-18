#remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # Output: [1, 2, 3, 4, 5]

def remove_duplicates(l: list) -> list:
    s = set()
    for i in l:
        if i in s:
            continue
        else:
            s.add(i)
    return list(s)

assert remove_duplicates([1, 2, 2, 3, 4, 4, 5])  == [1, 2, 3, 4, 5]

#increment_list([1, 2, 3])
increment_list = [1, 2, 3]
result = list(map(lambda x: x + 1, increment_list))
assert result == [2,3,4]

import requests

def get_data_endpoint():
    url = "test"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

    except requests.RequestException as e:
        print(e)

for x in range(0,3):
    print(x)

