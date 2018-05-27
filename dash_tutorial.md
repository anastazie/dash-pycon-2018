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
and the third one containing data about [distance travelled by toy cars at varying angles](http://math.furman.edu/~dcs/courses/math47/R/library/DAAG/html/toycars.html). Lets put all the links to teh dataset that we will be using on our page. Use [`dcc.Markdown`](https://dash.plot.ly/dash-core-components/markdown) component and following notation to add links `[link text](link_url)`
