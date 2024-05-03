import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from news.models import PostCategory, Post

from .tasks import send_email_task


# def send_notifications(preview, pk, headline, subscribers):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=headline,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = cat.subscribers.all()
#             subscribers_emails += [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.headline, subscribers_emails)

# @receiver(pre_save, sender=Post)
# def post_limit(sender, instance, **kwargs):
#     today = datetime.date.today()
#     post_limit = Post.objects.filter(author=instance.author, some_datatime__date=today).count()
#     if post_limit >= 3:
#         raise ValidationError('Нельзя п   убликовать более 3 х постов в сутки')

#При необходимости проверить отсылку сообщений расскоментировать данный сигнал!!!!!
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         send_email_task.delay(instance.pk)
