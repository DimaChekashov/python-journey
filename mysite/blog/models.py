from django.db import models
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
    
    subpage_types = ['blog.BlogPage']

class BlogPage(Page):
    date = models.DateField("Дата публикации")
    intro = models.CharField("Краткое описание", max_length=250)
    body = RichTextField(blank=True)

    parent_page_types = ['blog.BlogIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]