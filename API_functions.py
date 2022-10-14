import requests


def showKeys(dict):
    for i, item in enumerate (dict.keys()):
        print(i, item)

def totalRepoCount(dict):
    print(f'total amount of repositories: {dict["total_count"]}')

def firstRepo(dict):
    repo_dict = dict[0]
    print(f"\nKeys: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)

def repoInformations(dict):
    dict = dict[0]
    print(f'name: {dict["name"]}')
    print(f'owner: {dict["owner"]["login"]}')
    print(f'stars: {dict["stargazers_count"]}')
    print(f'repository: {dict["html_url"]}')
    print(f'created: {dict["created_at"]}')
    print(f'description: {dict["description"]}')




