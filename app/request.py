import urllib.request,json
from .models import Source,Articles


# Getting the api key
# Getting the base url
base_url = None
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']

def get_sources():
    '''
    functions that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = []
        
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
            print(source_results_list)
            
        return source_results

def process_results(source_list):
    '''
    functions that process the sources result and transforms them to a list of objects
    Args:
        source list:  A list of dictionaries that contain sources details
    returns:
        source results: A list of article objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        category= source_item.get('category')
        description = source_item.get('description')
        url= source_item.get('url')
        country = source_item.get('country')
        
        source_object = Source(id,name,category,description,url,country)
        source_results.append(source_object)

    return source_results

def get_articles(id):
    '''
    functions that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        # print(get_articles_response)

        articles_results = []
        

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
        
            
        return articles_results

def process_articles(articles_list):

    results = []
    for articles in articles_list:
        source=articles.get('source')
        author= articles.get('author')
        title = articles.get('title')
        description= articles.get('description')
        urlToImage= articles.get('urlToImage')
        url = articles.get('url')
        publishedAt = articles.get('publishedAt')
        content = articles.get('content')

        if urlToImage:
            articles_objects = Articles(source,author,title,description,url,urlToImage,publishedAt,content)
            results.append(articles_objects)
            
        
    return results
