import requests
from API_functions import showKeys, totalRepoCount, firstRepo, repoInformations
from  repos_visual import visuals


def mainApi(url):
    #defining Api version
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers= headers)
    print(f'Status Code: {r.status_code}')

    #API response
    res_dict = r.json()
    showKeys(res_dict)
    return res_dict






if __name__ == '__main__':
    url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
    tempDict = mainApi(url)
    #totalRepoCount(tempDict)
    #firstRepo(tempDict['items'])
    repoInformations(tempDict['items'])
    visual = visuals(tempDict)
    visual.createVisuals()