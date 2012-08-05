from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class ImageFetch(BrowserView):
  def __call__(self, url):
    from urllib import urlopen
    f=urlopen(url)
    img = f.read()
    id = url.split('/')[-1]
    
    self.context.invokeFactory('Image',id)
    self.context[id].setImage(img)
    return self.context[id]()

class WebpageFetch(BrowserView):
  def __call__(self, url):
    from urllib import urlopen
    f=urlopen(url)
    text = f.read()
    id = url.split('/')[-1]
    
    self.context.invokeFactory('Document',id)
    self.context[id].setText(text,mimetype="text/html")
    return self.context[id]()