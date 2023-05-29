# from bs4 import BeautifulSoup
US_CITIES = {}


def parse_cities():
    file = open("./scheduler/support/cities.txt", "r")
    lines = file.readlines()

    for row in lines:
        curr_row = row.split(",")
        US_CITIES.append(curr_row[1])

    # with open("./scheduler/support/cities.txt", "r") as fp:
    #     soup = BeautifulSoup(fp)
    #     table = soup.find("table", 'table-condensed')
    #     for row in table.findAll('tr')[0:]:
    #         col = row.findAll('td')
    #         city = col[1].find('a').text.split('\n')[0]
    #         US_CITIES.append(city)

    # print(US_CITIES)