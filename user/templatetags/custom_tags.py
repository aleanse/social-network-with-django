from django import template

register = template.Library()

@register.simple_tag
def user_has_liked(post, user):
    return post.user_has_liked(user)