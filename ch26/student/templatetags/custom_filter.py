from django import template
register=template.Library()

@register.filter(name='iamtoweare')
def myreplace(value,args):
    return value.replace(args,'We Are')
# register.filter('IamtoWeare',myreplace)