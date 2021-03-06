""" StackBehavior - User World Map
This module visualize user count by country into world map using pygal library
"""
import pygal
import csv
from pygal.style import Style

custom_style = Style(
  colors=('#F6D18B', '#F0AE58', '#EF8823', '#EB7A3E', '#F05328', '#C24320'))

# source, output = './dataset/data/user_location_min.csv', './visualize/output/user_world_map.svg'
source, output = './dataset/data/reputation_min.csv', './visualize/output/user_rep_world_map.svg'

def read(stt, stp=0):
    """ Convert data from an csv file into dict """
    data_dict = {}
    with open(source, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if stt <= int(row[1]) <= stp or (int(row[1]) >= stt and not stp):
                # data_dict[row[0]] = int(row[1])
                data_dict[row[0]] = 1
    return data_dict

def visualize_user():
    worldmap_chart = pygal.maps.world.World(style=custom_style)
    worldmap_chart.title = 'Numbers of StackOverflow users by country'
    worldmap_chart.add('1 - 10000', read(1, 10000))
    worldmap_chart.add('10001 - 40000', read(10001, 40000))
    worldmap_chart.add('40001 - 80000', read(40001, 80000))
    worldmap_chart.add('80001 - 140000', read(80001, 140000))
    worldmap_chart.add('140000+', read(140001))
    worldmap_chart.render_to_file(output)

def visualize_rep():
    worldmap_chart = pygal.maps.world.World(style=custom_style)
    worldmap_chart.title = 'StackOverflow users reputation by country'
    worldmap_chart.add('1 - 1M', read(1, 1000000))
    worldmap_chart.add('1M - 5M', read(1000001, 5000000))
    worldmap_chart.add('5M - 10M', read(5000001, 10000000))
    worldmap_chart.add('10M - 15M', read(10000001, 15000000))
    worldmap_chart.add('15M - 50M', read(15000000, 50000000))
    worldmap_chart.add('50M+', read(50000000))
    worldmap_chart.render_to_file(output)
visualize_rep()
