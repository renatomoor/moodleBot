import env
from message import Messages
from bs4 import BeautifulSoup
from DiscordHooks import Color
import json
from helpers import getcourse_link_name, exist_file, open_and_write_json
from login import get_html_loged_in

send = Messages()


def getlistcourses():
    file_name = 'courses_list.txt'

    exist_file(file_name)

    with open('files/' + file_name) as data_file:
        list_courses_old = json.load(data_file)

    list_courses = dict()
    list_courses_links = dict()
    list_courses['courses'] = []
    list_courses_links['links'] = []

    html = get_html_loged_in(env.Moodle._URLYEARLIST)
    soup = BeautifulSoup(str(html), "html.parser")

    moduleshtml = soup.find_all("div", class_="coursebox")

    for module in moduleshtml:
        id = module.get('data-courseid')
        list_courses['courses'].append(id)
        a = getcourse_link_name(id, soup)
        list_courses_links['links'].append(a['link'])

    list1 = set(list_courses['courses'])
    list2 = set(list_courses_old['courses'])

    open_and_write_json(file_name, list_courses)

    if list1 == set():
        return
    if list2 == set():
        return

    if not list1 == list2:
        if len(list1) > len(list2):
            diff = list1 - list2
            for id in diff:
                a = getcourse_link_name(id, soup)
                send.sendMessageAll(env.Channel._MOODLEBOT,
                                    "Module info",
                                    str(a['name']),
                                    "Go to module",
                                    str(a['link']),
                                    Color.Green,
                                    "Module Added")

                print('message send, module added, module id: ' + id)
        elif len(list1) < len(list2):
            diff = list2 - list1
            for id in diff:
                send.sendMessageAll(env.Channel._MOODLEBOT,
                                      "Module info",
                                      "Go to module's list",
                                      "Go to module",
                                    env.Moodle._URLYEARLIST,
                                    Color.Red,
                                      "Module Deleted")
                print('message send, module deleted , module id: ' + id)
        else:
            print('Error trying to read list of modules ids')
    else:
        print('nothing change in modules lists')
        return list_courses['courses']