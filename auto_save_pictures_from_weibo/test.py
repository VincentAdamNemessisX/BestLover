from urllib import request
import pymysql

from bs4 import BeautifulSoup


def request_url():
    url = 'https://weibo.com/3179885602'
    html_content = request.urlopen(url)
    return parse_html(html_content)


def parse_html(html_content):
    html_str = html_content.read().decode('utf-8')
    html_soup = BeautifulSoup(html_str, 'html.parser')





def main():
    result = request_url()
    print(result)


if __name__ == '__main__':
    main()