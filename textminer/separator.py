import re


def words(string_input):
    return re.findall(r'[0-9]*[-]?[a-zA-Z][\S]*', string_input)


def phone_number(string_input):
    if len(re.findall(r'^[\D]?[0-9]{3}[\D]?[\s]?[0-9]{3}[\D]?[0-9]{4}$', string_input)) >= 1:
        return {"area_code": re.search(r'[0-9]{3}', string_input)[0], "number": re.findall(r'[0-9]{3}(?=[\D]?[0-9]{4}$)', string_input)[0] + '-' + re.findall(r'[0-9]{4}$', string_input)[0]}
    return None


def money(string_input):
    result = {}
    if string_input[0] == "$":
        result["currency"] = "$"
    else:
        return None
    dollars = re.findall(r'[0-9]{1,3}', string_input)
    dollars = dollars[0]
    if len(dollars) == 0:
        return None
    cents = re.findall(r'[.][0-9]{1,3}', string_input)
    cents = cents[0]
    if len(cents) != 2:
        return None


while True:
    print(phone_number(input()))
