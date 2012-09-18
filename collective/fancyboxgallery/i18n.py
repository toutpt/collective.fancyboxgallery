
from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory('collective.fancyboxgallery')
ploneMessageFactory = MessageFactory('plone')

_ = messageFactory

padding_description = _(u"padding_description",
                 default=u"Space between FancyBox wrapper and content")

margin_description = _(u"margin_description",
                 default=u"Space between viewport and FancyBox wrapper")

opacity_description = _(u"opacity_description",
                 default=u"When true, transparency of content is changed for elastic transitions")


modal_description = _(u"modal_description",
                 default=u"When true, 'overlayShow' is set to 'true' and 'hideOnOverlayClick', 'hideOnContentClick', 'enableEscapeButton', 'showCloseButton' are set to 'false'")

cyclic_description = _(u"cyclic_description",
                 default=u"When true, galleries will be cyclic, allowing you to keep pressing next/back.")

scrolling_description = _(u"scrolling_description",
                 default=u"Set the overflow CSS property to create or hide scrollbars. Can be set to 'auto', 'yes', or 'no'")

autoScale_description = _(u"autoScale_description",
                 default=u"If true, FancyBox is scaled to fit in viewport")

overlayOpacity_description = _(u"overlayOpacity_description",
                 default=u"Opacity of the overlay (from 0 to 1; default - 0.3)")

overlayColor_description = _(u"overlayColor_description",
                 default=u"Color of the overlay")

titleShow_description = _(u"titleShow_description",
                 default=u"Toggle title")

titlePosition_description = _(u"titlePosition_description",
                 default=u"The position of title. Can be set to 'outside', 'inside' or 'over'")

transition_description =_(u"transitionIn_description",
                            default=u"The transition type. Can be set to 'elastic', 'fade' or 'none'")

speed_description = _(u"speed_description",
                 default=u"Speed of the fade and elastic transitions, in milliseconds")

changeSpeed_description = _(u"changeSpeed_description",
                 default=u"Speed of resizing when changing gallery items, in milliseconds")

changeFade_description = _(u"changeFade_description",
                 default=u"Speed of the content fading while changing gallery items")

easing_description = _(u"easing_description",
                 default=u"Easing used for elastic animations")

showCloseButton_description = _(u"_description",
                 default=u"")

showCloseButton_description = _(u"showCloseButton_description",
                 default=u"Toggle close button")
