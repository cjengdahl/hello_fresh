import os
from flask import Flask, render_template

app = Flask("hello_fresh")

@app.route("/")
def hello_fresh():

    directory_contents = [d for d in os.listdir('./static/recipes') \
        if os.path.isdir('./static/recipes/' + d) and not d.startswith('.')]
    directory_contents.sort()
    num_rows = int(len(directory_contents) / 3) + 1

    recipes = []

    col_idx = 0
    while num_rows:
        recipes.append(directory_contents[col_idx: col_idx+3])
        col_idx += 3
        num_rows -= 1

    return render_template('hello_fresh.html', recipes=recipes)


if __name__ == '__main__':
    app.run(debug=False )