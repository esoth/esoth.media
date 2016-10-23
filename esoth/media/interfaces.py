from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
import zope.schema as schema

from esoth.media import _


class IAlbumMetadata(model.Schema):
    """ Metadata for album collection """

    artist = schema.TextLine(
        title=_(u'Artist'),
        required=True,
    )

    country = schema.List(
        title=_(u'Country'),
        required=False,
        value_type=schema.TextLine(),
    )
    directives.widget(
        'subjects',
        AjaxSelectFieldWidget,
        vocabulary='esoth.media.Countries'
    )

    year = schema.Int(
        title=_(u'Year'),
        required=False,
    )

    img_url = schema.URI(
        title=_(u'Image URL'),
        required=False,
    )

    img = NamedBlobImage(
        title=_(u'Image'),
        required=False,
    )
