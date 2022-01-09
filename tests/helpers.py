from urllib.parse import urlencode

from django.urls import reverse as django_reverse


def reverse(*args, query_params=None, **kwargs):
    """
    django's reverse, but with support for query params
    :param args:
    :param query_params:
    :param kwargs:
    :return:
    """
    url = django_reverse(*args, **kwargs)

    if query_params:
        return f"{url}?{urlencode(query_params)}"
    return url


def assert_dict_in(needles, haystack):
    for k, v in needles.items():
        assert k in haystack
        assert haystack[k] == v
