import re


def parser_ques_id(data):
    s = str(data)
    s = s[2:len(s) - 2]
    regex = re.compile("\|\d*#\d*\|")
    return regex.split(s)