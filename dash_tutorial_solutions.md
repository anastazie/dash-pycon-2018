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

2. ## Adding markdown.

For this task we will use `dcc.Markdown` component:

```
dcc.Markdown('''*Source:* [books](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/allbacks.html),
		[cakes](https://vincentarelbundock.github.io/Rdatasets/doc/lme4/cake.html),
		[toy cars](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/toycars.html)'''),
```
In order to align this text to center, we need to wrap it into `html.Div` component and use it's `style` parameter (specifically set `'text-align'` to `'center'`). We can also set other parameters of `style`, such as `font-size`:
```
html.Div(
		dcc.Markdown('''*Source:* [books](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/allbacks.html),
		[cakes](https://vincentarelbundock.github.io/Rdatasets/doc/lme4/cake.html),
		[toy cars](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/toycars.html)'''),
		style={'textAlign': 'center', 'font-size': '1.6em'}
	)
```
