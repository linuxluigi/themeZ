from django.db import models
from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


# Standard page

class StandardPage(Page):
    intro = models.CharField(max_length=128)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    api_fields = ['intro', 'body', 'feed_image', 'carousel_items', 'related_links']


StandardPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('body', classname="full"),
]

StandardPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class PageAlias(Page):
    alias_for_page = models.ForeignKey('wagtailcore.Page',
                                       related_name='aliases',
                                       null=True,
                                       on_delete=models.SET_NULL)

    def serve(self, request):
        return redirect(self.alias_for_page.url, permanent=False)


PageAlias.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('alias_for_page', classname="site alias"),
]
