from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class CDCollection(BrowserView):
  def albums(self):
    catalog = getToolByName(self.context,'portal_catalog')
    artist = self.request.get('artist','')
    year = self.request.get('year','')
    country = self.request.get('country','')
    filter = {'portal_type':'CDInfo'}
    if artist:
      filter['artist']=artist
    if country:
      filter['country']=country
    if year:
      filter['year']=year
    
    return catalog(filter)

  def artists(self):
    catalog = getToolByName(self.context,'portal_catalog')
    return catalog.uniqueValuesFor('artist')

  def countries(self):
    catalog = getToolByName(self.context,'portal_catalog')
    return catalog.uniqueValuesFor('country')

  def years(self):
    catalog = getToolByName(self.context,'portal_catalog')
    return catalog.uniqueValuesFor('year')

class CDInfo(BrowserView):
  def getcd(self,uid):
    catalog = getToolByName(self.context,'portal_catalog')
    return catalog(UID=uid)[0].getObject()