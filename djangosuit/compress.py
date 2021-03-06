from os.path import abspath
from shutil import copyfile
from djangosuit.settings import ENV_ROOT, PROJECT_ROOT


def post_less_compile(sender, **kwargs):
    """
    Post compress signal handler. Signal is connected in urls.py file
    Overrides suit/static/css/suit.css with compiled css file
    """
    type = kwargs.get('type', None)
    context = kwargs.get('context', None)
    if not context:
        return

    compressed = context.get('compressed', None)
    if compressed and type == 'css':
        css_file = abspath(ENV_ROOT + compressed['url'])
        target_file = abspath(
            PROJECT_ROOT + '/suit/suit/static/suit/css/suit.css')
        copyfile(css_file, target_file)
