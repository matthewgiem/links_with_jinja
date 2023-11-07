from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/post/<int:blog_id>')
def show_blog(blog_id):
    blog = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            blog = blog_post
    return render_template("post.html", post=blog)
    

if __name__ == "__main__":
    app.run(debug=True)
