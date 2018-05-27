import dash.dependencies
import dash_html_components as html
import dash_core_components as dcc
import os
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()

app.layout = html.Div(children=[

	html.Div(html.Label('Hello, what do you like to do in your free time?'),
			 style={
				'display': 'inline-block', 'vertical-align': 'middle',
				'textAlign': 'center', 'font-size': '1.6em', 'width': '40%'
	}),
	html.Div(
		dcc.Dropdown(
		 id='example-dropdown',
			options=[
				{'label': 'Read books', 'value': 'read'},
				{'label': 'Bake cakes', 'value': 'bake'},
				{'label': 'Play with cars', 'value': 'cars'}
			],
			value='read'
		),style={
				'display': 'inline-block', 'vertical-align': 'middle',
				'textAlign': 'center', 'font-size': '1.6em', 'width': '40%'
	}),

    dcc.Graph(
        id='example-plot',
        figure={
            'data': [],
            'layout': {
                'title': ''
                }
            }
    ),
	html.Div(
		dcc.Markdown('''*Source:* [books](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/allbacks.html),
		[cakes](https://vincentarelbundock.github.io/Rdatasets/doc/lme4/cake.html),
		[toy cars](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/toycars.html)'''),
		style={'textAlign': 'center', 'font-size': '1.6em'}
	)
])

@app.callback(
    dash.dependencies.Output(component_id='example-plot', component_property='figure'),
    [dash.dependencies.Input(component_id='example-dropdown', component_property='value')]
)

def update_plot(choice):
	if choice == 'read':
		trace1 = go.Bar(x=[1], y=[628], name='Paperback')
		trace2 = go.Bar(x=[1], y=[796], name='Hard book')

		layout = go.Layout(
			title = 'Book weight in grams',
			showlegend = False,
			xaxis = dict(
				title = "Book type",
				showticklabels = False
			),
		)

		data = [trace1, trace2]
		fig = dict(data = data, layout = layout)

		return fig
	elif choice == 'bake':
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
		return fig

	elif choice == 'cars':
		cars = pd.read_csv(
			'https://vincentarelbundock.github.io/Rdatasets/csv/DAAG/toycars.csv',
			index_col = 0
		)
		trace = go.Box(
			x = cars.car,
			y = cars.distance,
		)

		layout = go.Layout(
			title = 'Toy car distance - different angles',
			showlegend = False,
			xaxis = dict(
				title = "Car number"),
			yaxis = dict(
				title = "Distance, meters"),
		)

		data = [trace]
		fig = dict(data = data, layout = layout)
		return fig
if __name__ == '__main__':
	app.run_server()
