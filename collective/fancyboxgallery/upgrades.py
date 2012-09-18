from Products.CMFCore.utils import getToolByName

PROFILE = 'profile-collective.fancyboxgallery:default'


def common(context):
    context.runAllImportStepsFromProfile(PROFILE)

