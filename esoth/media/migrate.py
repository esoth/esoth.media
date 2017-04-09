import logging

import plone.api
from Products.Five import BrowserView
from plone.app.contenttypes.migration.dxmigration import ContentMigrator, migrate
from plone.app.contenttypes.migration.field_migrators import migrate_simplefield, migrate_imagefield, migrate_richtextfield
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides


class Media(ContentMigrator):
    src_portal_type = 'CDInfo'
    src_meta_type = 'CDInfo'
    dst_portal_type = 'AlbumMetadata'
    dst_meta_type = None  # not used

    def migrate_atctmetadata(self):
        pass

    def migrate_schema_fields(self):
        migrate_simplefield(self.old, self.new, 'artist', 'artist')
        migrate_simplefield(self.old, self.new, 'country', 'country')
        migrate_simplefield(self.old, self.new, 'year', 'year')
        migrate_richtextfield(self.old, self.new, 'notes', 'notes')
        migrate_simplefield(self.old, self.new, 'imgUrl', 'img_url')
        migrate_imagefield(self.old, self.new, 'image', 'image')


class MigrateMedia(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        logger = logging.getLogger('ATCT.migration')
        logger.setLevel(0)
        logger = logging.getLogger('plone.app.contenttypes.migration.field_migrators')
        logger.setLevel(0)
        qi = plone.api.portal.get_tool('portal_quickinstaller')
        #qi.uninstallProducts(['esoth.media'])
        qi.installProduct('esoth.media')
        portal = plone.api.portal.get()
        migrate(portal, Media)
