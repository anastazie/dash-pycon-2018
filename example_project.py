import dash.dependencies
import dash_html_components as html
import dash_core_components as dcc
import os
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()

app.layout = html.Div(children=[

	html.Div(html.Label('Hello, what do you like to do in your free time?'),
			 style = {
				 'display': 'inline-block', 'vertical-align': 'middle',
				 'textAlign': 'center', 'font-size': '1.6em', 'width': '40%'
			 }),
	html.Div(
		dcc.Dropdown(
			id = 'example-dropdown',
			options = [
				{'label': 'Read books', 'value': 'read'},
				{'label': 'Bake cakes', 'value': 'bake'},
			],
			value = ''
		), style = {
			'display': 'inline-block', 'vertical-align': 'middle',
			'textAlign': 'center', 'font-size': '1.6em', 'width': '40%'
		}),

	dcc.Graph(
        id='example-plot',
        figure={
            'data': [
            	go.Bar(x=[1], y=[628], name='Paperback'),
                go.Bar(x=[1], y=[796], name='Hardcover')
            ],
            'layout': {
                'title': 'Book weight in grams'
                }
            }
    )
])

@app.callback(
    dash.dependencies.Output(component_id='example-plot', component_property='figure'),
    [dash.dependencies.Input(component_id='example-dropdown', component_property='value')]
)

def update_plot(choice):
	data=[]
	return data

if __name__ == '__main__':
	app.run_server()
