import urllib.request
import urllib.error
import urllib.parse
import socket

print("Welcome to the Site Connectivity Checker!")
print("This program checks the connectivity of a website by sending a request and checking the response.")
print("You can check the connectivity of a website by entering its URL.")   
print("Please enter the URL of the website you want to check (e.g., https://www.example.com):")
url = input("URL: ").strip()

def check_connectivity(url):
    print(f"Checking connectivity for {url}...")


    response = urlib.uropen(url)
    print(f"Response code: {response.getcode()}")
    print("Website is reachable.")