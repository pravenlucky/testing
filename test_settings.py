DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite',
    }
}

INSTALLED_APPS = [
    'nocaptcha_recaptcha',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
]

#NORECAPTCHA_SECRET_KEY = '6LeXfxQUAAAAAIIvSfPPscuPLqQBGPdiEF5EB5FS'
#NORECAPTCHA_SITE_KEY = '6LeXfxQUAAAAAK-yPbVnuorXVn2nWPoZCzSbY-Gw'

NORECAPTCHA_SECRET_KEY = '6LdY7hQUAAAAAGXpHoxbqyW3koV915Uc9-O_MYiT'
NORECAPTCHA_SITE_KEY = '6LdY7hQUAAAAAIDgqtIh9437ahDaeBwssJmKssCW'
