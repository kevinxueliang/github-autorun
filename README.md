
A server side script for [Github Post Receive Hook](https://help.github.com/articles/post-receive-hooks).

## HOW TO

1.You can refer to scripts/example.py
2.Create your own python file under scripts/
3.Define a function named run
4.Each time your repository is updated, every run functions will run

## Configuration 

Using flask's config.from\_pyfile method to load configuration from file app.cfg (You need to create this file).

## LICENSE

[MIT](http://opensource.org/licenses/MIT)
