from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.fancyboxgallery import i18n
_ = i18n.messageFactory

transitions = SimpleVocabulary(
    [SimpleTerm(value=u'elastic', title=_(u'elastic')),
     SimpleTerm(value=u'fade', title=_(u'fade')),
     SimpleTerm(value=u'none', title=_(u'none'))]
    )
scrolls = SimpleVocabulary(
    [SimpleTerm(value=u'auto', title=_(u'auto')),
     SimpleTerm(value=u'yes', title=_(u'yes')),
     SimpleTerm(value=u'no', title=_(u'no'))]
    )
titlePositions = SimpleVocabulary(
    [SimpleTerm(value=u'outside', title=_(u'outside')),
     SimpleTerm(value=u'inside', title=_(u'inside')),
     SimpleTerm(value=u'over', title=_(u'over'))]
    )
fades = SimpleVocabulary(
    [SimpleTerm(value=u'fast', title=_(u'fast')),
     SimpleTerm(value=u'slow', title=_(u'slow'))]
    )
