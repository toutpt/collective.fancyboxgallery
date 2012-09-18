"""This is an integration "unit" test. It uses PloneTestCase, but does not
use doctest syntax.

You will find lots of examples of this type of test in CMFPlone/tests, for
example.
"""

from collective.gallery.tests import base


class TestSetup(base.TestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def setUp(self):
        super(TestSetup, self).setUp()
        self.portal_types = self.portal.portal_types

    def beforeTearDown(self):
        pass

    def testInstalledAddon(self):
        qi = self.portal.portal_quickinstaller
        for addon in ('collective.gallery',
                      'collective.js.fancybox',
                      'collective.configviews',
                      'collective.js.easing'):
            qi.isProductInstalled(addon)


def test_suite():
    return base.build_test_suite((TestSetup,))
