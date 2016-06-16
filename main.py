from settings import *
from v1.thenewboston_api import thenewbostonApi

API = thenewbostonApi(IP_ADDRESS, PORT, API_TOKEN)


def adding_data_demo():
    API.add_major('adminToken', 'Apples', 'apples')
    API.add_video('adminToken', 2, 3, 'Title of Video', 'KQzxkeH3ebE')
    API.add_course('computer-science', 'adminToken', 'Course Category', 'Course Name', 3)


def getting_data_demo():

    print('\n----- All Majors -----')
    for major in API.get_majors_or_course('majors'):
        print(major)

    print('\n----- Courses -----')
    for course in API.get_majors_or_course('computer-science'):
        print(course)

    print('\n----- Videos -----')
    for video in API.get_videos(1):
        print(video)


if __name__ == '__main__':
    # adding_data_demo()
    getting_data_demo()
