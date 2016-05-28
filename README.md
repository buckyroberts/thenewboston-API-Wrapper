![](http://i.imgur.com/0Mlbb6y.png)

# About

This is a Python wrapper for thenewboston API.


### Get all majors or courses
`get_majors_or_course()` - returns an array of all majors or courses for a specific major

```
def main():
    for major in API.get_majors_or_course('majors'):
        print(major)
```

output:
```
{'id': 1, 'slug': 'beauty', 'name': 'Beauty'}
{'id': 2, 'slug': 'business', 'name': 'Business'}
{'id': 3, 'slug': 'computer-science', 'name': 'Computer Science'}
{'id': 4, 'slug': 'cooking', 'name': 'Cooking'}
```


### Get all videos for a course
`get_majors_or_course()` - returns an array of all videos for a course

```
def main():
    for video in API.get_videos(1):
        print(video)
```

output:
```
{'youtube_code': 'tp3Gw-oWs2k', 'course': 1, 'title': 'Introduction to AJAX', 'episode': 1}
{'youtube_code': '-1RLW7a8Gr4', 'course': 1, 'title': 'Some Examples of AJAX', 'episode': 2}
```
