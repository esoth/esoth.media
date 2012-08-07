from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from urllib2 import urlopen

class ImageFetch(BrowserView):
  def __init__(self,context,request):
    self.context=context
    self.request=request

  def __call__(self, u):
    f = urlopen(u)
    img = f.read()

    mimereg = getToolByName(self,'mimetypes_registry')
    mimetype = mimereg.lookupExtension(u.split('.')[-1])
    self.request.response.setHeader('Content-Type', mimetype)
    return img

class WebpageFetch(BrowserView):
  def __init__(self,context,request):
    self.context=context
    self.request=request

  def __call__(self, u):
    f = urlopen(u)
    text = f.read()

    self.request.response.setHeader('Content-Type', 'text/html')
    return text