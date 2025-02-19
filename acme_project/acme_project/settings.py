from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-m&$lzdzkutvrbr5vt=jpm)7#g7cken_tk%($ty+w902n7wb#=e'

DEBUG = True

CSRF_FAILURE_VIEW = 'core.views.csrf_failure'

ROOT_URLCONF = 'acme_project.urls'

LOGIN_REDIRECT_URL = 'pages:homepage'

LOGIN_URL = 'login'

STATIC_URL = '/static/'

TEMPLATES_DIR = BASE_DIR / 'templates'

MEDIA_ROOT = BASE_DIR / 'media'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Подключаем бэкенд filebased.EmailBackend:
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# Указываем директорию, в которую будут сохраняться файлы писем:
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'birthday.apps.BirthdayConfig',
    'users.apps.UsersConfig',
    'core.apps.CoreConfig',
    'pages.apps.PagesConfig',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (TEMPLATES_DIR,),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'acme_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Переопределяем форматы ввода даты
# DATE_INPUT_FORMATS = [
#     '%Y-%m-%d',  # '2006-10-25'
#     '%d/%m/%Y',  # '25/10/2006'
#     '%d.%m.%Y',  # '25.10.2006'
#     '%d-%m-%Y',  # '25-10-2006'
#     '%m/%d/%Y',  # '10/25/2006' (американский формат)
# ]
