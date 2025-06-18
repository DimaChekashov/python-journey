from django.db import models

# Add these:
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):
    intro = RichTextField(
            blank=False,
            null=False,
            verbose_name="Описание",
            help_text="Заполните: описание вакансии, требования и обязанности"
        )

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]