import requests
from plotly.graph_objs import Bar
from  plotly import offline

class visuals:
    def __init__(self, r):
        self.response_dict = r

    #inserting response in variable
    def apiResponse(self):
        self.repo_dicts = self.response_dict['items']
        self.repo_names, self.stars = [], []
        for self.repo_dict in self.repo_dicts:
            self.repo_names.append(self.repo_dict['name'])
            self.stars.append(self.repo_dict['stargazers_count'])

        self.tempList = [self.repo_names, self.stars]
        return self.tempList

    def createVisuals(self):
        self.tempList = self.apiResponse()
        self.data = [{
            'type': 'bar',
            'x': self.tempList[0],
            'y': self.tempList[1]
        }]

        self.myLayout = {
            'title': 'Python project with the highest number of stars',
            'xaxis': {'title': 'Repository'},
            'yaxis': {'title': 'Stars'}
        }

        self.fig  = {
            'data': self.data,
            'layout': self.myLayout,
        }
        offline.plot(self.fig, filename='python_repos.html')

