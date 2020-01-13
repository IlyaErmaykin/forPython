import requests;

#r = requests.get('http://example.com');        # Get запрос
#print(r.text);                                 # Вывод ответа от сервера

#url = 'http://example.com';
#par = {'key1': 'value1', 'key2': 'value2'};
#r = requests.get(url, par);                    # Передача параметров в запрос 
#print(r.url);                                  # Вывод url-адреса с учетом параметров Get запроса

url = 'http://httpbin.org/cookies';
cookies = {'cookies_age': 'working'};
r = requests.get(url, cookies);                 # Отправка сформированных cookies на сервер
print(r.text);

print(r.cookies['example_cookie_name']);        # Использование cookies, полученных от сервера
