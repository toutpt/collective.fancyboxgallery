from zope import interface
from zope import schema
from collective.configviews import ConfigurableBaseView
from collective.fancyboxgallery import i18n
from collective.fancyboxgallery import vocabulary
from collective.js.easing.vocabulary import easings as vocabulary_easings

_ = i18n.messageFactory

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

    modal = schema.Bool(title=_(u"modal"),
                description=i18n.modal_description,
                default=False)

    cyclic= schema.Bool(title=_(u"cyclic"),
                description=i18n.cyclic_description,
                default=False)

    scrolling = schema.Choice(title=_(u"scrolling"),
                description=i18n.scrolling_description,
                default='auto',
                vocabulary=vocabulary.scrolls)

    autoScale = schema.Bool(title=_(u"autoScale"),
                description=i18n.autoScale_description,
                default=True)

    overlayOpacity = schema.ASCIILine(title=_(u"overlayOpacity"),
                description=i18n.overlayOpacity_description,
                default='0.3')

    overlayColor = schema.ASCIILine(title=_(u"overlayColor"),
                description=i18n.overlayColor_description,
                default='#666')

    titleShow = schema.Bool(title=_(u"titleShow"),
                description=i18n.titleShow_description,
                default=True)

    titlePosition = schema.Choice(title=_(u"titlePosition"),
                description=i18n.titlePosition_description,
                default='outside',
                vocabulary=vocabulary.titlePositions)

    transitionIn = schema.Choice(title=_(u"transitionIn"),
                                 description=i18n.transition_description,
                                 default='fade',
                                 vocabulary=vocabulary.transitions)

    transitionOut = schema.Choice(title=_(u"transitionOut"),
                                  description=i18n.transition_description,
                                  default='fade',
                                  vocabulary=vocabulary.transitions)

    speedIn = schema.Int(title=_(u"speedIn"),
                description=i18n.speed_description,
                default=300)

    speedOut = schema.Int(title=_(u"speedOut"),
                description=i18n.speed_description,
                default=300)

    changeSpeed = schema.Int(title=_(u"changeSpeed"),
                description=i18n.changeSpeed_description,
                default=300)

    changeFade = schema.Choice(title=_(u"changeFade"),
                description=i18n.changeFade_description,
                default='fast',
                vocabulary=vocabulary.fades)

    easingIn = schema.Choice(title=_(u"easingIn"),
                description=i18n.easing_description,
                default='swing',
                vocabulary=vocabulary_easings)

    easingOut = schema.Choice(title=_(u"easingOut"),
                description=i18n.easing_description,
                default='swing',
                vocabulary=vocabulary_easings)

    showCloseButton = schema.Bool(title=_(u"showCloseButton"),
                description=i18n.showCloseButton_description,
                default=True)


class FancyBoxGallery(ConfigurableBaseView):
    """View"""
    jsvarname = "fancyboxgallery"
    settings_schema = IFancyBoxSettings
