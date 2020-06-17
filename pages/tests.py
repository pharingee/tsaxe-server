from django.test import TestCase

from pages import models, constants


class PageTypeTestCase(TestCase):
    default_page_text = 'Default Page'

    def setUp(self):
        models.PageType.objects.create(
            name=self.default_page_text
        )

    def test_defaults(self):
        page = models.PageType.objects.get(
            name=self.default_page_text
        )
        self.assertEqual(self.default_page_text, page.name)
        self.assertEqual('default-page', page.slug)
        self.assertEqual(constants.NONE, page.nav_type)


class TagTestCase(TestCase):
    default_tag_text = 'Default Tag'

    def setUp(self):
        models.Tag.objects.create(
            name=self.default_tag_text
        )

    def test_defaults(self):
        tag = models.Tag.objects.get(
            name=self.default_tag_text
        )
        self.assertEqual(self.default_tag_text, tag.name)
        self.assertEqual('default-tag', tag.slug)
        self.assertEqual(True, tag.is_visible)
