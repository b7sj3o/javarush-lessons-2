import json
import requests


# from datetime import datetime
# from pathlib import Path

# path = Path(__file__).parent.absolute()


# with open(path/"data.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# print(data)
# print(data["name"])
# print(data["address"]["street"])
# print(data['lastLogin'])
# print(datetime.strptime(data['lastLogin'], "%Y-%m-%dT%H:%M:%SZ").date())


# data = {
#     "username": "bob",
#     "password": "",
#     "email": "",
#     "address": {
#         "city": "Київ",
#         "street": "Хрещатик",
#         "zip": "10000",
#     },
#     "is_adult": True,
#     10: 2,
#     True: False
# }

# with open('data2.json', 'w', encoding="utf-8") as file:
#     json.dump(
#         data,
#         file,
#         skipkeys=True,
#         indent=4,
#         ensure_ascii=False,
#     )


# print(json.loads(json.dumps(data)))

# with open('data3.json', 'w', encoding="utf-8") as file:
#     file.write(json.dumps(data, ensure_ascii=False, indent=4))


# JSON METHODS
# load: json file -> python object
# dump: python object -> json file
# loads: str -> python object
# dumps: python object -> str




# response = requests.get("https://google.com")
# params = {'userId': 1}
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# print(response.status_code, response.reason)
# print(json.dumps(response.json(), indent=2))

# # GET /api/users?is_active=true
# def users(is_active: bool = False):
#     # SELECT * FROM users u WHERE u.is_active IS is_active


# data = {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1
# }

# data = {'name': 'Іван', 'email': 'i@ex.com'}
# {"name": "\u0406\u0432\u0430\u043d", "email": "i@ex.com"}
# name=%D0%86%D0%B2%D0%B0%D0%BD&email=i%40ex.com

# response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
#
# print(response.status_code)
# print(response.json())

# response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# print(response.status_code)
# print(response.json())

# response = requests.get('https://api.github.com/users/swaasw')

# print(response.status_code, response.reason)
# print(json.dumps(response.json(), indent=2))


URL = "https://api.github.com/users/{username}"


def get_user_data_from_github(username) -> dict | None:
    try:
        response = requests.get(URL.format(username=username), timeout=20)
        response.raise_for_status()

        if "application/json" in response.headers["Content-Type"]:
            return response.json()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print("Такого користувача не знайдено")
        elif err.response.status_code == 403:
            print("Заборонено, можливо забагато запитів")
        else:
            print("Requests Exception: ", err)

    except Exception as err:
        print("Exception: ", err)



def main():
    while True:
        username = input("Введіть нікнейм користувача (Enter щоб вийти): ")

        if username == "":
            break

        data = get_user_data_from_github(username)

        if data is None:
            print("Немає даних")
            continue

        print(data)


if __name__ == "__main__":
    main()