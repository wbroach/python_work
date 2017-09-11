import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import webbrowser

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

response_dict = r.json() #returns a dict, 'items' key returns a list of dicts
                         #and each dict has info about each github repository.
repo_dicts = response_dict['items'] #returns a list of dictionaries

names, plot_dicts = [], []
for repo_dict in repo_dicts: #For each dictionary in list
    names.append(repo_dict['name'])
    
    description = repo_dict['description']
    if not description:
        description = 'Not Provided'
    
    plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': description,
                'xlink': repo_dict['html_url'],
                }
    plot_dicts.append(plot_dict)
    
    
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart_file_name = 'python_repos.svg'
chart.render_to_file(chart_file_name)

web_controller = webbrowser.get(using='windows-default')
web_controller.open(chart_file_name)

