from settings import *
from v1.thenewboston_api import thenewbostonApi

API = thenewbostonApi(IP_ADDRESS, PORT, API_TOKEN)


def main():
    for major in API.get_majors_or_course('majors'):
        print(major)


"""
def main():

    print('\n----- All Majors -----')
    for major in API.get_majors_or_course('majors'):
        print(major['name'])

    print('\n----- Courses -----')
    for course in API.get_majors_or_course('computer-science'):
        print(course['name'])

    print('\n----- Videos -----')
    for video in API.get_videos(1):
        print(video['title'])
"""

if __name__ == '__main__':
    main()
