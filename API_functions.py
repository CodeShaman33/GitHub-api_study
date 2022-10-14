import requests


def showKeys(dict):
    for i, item in enumerate (dict.keys()):
        print(i, item)

def totalRepoCount(dict):
    print(f'total amount of repositories: {dict["total_count"]}')




