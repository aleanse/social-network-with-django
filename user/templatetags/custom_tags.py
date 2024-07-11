from django import template

register = template.Library()

@register.simple_tag
def user_has_liked(post, user):
    return post.user_has_liked(user)

@register.simple_tag
def user_is_following(current_user, other_user):
    return current_user.is_following(other_user)