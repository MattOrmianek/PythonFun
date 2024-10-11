from fastapi import FastAPI
from blog.models import Blog
app = FastAPI()

@app.post("/blog")
def create_blog(blog: Blog):
    return {'Creating: ': blog.title, 'body: ': blog.body}