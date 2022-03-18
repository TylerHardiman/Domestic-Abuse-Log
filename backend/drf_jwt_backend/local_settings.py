SECRET_KEY = 'django-insecure-J+OeQ8UNz272bjpe2YdOtY3NgzpUnlkQT8Tk2+QG'
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'domestic_abuse_db',
        'USER': 'root',
        'PASSWORD': 'BingBong',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': 'True',
        }
        
        
    }
}
