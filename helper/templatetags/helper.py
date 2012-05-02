from django import template

register = template.Library()

'''@register.filter(name='trunc')
def trunc(value, arg):
    return value[:arg] + (value[arg:] and '...')

@register.filter(name='wrap_par')
def wrap_par(value):
    return '(' + str(value) + ')'

@register.inclusion_tag('templatetags/help_text.html')
def help_text():
    return {}

@register.inclusion_tag('templatetags/div_clearfix.html')
def clearfix():
    return {}

@register.inclusion_tag('templatetags/hr_dot.html')
def hr_dot():
    return {}

'''

@register.inclusion_tag('templatetags/js_tag.html')
def js_tag(url):
    return  {'url' : url}

@register.inclusion_tag('templatetags/css_tag.html')
def css_tag(url):
    return  {'url' : url}

@register.inclusion_tag('templatetags/div_link.html')
def div_link(url, value, id=None, clazz=None):
    return  {'url' : url,
             'value' : value,
             'id' : id,
             'clazz' : clazz}

@register.inclusion_tag('templatetags/div_submit.html')
def div_submit(value, id=None, clazz=None):
    return  {'value' : value,
            'submit_id' : id,
            'submit_class' : clazz}

'''
@register.inclusion_tag('templatetags/div_image.html')
def div_image(image_url, image_id=None, image_class=None):
    return  {'image_url' : image_url,
            'image_id' : image_id,
            'image_class' : image_class}

'''
@register.inclusion_tag('templatetags/div_text.html')
def div_text(text, id=None, clazz=None):
    return  {'text' : text,
            'id' : id,
            'clazz' : clazz}
    
'''
@register.inclusion_tag('templatetags/div_abbr.html')
def div_abbr(time, text_id=None, text_class=None):
    return  {'time' : time,
            'text_id' : text_id,
            'text_class' : text_class}
    
@register.inclusion_tag('templatetags/div_label_abbr.html')
def div_label_abbr(time, text_id=None, text_class=None, label_val=None):
    return  {'time' : time,
            'text_id' : text_id,
            'text_class' : text_class,
            'label_val' : label_val,}
    
@register.inclusion_tag('templatetags/div_quote_text.html')
def div_quote_text(text, text_id=None, text_class=None, label_val=None):
    return {'text' : text,
            'text_id' : text_id,
            'text_class' : text_class,
            'label_val' : label_val}

'''
@register.inclusion_tag('templatetags/div_label_text.html')
def div_label_text(text, id=None, clazz=None, value=None):
    return {'text' : text,
            'id' : id,
            'clazz' : clazz,
            'value' : value}


@register.inclusion_tag('templatetags/form_label_text.html')
def form_label_text(object, field_name, label_name, clazz):
    return {'object' : object,
            'field_name' : field_name,
            'label_name' : label_name,
            'clazz' : clazz}
    


    
