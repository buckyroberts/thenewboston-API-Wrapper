import json
import requests


class thenewbostonApi:

    def __init__(self, ip_address, port, api_token):
        self.ip_address = ip_address
        self.port = port
        self.api_token = api_token

    def add_course(self, major_slug, token, category, name, major_id):
        data = {
            'token': token,
            'category': category,
            'name': name,
            'major': major_id
        }
        r = requests.post(self.get_api_url() + major_slug + '/', data=data)
        if r.status_code == 201:
            print('Course has been added')
        else:
            print(str(r.status_code) + '\n' + r.text)

    def add_major(self, token, name, slug):
        data = {
            'token': token,
            'name': name,
            'slug': slug
        }
        r = requests.post(self.get_api_url() + 'majors/', data=data)
        if r.status_code == 201:
            print('Major has been added')
        else:
            print(str(r.status_code) + '\n' + r.text)

    def add_video(self, token, course_id, episode, title, youtube_code):
        data = {
            'token': token,
            'course': course_id,
            'episode': episode,
            'title': title,
            'youtube_code': youtube_code
        }
        r = requests.post(self.get_api_url() + 'videos' + '/', data=data)
        if r.status_code == 201:
            print('Video has been added')
        else:
            print(str(r.status_code) + '\n' + r.text)

    def get_majors_or_course(self, keyword):
        r = requests.get(self.get_api_url() + keyword + '/')
        if r.status_code != 200:
            print('Could not get majors')
            return False
        return json.loads(r.text)

    def get_videos(self, course_id):
        r = requests.get(self.get_api_url() + 'videos' + '/' + str(course_id) + '/')
        if r.status_code != 200:
            print('Could not get majors')
            return False
        return json.loads(r.text)

    def get_api_url(self):
        url = 'http://' + self.ip_address
        if self.port is not '':
            url += ':' + self.port
        url += '/v1/'
        return url
