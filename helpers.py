import json
from bs4 import BeautifulSoup


def read_file(file_name):
    f = open(file_name, 'r')
    f.readlines()
    f.close()
    return


def getcourse_link_name(id, soup):
    result = dict()
    for module in soup.find_all("div", attrs={"data-courseid": id}):
        result['name'] = module.a.string
        result['link'] = module.a['href']
    return result


def get_resource_link_name(soup, href):
    result = dict()
    parent = soup.find_all("a", attrs={"href": href})
    for module in parent:
        div = BeautifulSoup(str(parent), "html.parser")
        try:
            result['type'] = div.a.span.span.string
        except:
            result['type'] = ''
        name_file = str.replace(str(div.a.span), str(div.a.span.span), '')
        name_file_parse = BeautifulSoup(str(name_file), "html.parser")
        result['name'] = name_file_parse.string
        result['link'] = div.a['href']
    return result


def exist_file(file_name):
    try:
        open('files/' + file_name, 'r')
        return True
    except FileNotFoundError:
        f = open('files/' + file_name, 'w+')
        f.write('{"courses" : [""]}')
        f.close()
        print('File Created : ' + file_name)
        return False


def exist_file_module(file_name):
    try:
        open('files/' + file_name, 'r')
        return True
    except FileNotFoundError:
        f = open('files/' +file_name, 'w+')
        f.write('{"id" : [""]}')
        f.close()
        print('File Created : ' + file_name)
        return False


def open_and_write_json(file_name, arraytojson):
    f = open('files/' + file_name, 'w+')
    f.write(json.dumps(arraytojson))
    f.close()