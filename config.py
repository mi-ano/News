import os
class Config:
   
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings.
    '''

    pass

class DevConfig(Config):
    '''
    Development configurations child class 
    args:
        config: The parent configurations class with general configurations settings
    '''

    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}
