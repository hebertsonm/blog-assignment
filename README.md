# blog-assignment

## Test APIs

Run the server and perform `curl` commands

```
 curl -d '{"title":"value2", "body":"value2", "author":"Jane"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/post
 curl -d '{"body":"value11", "author":"Jane"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/comment/0
 curl -X GET  http://127.0.0.1:5000/api/post/0
 curl -X GET  http://127.0.0.1:5000/api/comment/0
```