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

3. ## Adding conditions based in `update_plot` function

The idea here is that ased on user input `update_plot` function shows different plot. By user input we mean selecting item from dropdown. Selected value is then stored in `choice` variable of our callback function. 
Now we need to create scatterplot, we can use following pies of code:
```python
cakes = pd.read_csv(
			'https://vincentarelbundock.github.io/Rdatasets/csv/lme4/cake.csv',
			index_col = 0
)
trace = go.Scatter(
	x = cakes.groupby('temperature').angle.mean().index,
	y = cakes.groupby('temperature').angle.mean(),
	mode = 'markers+lines'
)

layout = go.Layout(
	title = 'Chocolate cake breakage - various baking temperatures',
	showlegend = False,
	xaxis = dict(
		title = "Baking temperature, degrees F"),
)

data = [trace]
fig = dict(data = data, layout = layout)
```

Few comments on this code:
- Data are loaded using `pd.read_csv`
- Data are then grouped based on value of `temperature` variable using `groupby`
- Mean value is computed on grouped data
- To show both points and lines in scatterplot, `mode = 'markers+lines'` is used

In the same way, boxplot is created for toy cars data. You can see resulting file [here](https://github.com/anastazie/dash-pycon-2018/blob/master/example_project5.gif)
