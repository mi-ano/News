import os

class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=4185bf275a994ad3bd6ebcb379996bb5'
    EVERYTHING_URL = 'https://newsapi.org/v2/everything?sources={}&apikey={}'
    SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    CATEGORY_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    LANGUAGE_URL = 'https://newsapi.org/v2/sources?language={}&apiKey={}'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q=apple&from=2019-07-28&to=2019-07-28&sortBy=popularity&apiKey=4185bf275a994ad3bd6ebcb379996bb5'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config : the parent configuration class with General configuration settings
    '''
    DEBUG = True



config_options={
    'development':DevConfig,
    'production':ProdConfig
}

