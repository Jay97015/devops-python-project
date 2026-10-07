import requests 
def get_github_user_stats(username): 
    url = f"https://api.github.com/users/{username}" 
    response = requests.get(url) 
    if response.status_code == 200: 
        data = response.json() 
        print(f"=== GitHub Profile: {data.get('login')} ===") 
        print(f"Name: {data.get('name')}") 
        print(f"Public Repos: {data.get('public_repos')}") 
        print(f"Followers: {data.get('followers')}") 
    else: 
        print(f"Failed to fetch user. Status code: {response.status_code}") 
if __name__ == "__main__": 
    get_github_user_stats("jay97015") 
