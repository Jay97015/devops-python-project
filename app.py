import requests 
response = requests.get("https://api.github.com") 
print("GitHub API Status:", response.status_code) 
