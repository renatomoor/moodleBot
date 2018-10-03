import json
import env
from bs4 import BeautifulSoup
from DiscordHooks import Color
from login import get_html_loged_in
from message import Messages
from helpers import  open_and_write_json, getcourse_link_name,get_resource_link_name, exist_file_module

send = Messages()


def diff_module(module_id, html_type, type_name):

    html = get_html_loged_in(env.Moodle._URLYEARLIST)
    soup = BeautifulSoup(str(html), "html.parser")
    module_info = getcourse_link_name(int(module_id), soup)

    file_name = module_id + '_' + type_name + '.txt'
    exist_file_module(file_name)

    list_resources = dict()
    list_resources['id'] = []

    with open('files/' + file_name) as data_file:
        list_resources_old = json.load(data_file)


    html_compose = env.Moodle._URLBASEVIEW + '?id=' + module_id
    html = get_html_loged_in(str(html_compose))

    if not html:
        return

    soup = BeautifulSoup(str(html), "html.parser")
    content = soup.findAll('a')

    for a in content:
        if html_type in str(a):
            html = BeautifulSoup(str(a.parent), "html.parser")
            id = str.replace(html.a['href'], html_type, '')
            list_resources['id'].append(str(id))
            resourse = get_resource_link_name(html, html_type + id)
            list_resources[id + '_link'] = resourse['link']
            list_resources[id + '_name'] = resourse['name']
            list_resources[id + '_type'] = resourse['type']

    open_and_write_json(file_name, list_resources)

    list1 = set(list_resources['id'])
    list2 = set(list_resources_old['id'])

    if list1 == set():
        return
    if list2 == set():
        return

    if not list1 == list2:
        if len(list1) > len(list2):
            diff = list1 - list2
            for id in diff:
                send.sendMessageAll(env.Channel._MOODLEBOT,
                                     "```" + module_info["name"] + "```",
                                    "Name:  **" + str(list_resources[id + '_name'] + "**\n"
                                    "Type:  " + type_name),
                                    "Link - Download - Go to",
                                    str(list_resources[id + '_link']),
                                    Color.Green,
                                    "Resource added: ")

                print('message send, module added, ' + type_name  + ' id: ' + id)
        elif len(list1) < len(list2):
            diff = list2 - list1
            for id in diff:
                print(id)
                send.sendMessageAll(env.Channel._MOODLEBOT,
                                       "```" + module_info["name"] + "```",
                                      "Go to module",
                                      "Go to module",
                                    html_compose,
                                    Color.Red,
                                      "Resource deleted")

                print('message send, module deleted , module id: ' + id)
        else:
            print('Error trying to read list of modules ids')

