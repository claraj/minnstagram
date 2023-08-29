from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Example app data. For a real app, this would be stored persistently in a database.
# Every time we restart this app, we lose all the comments. 

posts = [
    {'id': 1, 'user': 'brunch_is_the_best_meal', 'text': 'So thankful I got to finally check out this new brunch place', 'url': 'brunch.jpeg', 'likes': 0},
    {'id': 2, 'user': 'ford_chevy_bmw', 'text': 'Another dream car on a dreary day', 'url': 'car.jpeg', 'likes': 10},
    {'id': 3, 'user': 'funny_cats', 'text': 'My cat looks very cool in these shades', 'url': 'cat.jpeg', 'likes': 0},
    {'id': 4, 'user': 'fashionista', 'text': 'New clothes day. What should I try on first???', 'url': 'clothes.jpeg', 'likes': 1},
    {'id': 5, 'user': 'world_traveler', 'text': 'Coffee in Manhattan, so delicious', 'url': 'coffee.jpeg', 'likes': 3},
    {'id': 6, 'user': 'get_outdoors', 'text': 'Worth getting up so early for these pictures!', 'url': 'hiking.jpeg', 'likes': 2310},
]

all_comments = [
    {'id': 3, 'text': 'what is your cats name?'},
    {'id': 6, 'text': 'incredible pictures!'},
    {'id': 6, 'text': 'wow, where is this?'},
    {'id': 6, 'text': 'jumping for joy!!'},
]

@app.route('/')
def homepage():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def one_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            comments = get_comments_for_post(post_id)
            return render_template('post.html', post=post, comments=comments)
    # error - this post does not exist
    return 'Post not found'


@app.route('/add_comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    form_data = request.form 
    comment = form_data['comment_text']
    new_comment = {'id': post_id, 'text': comment}
    all_comments.append(new_comment)
    return redirect(f'/post/{post_id}')


def get_comments_for_post(post_id):
    post_comments = []
    for comment in all_comments:
        if comment['id'] == post_id:
            post_comments.append(comment['text'])
    return post_comments 