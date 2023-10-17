# Code for fetching the link
import requests

url = "https://www.virustotal.com/api/v3/urls"

payload = {"url": "www.google.com"}
headers = {
    "accept": "application/json",
    "x-apikey": "f2e0a0853596330c0011bf5626cc5d48bc9d53e84388f42daaa426d4623cbfa5",
    "content-type": "application/x-www-form-urlencoded",
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)


# Code for the output of that link


# url = "https://www.virustotal.com/api/v3/urls/dd014af5ed6b38d9130e3f466f850e46d21b951199d53a18ef29ee9341614eaf"

# headers = {
#     "accept": "application/json",
#     "x-apikey": "f2e0a0853596330c0011bf5626cc5d48bc9d53e84388f42daaa426d4623cbfa5",
# }

# response = requests.get(url, headers=headers)

# print(response.text)
