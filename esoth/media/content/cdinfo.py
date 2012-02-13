# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.ATContentTypes import ATCTMessageFactory as _
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import RFC822Marshaller
from Products.Archetypes.atapi import StringField, IntegerField, ImageField, TextField, LinesField
from Products.Archetypes.atapi import StringWidget, IntegerWidget, ImageWidget, RichWidget, LinesWidget
from Products.ATContentTypes.content.base import ATCTContent, registerATCT
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.Archetypes.atapi import AnnotationStorage
from Products.CMFCore.permissions import View
from esoth.media.config import PROJECTNAME
from esoth.media.interfaces import ICDInfo
from zope.interface import implements

CDSchema = ATContentTypeSchema.copy() + Schema((
    StringField('artist',
        required = False,
        widget = StringWidget(
            label= u'Artist'),
    ),
    LinesField('country',
        required = False,
        widget = LinesWidget(
            label= u'Country'),
    ),
    IntegerField('year',
        required = False,
        widget = IntegerWidget(
            label= u'Year'),

    ),
    TextField('notes',
        required = False,
        widget = RichWidget(
            label= u'Notes'),

    ),
    StringField('imgUrl',
        required = False,
        widget = StringWidget(
            label= u'Image (url)'),

    ),
    ImageField('image',
        required = False,
        storage = AnnotationStorage(migrate=True),
        sizes= {'large'   : (768, 768),
                'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (170, 170),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
               },
        widget = ImageWidget(
            label= u'Image (upload)'),

    ),
    
    ),
    marshall=RFC822Marshaller()
    )
    
class CDInfo(ATCTContent):
    schema = CDSchema
    implements(ICDInfo)

    security = ClassSecurityInfo()

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = 'Album art'
        return self.getField('image').tag(self, **kwargs)

    security.declareProtected(View, 'hasTag')
    def hasTag(self):
        return self.getImage() and True or False
    
    
    security.declareProtected(View, 'artistYear')
    def artistYear(self):
        from Products.CMFPlone.utils import safe_unicode as su
        def anglicize(value):
          return su(value).replace(u'Ä',u'A')
        return '%s%s' % (anglicize(self.getArtist()),self.getYear())

registerATCT(CDInfo, PROJECTNAME)