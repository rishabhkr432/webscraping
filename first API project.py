import requests
import random
#could use import choice from random
import pyfiglet
header = pyfiglet.figlet_format("DAD JOKES!")
print(header)
url = "https://icanhazdadjoke.com/search"

userinput = input("Give me a word?\n")
response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": userinput}).json()
totaljk = response["total_jokes"]

if totaljk == 1:
    print("This is the only joke")
    data = response["results"][0]['joke']
    print(data)
elif totaljk > 1:
    print(f"I have found {totaljk} jokes. Here is a random one")
    random_num = random.randint(0, totaljk)
    jokes = response["results"][random_num]['joke']
    print(jokes)
else:
    print(f"There are no jokes with {userinput} letters.")
