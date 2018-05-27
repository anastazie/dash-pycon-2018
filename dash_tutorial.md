# Dash for beautiful and easy data visualization

We will work with [example Dash app](https://github.com/anastazie/dash-pycon-2018/blob/master/example_project.py) 
that we will improve.

In our example we have data about books, data comes from 
[the bookshelf of J. H. Maindonald](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/allbacks.html), 
who, apparently, like to read.

What do you like to do in your free time: read bake or may be play with toy cars? 
Wouldnt it be interesting to know more about these activities? (*Spoiler*: yes, it would be interesting)

Then go ahead and add one more item to our dropdown menu named `Play with cars` with value name `cars`.

![](https://github.com/anastazie/dash-pycon-2018/blob/master/animated1.gif)

*Hint*: [Dropdown example](https://dash.plot.ly/dash-core-components/dropdown)

Perfect, now we will work with three datasets: [first one](https://vincentarelbundock.github.io/Rdatasets/doc/DAAG/allbacks.html) is already presented,
second dataset about [chocolate cake breakage](https://vincentarelbundock.github.io/Rdatasets/doc/lme4/cake.html)
and the third one containing data about [distance travelled by toy cars at varying angles](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/toycars.html). Lets put all the links to teh dataset that we will be using on our page. Use [`dcc.Markdown`](https://dash.plot.ly/dash-core-components/markdown) component and following notation to add links `[link text](link_url)`. 

![](https://github.com/anastazie/dash-pycon-2018/blob/master/markdown_source.png)

Additional task: align this text to center.

Let's now look more into the structure of plot and move books plot to `update_plot` function, preparing our app to show different plots based on what data we choose.

###  🚀 Speed of light intoduction into plotly

Plot using plotly library contain two major parts: data and layout. Here is an example of easy barplot:
```
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
```

`trace1` and `trace2` define data using plotly `go.Bar` object. 
Layout is made by using `go.Layout` object with varios parameter (look [docmentation](https://plot.ly/python/reference/) 
and [examples](https://plot.ly/python/bar-charts/)).

Last line is then putting it all together by creating dictionary of dictionaries.

In this tutorial, we will do barplots, scatterplots ([`go.Scatter`](https://plot.ly/python/line-and-scatter/)) and boxplots ([`go.Box`](https://plot.ly/python/box-plots/)).

Because dont want any data to be hard-coded into UI of our app, we will create ploltly plot inside our `update_plot` function (using code above) and erase data from `dcc.Graph` like this:
```
dcc.Graph(
        id='example-plot',
        figure={
            'data': [],
            'layout': {
                'title': ''
                }
            }
    ),
```
The only one more thing we need to change is to make `update_plot` function to return `fig`

###  🚀 Speed of light intoduction into pandas
