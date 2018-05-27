import sys

import requests


def create_locale_json_from_url(url, file_name):
    try:
        try:
            json_content = requests.get(url, allow_redirects=True)
        except Exception as error:
            print("There is not internet connection!\n", error)
            sys.exit()
        file = open(file_name, 'xb')
        file.write(json_content.content)
        file.close()
        print("file created")
    except FileExistsError:
        print("File already exists! Please delete it and run again.")


def does_json_contain_the_value(text_to_find):
    try:
        file = open('einat_world_bank.json', encoding="utf8")
        file_content = file.read()
        file.close()
        if file_content.find(text_to_find) != -1:
            print("Text '{0}' was found in the Json file".format(text_to_find))
        else:
            print("Text was NOT found in the Json file")
    except FileNotFoundError:
        print("File was not found!")
        sys.exit()


create_locale_json_from_url('http://a360ci.s3.amazonaws.com/Jmx/einat_world_bank.json', 'einat_world_bank.json')  # for question 1
does_json_contain_the_value('90224b0817be218_1_0')  # for question 2
