import requests
from datetime import datetime


def calc_age(uid):

    def get_information_of_user():
        params = {'v': '5.71',
                   'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
                   'user_ids': str(uid)}

        response = requests.get('https://api.vk.com/method/users.get', params=params)
        return str(response.json()['response'][0]['id'])

    def get_friends():
        params = {'v': '5.71',
                   'access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
                   'user_id': get_information_of_user(),
                   'fields': 'bdate'
                  }
        return requests.get('https://api.vk.com/method/friends.get', params=params).json()['response']['items']

    result = []

    for item in get_friends():
        if 'bdate' in item:
            bdate_str = item['bdate']
            splitted_date = bdate_str.split('.')
            if len(splitted_date) == 3:
                result.append(datetime.now().year - int(splitted_date[2]))
    result_counts = {}

    for item in result:
        if item not in result_counts:
            result_counts[item] = 1
        else:
            result_counts[item] += 1
    result_counts_list = [(k, v) for k, v in result_counts.items()]
    result_counts_list.sort(key=lambda element: (-element[1], element[0]))
    return result_counts_list


if __name__ == '__main__':
    print(calc_age('reigning'))
