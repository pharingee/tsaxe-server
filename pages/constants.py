from django.utils.translation import ugettext_lazy as _

TOP_LEVEL = 't'
SUB_LEVEL = 's'
FOOTER = 'f'
NONE = 'n'

NAV_TYPE_CHOICES = (
    (NONE, _('none')),
    (TOP_LEVEL, _('top level')),
    (SUB_LEVEL, _('sub level')),
    (FOOTER, _('footer')),
)
