import facebook
import json

token = 'EAAC7ehlAHnQBAG4NqtfNKeMJi3oz1IPsrauMjnLIgvQy7oIkDFV5xJ8AHfNC3DZBwjy0zG2QYsKOBtOUu6WXDBZCqvt3wePzVSqRwdr2BZCaMIN7S4Cwe3rddsl2ih0LQdQLik1mZAIP3QJVVpJLutiiQWUymb5m7F4qTKqQtAZDZD'

fb = facebook.GraphAPI(access_token=token)
me=fb.get_object('me')
share = fb.put_object(parent_object=me['id'], connection_name='feed', message='Salam')
print(share)
# fields = ['id','last_name']
# a = fb.get_object('me', fields=fields)

print(me['name'])
# b= fb.put_object(parent_object='me',connection_name='Guluzade',messages='hello')
# # print(json.dumps(a))
# print(b)
