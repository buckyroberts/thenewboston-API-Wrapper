![](http://i.imgur.com/0Mlbb6y.png)

# About

This is a Python wrapper for thenewboston API.


### Print a sorted set of all tickers
`get_majors_or_course()` - this returns an array of all majors or courses for a specific major

```
def main():
    for major in API.get_majors_or_course('majors'):
        print(major)
```

output:
```json
{'id': 1, 'slug': 'beauty', 'name': 'Beauty'}
{'id': 2, 'slug': 'business', 'name': 'Business'}
{'id': 3, 'slug': 'computer-science', 'name': 'Computer Science'}
{'id': 4, 'slug': 'cooking', 'name': 'Cooking'}
```