# Dash for beautiful and easy data visualization

1. ## Adding item to dropdown menu.

Here is our dropdown menu:
```
dcc.Dropdown(
			id = 'example-dropdown',
			options = [
				{'label': 'Read books', 'value': 'read'},
				{'label': 'Bake cakes', 'value': 'bake'},
			],
			value = ''
		)
```
In order to add another item, we need to add another `dict` to `options`, we will add `{'label': 'Play with cars', 'value': 'cars'}`.

Now we need to add default value, we will do that by replacing empty string with `'cars'`. Here is our resulting dropdown:

```
dcc.Dropdown(
		 id='example-dropdown',
			options=[
				{'label': 'Read books', 'value': 'read'},
				{'label': 'Bake cakes', 'value': 'bake'},
				{'label': 'Play with cars', 'value': 'cars'}
			],
			value='read'
		)
```
