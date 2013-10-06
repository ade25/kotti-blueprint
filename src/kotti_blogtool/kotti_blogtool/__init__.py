from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_blogtool')


def kotti_configure(settings):

    settings['kotti.includes'] += ' kotti_blogtool'
    settings['kotti.available_types'] += ' kotti_blogtool.resources.Blog'


def includeme(config):

    config.add_translation_dirs('kotti_blogtool:locale')
    config.scan(__name__)
