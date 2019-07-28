from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles
from ..models import Source,Articles

#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its page
    '''

    # getting new articles from different sources.
    sources = get_sources()

    title = 'Home - Welcome to the Best Online News.'
    return render_template('index.html', title=title, sources = sources)

@main.route('/source/<source>')
def source(source):
    '''
    view movie page function that returns the new movie details page
    '''
    articles = get_articles(source)
    title = 'Articles Page'

    return render_template('sources.html', articles = articles, title=title)
