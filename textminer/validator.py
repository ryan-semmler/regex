import re


def binary(string_input):
    return re.findall(r'[0-1]*[2-9]?', string_input) == re.findall(r'[0-1]*', string_input) and len(re.findall(r'[0-1]*', string_input)[0]) > 0


def binary_even(string_input):
    return binary(string_input) and len(re.findall(r'0$', string_input)) == 1


def hex(string_input):
    return re.findall(r'[0-9a-fA-F]*[g-zG-Z]?', string_input) == re.findall(r'[0-9a-fA-F]*', string_input) and len(re.findall(r'[0-9a-fA-F]*', string_input)[0]) > 0


def word(string_input):
    return len(re.findall(r'[a-zA-Z0-9 -]*', string_input)[0]) == len(string_input) and len(string_input) > 0 and len(re.findall(r'[a-zA-Z]', string_input)) >= 1


def words(string_input, count=False):
    return word(string_input) and not count or len(re.findall(r'[0-9]*[-]?[a-zA-Z][\S]*', string_input)) == count and word(string_input) and count > 0


def phone_number(string_input):
    return len(re.findall(r'^[\D]?[0-9]{3}[\D]?[\s]?[0-9]{3}[\D]?[0-9]{4}$', string_input)) >= 1


def money(string_input):
    return len(re.findall(r'^[$](([0-9]{1,3})|([0-9]{1,3},?[0-9]{3})|([0-9]{1,3},?[0-9]{3},?[0-9]{3}))([.][0-9]{2})?$', string_input)) >= 1


def zipcode(string_input):
    return len(re.findall(r'^[0-9]{5}$|([0-9]{5}-[0-9]{4}$)', string_input)) == 1


def date(string_input):
    return len(re.findall(r'^([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})|([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})', string_input)) == 1
