import plone.api
from plone.app.contenttypes.interfaces import IFolder
from Products.Five.browser import BrowserView


class AlbumCollection(BrowserView):
    def albums(self):
        catalog = plone.api.portal.get_tool('portal_catalog')
        artist = self.request.get('artist', '')
        year = self.request.get('year', '')
        country = self.request.get('country', '')
        filter = {'portal_type': 'AlbumMetadata', 'sort_on': 'artistYear'}
        if artist:
            filter['artist'] = artist
        if country:
            filter['country'] = country
        if year:
            filter['year'] = int(year)

        return catalog(filter)

    def get_values(self, field):
        catalog = plone.api.portal.get_tool('portal_catalog')
        return catalog.uniqueValuesFor(field)

    def artists(self):
        return self.get_values('artist')

    def countries(self):
        return self.get_values('country')

    def years(self):
        return self.get_values('year')


class AlbumMetadata(BrowserView):
    def getcd(self, uid):
        catalog = plone.api.portal.get_tool('portal_catalog')
        return catalog(UID=uid)[0].getObject()

    def search_youtube(self):
        base = 'http://www.youtube.com/results?search_query='
        artist = '+'.join([i.replace(',', '') for i in self.context.artist.lower().split()])
        album = '+'.join([i.replace(',', '') for i in self.context.title.lower().split()])
        return base + '+'.join((artist, album))

    def search_base(self, context=None):
        if not context:
            context = self.context
        if not IFolder.providedBy(context):
            return self.search_base(context=context.aq_parent)
        else:
            return context.absolute_url()
