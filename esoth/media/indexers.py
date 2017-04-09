from plone.indexer.decorator import indexer
from unidecode import unidecode

from interfaces import IAlbumMetadata


@indexer(IAlbumMetadata)
def country(object):
    return object.country


@indexer(IAlbumMetadata)
def artist(object):
    return object.artist


@indexer(IAlbumMetadata)
def year(object):
    return object.year

@indexer(IAlbumMetadata)
def img_name(object):
    if object.image:
        return object.image.filename


@indexer(IAlbumMetadata)
def artistYear(object):
    return ''.join([an for an in unidecode(object.artist) if an.isalnum()]) + ' ' + str(object.year)


@indexer(IAlbumMetadata)
def SearchableText(object):
    return u' '.join((
        unidecode(object.title),
        unidecode(object.artist),
    )) + u' '.join([unidecode(country) for country in object.country])
