import datetime

class Posts():
    def __init__(self, title, body, author):
        self._post = {
            'title': title,
            'body': body,
            'author': author,
            'date': datetime.datetime.now().strftime('%Y/%h/%d, %H:%M:%S')
        }
        self._comments = []
    
    @property
    def title(self):
        return self._post['title']        

    @property
    def body(self):
        return self._post['body'] 

    @property
    def author(self):
        return self._post['author'] 

    @property
    def serialize(self):
        return self._post

    def get_comments(self):
        return self._comments

    def add_comment(self, body, author):
        self._comments.append(
            {
            'body': body,
            'author': author,
            'date': datetime.datetime.now().strftime('%Y/%h/%d, %H:%M:%S')
            }
        )