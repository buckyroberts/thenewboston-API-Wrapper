import json
import requests


class thenewbostonApi:

    def __init__(self, ip_address, port, api_token):
        self.ip_address = ip_address
        self.port = port
        self.api_token = api_token

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
