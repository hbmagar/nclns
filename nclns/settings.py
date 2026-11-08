from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3%m$^nvcs8=z60ue3h7jkz$cx3$gy3=fq3k562tzs1j1ieuuwl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custome app list
    'header_app',
    'home_app',
    'about_us_app',
    'about_team_app',
    'service_app',
    'product_app',
    'gallery_app',
    'contact_app',
    'footer_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nclns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'header_app.context_processors.tab_items_processor',
                'footer_app.context_processors.footer_content_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'nclns.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nclns_data',
        'USER': 'root',
        'PASSWORD': 'Sony$2026',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


JAZZMIN_SETTINGS = {
    'site_title': "NCLNS",
    'site_logo': "../static/image/logo.png",
    "site_brand": "Nirmal Cleanness",
    'welcome_sign': "Welcome to NCLNS Admin",
    'copyright': "Nirmal Cleanness Pvt. Ltd.",
    "search_model": "auth.User",
    "show_ui_builder": True,
    "version": "5.2.5",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "footer_fixed": True,
    "sidebar_nav_compact_style": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "home_app": "fas fa-home",
        "header_app": "fas fa-header",
        "service_app": "fas fa-cogs",
        "product_app": "fas fa-boxes",
        "gallery_app": "fas fa-images",
        "contact_app": "fas fa-address-book",
    },
    "topmenu_links": [
        {"app": "home_app"},
        {"name": "Support", "url": "https://hbm.com.np/", "new_window": True},
    ],
    
   
   
    "order_with_respect_to": [
        # header app
        'header_app',
        'header_app.tabar',
        
        #home page
        'home_app',
        'home_app.index_slide',
        'home_app.our_business',
        'home_app.busisness_motive_list',
        'home_app.latest_product',
        'home_app.news_portal',
        'home_app.event_part',
        'home_app.experience_part',
        'home_app.feed_back',
        ''
        #about us app
        "about_us_app",
        "about_us_app.AboutUs",
        "about_us_app.about_aims",
        "about_us_app.about_partners_header",
        "about_us_app.partners_logo",

        #about team app
        "about_team_app",
        "about_team_app.TeamMember_title_part",
        "about_team_app.AdminTeamMember",
        "about_team_app.staffTeamMember",

        #Service app
        "service_app",
        "service_app.service_about_heading",
        "service_app.service_progress_aria",
        "service_app.feature_title",
        "service_app.service_feature",
        "service_app.service_Contact",

        # product app
        'product_app',
        'product_app.about_product',
        'product_app.product_list',
        'product_app.upcoming_product',
        'product_app.deals_product',

        #Gallery app
        "gallery_app",

        #Contact app
        "contact_app",

        #footer
        "footer_app",
        "footer_app.footer_about",
        "footer_app.recent_product_menu",
        
        #Authentcation app
        "auth",
        "auth.user",
        "auth.group",
    ],
   
}