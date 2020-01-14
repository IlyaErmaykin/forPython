import requests;

f = True;
url = 'https://stepic.org/media/attachments/course67/3.6.3/';
urlFile = '699991.txt';
r = requests.get(url + urlFile);
print(r.text);

while(f):
    if(r.text[:2] != "We"):
        r = requests.get(url + r.text);
        print(r.text);
        continue;
    else:
        print(r.text);
        f = False;
        break;

