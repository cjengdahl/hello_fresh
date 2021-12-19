# Hello Fresh PDF Server

Flask app to serve accumulated Hello Fresh recipes.

## Usage

For each recipe, add a directory to `static/recipes` containing
a cover photo `photo.jpeg` and the recipe `recipe.pdf`.

See toast as an example.

```bash

export FLASK_APP=hello_fresh
python3 -m  flask run --host=0.0.0.0 --port=3000

```
