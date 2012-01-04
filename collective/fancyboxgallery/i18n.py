
from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory('collective.fancyboxgallery')
ploneMessageFactory = MessageFactory('plone')

_ = messageFactory

padding_description = _(u"padding_description",
                   default=u"Space between FancyBox wrapper and content")

transition_description =_(u"transitionIn_description",
                            default=u"The transition type. Can be set to 'elastic', 'fade' or 'none'")

margin_description = _(u"margin_description",
                   default=u"Space between viewport and FancyBox wrapper")

opacity_description = _(u"opacity_description",
                        default=u"When true, transparency of content is changed for elastic transitions")