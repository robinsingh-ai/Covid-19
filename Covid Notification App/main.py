from bs4 import BeautifulSoup #pip intall bs4
from plyer import notification #pip install plyer
import requests
import time

def notify_me(title,message):
    notification.notify(

        title = title,
        message=message,
        app_name = "COVID -19 Notification ",
        app_icon = "D://Python Projects//COVID-19//virus.ico",
        timeout = 5

    )

def data_url(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    # notify_me('robin','singh')
    myData = data_url('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myData, 'html.parser')
    # print(soup.prettify())
    mydata1 = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        mydata1 += tr.get_text()
    mydata1 = mydata1[1:]
    items= mydata1.split('\n\n')
    #Entre Your States Name in the States array to get info
    states = ['Punjab','Maharashtra','Delhi','Chandigarh','Haryana']
    for item in items[0:41]:
        states_info = item.split('\n')
        if states_info[1] in states:
            print(states_info)
            ntitle = 'CASES OF COVID-19'
            nText = f"{states_info[1]}: \nActive Cases-{states_info[2]}\nCured Cases-{states_info[3]}\nDeaths-{states_info[4]}\tTotal Cases-{states_info[5]}"
            notify_me(ntitle,nText)
            time.sleep(5)

        # for table in soup.find_all('tbody'):
        # print(table.get_text())