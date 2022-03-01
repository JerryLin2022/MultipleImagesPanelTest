from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.blocks import URLBlock
from wagtail.core.fields import StreamField

from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail_multi_upload.edit_handlers import MultipleImagesPanel
from django.utils.translation import gettext_lazy as _


class InlineVideoBlock(blocks.StructBlock):
    caption = blocks.CharBlock(required=True, label=_("Video Caption"), max_length=64)
    url = URLBlock(required=True, label=_("Video URL"), max_length=256)
    cover = ImageChooserBlock(label="Video Cover", required=True)
    intro = blocks.CharBlock(required=False, label=_("Video Intro"), max_length=128)

    class Meta:
        icon = 'media'


class HomePage(Page):
    stream_body = StreamField([
        ('video', InlineVideoBlock(label="Video Stream Body")),
    ], verbose_name="Video Stream Body", blank=True)

    content_panels = Page.content_panels + [
        MultipleImagesPanel("gallery_images", label="Image Set", image_field_name="image"),
        StreamFieldPanel('stream_body'),
    ]


class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
