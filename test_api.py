import requests
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
username = os.getenv('USERNAME_GIT') # не создавайте переменную USERNAME, она может быть занята
reponame = os.getenv('REPONAME_GIT')
token = os.getenv('AUTH_TOKEN_GIT')
url = f'https://api.github.com'
headers= {'Authorization':'token '+ token}


class Github():
    def __init__(self, url, username, headers):
        self.url = url
        self.username = username
        self.headers = headers

    def check_repo(self):
        command = '/user/repos'
        endpoint = self.url + command
        response = requests.get(endpoint, headers=headers)
        if response.ok:
            print('Список созданных репозиториев: ')
            for i in response.json():
                print(f"Название: { i['name'] }")
        else:
            print(f'Ошибка: {response}')

    def create_repo(self):
        command = '/user/repos'
        endpoint = url + command 
        data = {'name': reponame}
        response = requests.post(endpoint, headers=headers, json=data)
        if response.ok:
            print(f'Репозиторий {reponame} успешно создан!')
        else:
            print(f'Ошибка: {response}')

    def delete_repo(self):
        command = f'/repos/{username}/{reponame}'
        endpoint = url + command 
        response = requests.delete(endpoint, headers=headers)
        if response.ok:
            print(f'Репозиторий {reponame} успешно удален!')
        else:
            print(f"Ошибка: {response}")


if __name__ == "__main__":
    git = Github(url, username, headers)
    git.check_repo()
    git.create_repo()
    git.check_repo()
    git.delete_repo()
    git.check_repo()