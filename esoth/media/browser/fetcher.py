from urllib2 import urlopen
import os
import plone.api
from Products.Five.browser import BrowserView

blockers = [
    '//imgur.com',
    '//m.imgur.com',
    '//i.imgur.com',
]

BASE = '//www.esoth.com'
if os.name == 'nt':
    BASE = 'http://localhost:8080/Plone'


def proxify(url):
    return '%s/proxy?u=http:%s' % (BASE, url)


class ProxyFetch(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        uri = self.request.get('uri') or self.request.get('u')

        f = urlopen(uri)
        contents = f.read()

        mimereg = plone.api.portal.get_tool('mimetypes_registry')
        mimetype = mimereg.lookupExtension(uri.split('.')[-1])
        if mimetype:
            self.request.response.setHeader('Content-Type', mimetype)
        else:
            for url in blockers:
                contents = contents.replace(url, proxify(url))
            self.request.response.setHeader('Content-Type', 'text/html')
        return contents
