from django.conf.urls import url


urlpatterns=[
    url(r'^$','live_sport_app.views.dashboard',name='dashboard'),
    url(r'^create_order/$','live_sport_app.views.create_order',name='create_order')
]