import requests

response = requests.get("https://countriesnow.space/api/v0.1/countries/capital")
result = response.json()
del result['error']
del result['msg']
new_list = result.values()

while True:
    user = input("please enter a country name and and you will know the capital: ").capitalize()

    if user.isalpha():
        for items in new_list:
            for i in items:
                new_dict = i.get("name")
                new_capital = i.get("capital")
                if user in new_dict:
                    print("the capital of ", user, "is ", new_capital)


    else:
        print("Please this not a country name")
