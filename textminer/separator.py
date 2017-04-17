import re


def words(string_input):
    return re.findall(r'[0-9]*[-]?[a-zA-Z][\S]*', string_input)


def phone_number(string_input):
    if len(re.findall(r'^[\D]?[0-9]{3}[\D]?[\s]?[0-9]{3}[\D]?[0-9]{4}$', string_input)) >= 1:
        return {"area_code": re.search(r'[0-9]{3}', string_input)[0], "number": re.findall(r'[0-9]{3}(?=[\D]?[0-9]{4}$)', string_input)[0] + '-' + re.findall(r'[0-9]{4}$', string_input)[0]}
    return None


def money(string):
    result = re.search(r'^(?P<symbol>[$]{1})'
                       r'(?P<number>(([\d]+([.][\d]{2}){0,1})$'
                       r'|([\d]{1,3}([,][\d]{3})+([.][\d]{2}){0,1})))', string)
    if result:
        return {'currency': result.group('symbol'),
                'amount': float(re.sub('[,]', '', result.group('number')))}
    return None


def zipcode(text):
    result = re.search(r'^(?P<zip5>[\d]{5})(-(?P<plus4>[\d]{4}))?$', text)
    if result:
        return {"zip": result.group('zip5'), "plus4": result.group('plus4')}


def date(text):
    result = re.search(r'^(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<year>[\d]{4})$', text)
    if not result:
        result = re.search(r'^(?P<year>[\d]{4})-(?P<month>[\d]{1,2})-(?P<day>[\d]{1,2})$', text)
    if not result:
        return None
    return {"month": int(result.group('month')), 'day': int(result.group('day')), 'year': int(result.group('year'))}
