from flask import Flask, jsonify, abort, request
import classes

api = Flask(__name__)

posts = [] # Create posts list to receive a list of Post objects
INDEX_NOT_FOUND = 'Index not found'

# Initial page
@api.route('/')
def home():
    return "Blog EA backend"

# Define blog post APIs
@api.route('/api/post/<int:post_id>', methods=['GET'])
def get_post(post_id):
  if post_id > len(posts) - 1:
    return INDEX_NOT_FOUND
  return jsonify(posts[post_id].serialize)

@api.route('/api/post', methods=['GET'])
def get_posts():
  result = []
  for post in posts:
    result.append(post.title)

  return jsonify(result)

@api.route('/api/post', methods=['POST'])
def post_post():
    if not request.json or not 'title' in request.json:
        abort(400)
    post = classes.Posts(request.json['title'],request.json['body'],request.json['author'])
    posts.append(post)

    return '%s posted successfully!' % post.title

@api.route('/api/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
  for post in posts:
    if posts.index(post) == post_id:
      posts.remove(post)
      return 'deleted'
  return INDEX_NOT_FOUND

# Define post comments APIs
@api.route('/api/comment/<int:post_id>', methods=['GET'])
def get_comments(post_id):
  if post_id > len(posts) - 1:
    return INDEX_NOT_FOUND
  comments = posts[post_id].get_comments()

  return jsonify(comments)

@api.route('/api/comment/<int:post_id>', methods=['POST'])
def post_comments(post_id):
    if not request.json or not 'body' in request.json:
        abort(400)

    if post_id > len(posts) - 1:
      return INDEX_NOT_FOUND

    posts[post_id].add_comment(request.json['body'],request.json['author'])

    return 'comment posted successfully!'

if __name__ == '__main__':
    api.run(debug=True)
