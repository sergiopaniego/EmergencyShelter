# Emergency Shelter backend
import requests

url = "https://api.telegram.org/bot401538688:AAHmvB5Md-qjqMSGhhiLs7mJJVnxbBAyJLY/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))

send_mess(chat_id, 'Welcome to the Emergency Shelter bot. Please select an option from those offered so we can help you')

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           #send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
           #print(last_update(get_updates_json(url))['message']['text'])
           if last_update(get_updates_json(url))['message']['text'] == '/offershelter':
               send_mess(get_chat_id(last_update(get_updates_json(url))), 'Offer shelter option selected')
           elif last_update(get_updates_json(url))['message']['text'] == '/seekshelter':
               send_mess(get_chat_id(last_update(get_updates_json(url))), 'Seek shelter option selected')
    sleep(1)

if __name__ == '__main__':
    main()