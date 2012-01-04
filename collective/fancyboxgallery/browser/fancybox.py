from zope import interface
from zope import schema
from collective.configviews import ConfigurableBaseView
from collective.fancyboxgallery import i18n

_ = i18n.messageFactory

transition_vocabulary = ('fade','elastic','none')

class IFancyBoxSettings(interface.Interface):
    """http://fancybox.net/api"""

    padding = schema.Int(title=_(u"padding"),
                         description=i18n.padding_description,
                         default=10,
                         required=False)

    margin = schema.Int(title=_(u"margin"),
                         description=i18n.margin_description,
                         default=20,
                         required=False)

    opacity = schema.Bool(title=_(u"opacity"),
                          description=i18n.opacity_description,
                          default=False,
                          required=False)
 
    transitionIn = schema.ASCIILine(title=_(u"transitionIn"),
                                    description=i18n.transition_description,
                                    default='fade',
                                    #vocabulary=transition_vocabulary,
                                    )
    transitionOut = schema.ASCIILine(title=_(u"transitionOut"),
                                     description=i18n.transition_description,
                                     default='fade',
                                     #vocabulary=transition_vocabulary,
                                     )
#    speedIn = schema.Int
#    speedOut = schema.Int
#    overlayShow = schema.Bool


class FancyBoxGallery(ConfigurableBaseView):
    """View"""
    jsvarname = "fancyboxgallery"
    settings_schema = IFancyBoxSettings
