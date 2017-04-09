import plone.api
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

@provider(IContextSourceBinder)
def available_countries(context):
    catalog = plone.api.portal.get_tool('portal_catalog')
    countries = catalog.uniqueValuesFor('country')

    return SimpleVocabulary([SimpleTerm(value=country, title=country) for country in countries])

@provider(IContextSourceBinder)
def available_artists(context):
    catalog = plone.api.portal.get_tool('portal_catalog')
    countries = catalog.uniqueValuesFor('country')

    return SimpleVocabulary([SimpleTerm(value=country, title=country) for country in countries])