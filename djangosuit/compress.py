from pprint import pprint

def post_less_compile(sender, **kwargs):
    """
    Post compress signal handler. Signal is connected in urls.py file
    Overrides suit/static/css/suit.css with compiled css file
    """
    pprint(kwargs.get('type', 'NOOO'))
    pprint(kwargs.get('mode', 'NOOO'))
    context = kwargs.get('context', None)
    if context and 'compressed' in context:
        pprint(context['compressed'])

        # pprint(context.get('compressed', 'NOOO'))
        # if isinstance(sender, CssCompressor):
        # print(kwargs['sender'])
        # print(kwargs['mode'])
        # print(kwargs['type'])
        # print(kwargs['context'])
        #     print(kwargs)
