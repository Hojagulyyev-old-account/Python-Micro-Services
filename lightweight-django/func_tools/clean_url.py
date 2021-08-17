''' Library for Micro Django URL Patterns  '''

from django.urls import path

# Break to two function
def rpath(url=None, view=None):
    try:
        if url.endswith('/'):
            url0 = url[:-1]
        else:
            url0 = url
        return [path('{}'.format(url0), view), path('{}/'.format(url0), view)]
    except:
        return [path('', view)]

# Connect my urlpatterns to urlpatterns
def connect(urlpatterns, my_urlpatterns):

    for url in my_urlpatterns:
        urlpatterns += url

    return urlpatterns
