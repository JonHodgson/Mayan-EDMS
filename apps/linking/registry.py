from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from smart_settings import LocalScope

from .icons import icon_smart_link_setup

label = _(u'Document linking')
description = _(u'Links documents together using a rule based system.')
dependencies = ['app_registry', 'icons', 'navigation', 'documents', 'metadata']
icon = icon_smart_link_setup
settings = [
    {
        'name': 'SHOW_EMPTY_SMART_LINKS',
        'default': True,
        'description': _(u'Show smart link that don\'t return any documents.'),
        'scopes': [LocalScope()]
    }
]
