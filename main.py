from bs4 import BeautifulSoup
import lxml

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find_all('h5')
    # print(tags)
    #
    # for course in tags:
    #     print(course.text)

    course_cards = soup.find_all('div', class_='card')  # _ = class is already an inbuilt variable in python

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')    # can be used for udemy courses at a glance