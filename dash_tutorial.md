# Dash for beautiful and easy data visualization

We will work with [example Dash app](https://github.com/anastazie/dash-pycon-2018/blob/master/example_project.py) 
that we will improve.

In our example we have data about books. Data comes from 
[the bookshelf of J. H. Maindonald](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/allbacks.html), 
who, apparently, likes to read.

What do you like to do in your free time: read, bake or maybe play with toy cars? 
Wouldn't it be interesting to know more about these activities? (*Spoiler*: yes, it would be interesting)

:scream_cat: **Task:** Then go ahead and add one more item to our dropdown menu named `Play with cars` with value name `cars`.

![](https://github.com/anastazie/dash-pycon-2018/blob/master/animated1.gif)

*Hint*: [Dropdown example](https://dash.plot.ly/dash-core-components/dropdown)

Perfect, now we will work with three datasets: [first one](https://vincentarelbundock.github.io/Rdatasets/doc/DAAG/allbacks.html) is already presented,
second dataset about [chocolate cake breakage](https://vincentarelbundock.github.io/Rdatasets/doc/lme4/cake.html)
and the third one containing data about [distance travelled by toy cars at varying angles](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/toycars.html). 

:scream_cat: **Task:** Lets put all the links to the datasets that we will be using to our page. Use [`dcc.Markdown`](https://dash.plot.ly/dash-core-components/markdown) component. A link is written as `[link text](link_url)`.

![](https://github.com/anastazie/dash-pycon-2018/blob/master/markdown_source.png)

:scream_cat: **Task:** And why don't we align this text to center.

Let's now look more into the structure of plot and move books plot to `update_plot` function, preparing our app to show different plots based on what data we choose.

###  🚀 Speed of light intoduction into plotly

Plots created using `plotly` library contain two major parts: data and layout. Here is an example of easy barplot:
```python
trace1 = go.Bar(x=[1], y=[628], name='Paperback')
trace2 = go.Bar(x=[1], y=[796], name='Hardcover')

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

`trace1` and `trace2` define data using plotly `go.Bar` object (we are using `go.Bar` because we want to draw barplot). 
Layout is made by using `go.Layout` object with varios parameter (look [docmentation](https://plot.ly/python/reference/) 
and [examples](https://plot.ly/python/bar-charts/)).

Last line is then putting it all together by creating dictionary of dictionaries.

In this tutorial, we will do barplots, scatterplots ([`go.Scatter`](https://plot.ly/python/line-and-scatter/)) and boxplots ([`go.Box`](https://plot.ly/python/box-plots/)).

:scream_cat: **Task:** Because we don't want any data to be hard-coded into UI of our app, we will create plotly plot inside our `update_plot` function (using code above) and erase data from `dcc.Graph` like this:
```python
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

`Pandas` is cool. 

Like, seriously, you can't do data preprocessing in Python without meeting `pandas`. It has enormous amout of nice functions, but we will look only at a few of them. I recommend you to take at least [10 minutes intro](https://pandas.pydata.org/pandas-docs/stable/10min.html) after the workshop.

We will work with data by loading them using `pd.read_csv` function (you don't need to download data, just pass URL). It produces a `pd.DataFrame` object. This data type is a table with numbered rows. The same that you can see in Excel. 

```python
cakes = pd.read_csv(
    'https://vincentarelbundock.github.io/Rdatasets/csv/lme4/cake.csv',
    index_col=0
)
```
Here, we are also specifying `index_col` parameter, because our CSV fike already contains index as it's first column.

*Note: if you want, you can look more at the data using Jupyter Notebook by running `jupyter notebook` in your terminal and creating python3 notebook file in Jupyter Notebook dashboard, more infor [here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html)*

:scream_cat: **Task:** Look at the beggining of the file using `cakes.head()`. 
If you want to know what columns are in `DataFrame`, use `columns` attribute. Then, if you want to select one column, use `cakes.angle` or `cakes['angle']` notations. For selecting multiple columns use `.loc` - `cakes.loc[, ['angle', 'recipe]]`. You can also use `.loc` to select rows - `cakes.loc[[6,7,12]]`.

Next function that we will be using is `groupby`, which is grouping rows in a table by the specified column to perform various functions (`mean`, `median`, `describe`, etc.).

Here is how we can get mean values of breakage angle for each temperature:

```python
cakes.groupby('temperature').angle.mean()
```

:scream_cat: **Task:** Here is the most interesting part, create scatter plot, where x axis is baking temperature (`temperature`) and y-axis is breakage angle (`angle`). But this is not all, use `value` in dropdown menu to decide in `update_plot` function what plot to show, so it will be something like this:

```python
def update_plot(choice):
  if choice == 'read':
    # create barplot from books data
    return fig
  if choice == 'bake':
    # create scatter plot from cake data
    return fig
  if choice == 'cars':
    fig = dict(data = [], layout = {})
    return fig
```
![](https://github.com/anastazie/dash-pycon-2018/blob/master/animated2.gif)

:scream_cat: **Task:** Last step is to add box plot with toy cars data. Make box plot for each car (`car`) on distance (`distance`) using `go.Box`.

Here is how your app should like like:

![](https://github.com/anastazie/dash-pycon-2018/blob/master/gif3_3.png)

Now have a break, it was intense! ☕
