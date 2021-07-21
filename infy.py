panel1 = []
panel2 = []
from bs4 import BeautifulSoup

with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        panel1.append('https://infosys.webex.com/meet/' + str(line[0:len(line)-1]))
with open('input2.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        panel2.append('https://infosys.webex.com/meet/' + str(line[0:len(line)-1]))
finalurl = []
import requests
for i in range(0,len(panel1)):
    request = requests.get(panel1[i])
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        tag = soup.find('script')
        if(tag.contents == []):
            print(panel1[i])
        else:
            request1 = requests.get(panel2[i])
            if request1.status_code == 200:
                soup = BeautifulSoup(request1.content, 'html.parser')
                if(tag.contents == []):
                    print(panel2[i])
                else:
                    print('No webex')
            else:
                print('No webex')           
    else:
        request1 = requests.get(panel2[i])
        if request1.status_code == 200:
            soup = BeautifulSoup(request1.content, 'html.parser')
            if(tag.contents == []):
                print(panel2[i])
            else:
                print('No webex')
        else:
            print('No webex')