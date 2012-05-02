# -*- coding: utf-8 -*-
import urllib
def url_with_querystring(path, dict):
    return path + '?' + urllib.urlencode(dict)

def get_search_message(fields, dict):
    return (u'且'.join((u'%s包含"%s"' % (fields[k].label, dict[k]) for k in dict))).encode('utf-8')