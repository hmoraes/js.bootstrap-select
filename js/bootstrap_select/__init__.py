from fanstatic import Library, Resource, Group
from js.jquery import jquery
from js.bootstrap import bootstrap_js, bootstrap_css

library = Library('bootstrap_select', 'resources')

bootstrap_select_css = Resource(
    library, 'css/bootstrap-select.css',
    minified='css/bootstrap-select.min.css',
    depends=[bootstrap_css,])

bootstrap_select_js = Resource(
    library, 'js/bootstrap-select.js',
    minified='js/bootstrap-select.min.js',
    bottom=True,
    depends=[bootstrap_js, jquery,])

bootstrap_select = Group([bootstrap_select_css, bootstrap_select_js])

ALL_LANGS = ['ar_AR', 'bg_BG', 'cro_CRO',
             'cs_CZ', 'da_DK', 'de_DE',
             'en_US', 'es_CL', 'es_ES',
             'eu'   , 'fa_IR', 'fi_FI',
             'fr_FR', 'hu_HU', 'id_ID',
             'it_IT', 'ko_KR', 'lt_LT',
             'nb_NO', 'nl_NL', 'pl_PL',
             'pt_BR', 'pt_PT', 'ro_RO',
             'ru_RU', 'sk_SK', 'sl_SI',
             'sv_SE', 'tr_TR', 'ua_UA',
             'zh_CN', 'zh_TW', ]


def bootstrap_select_i18n_js(lang=None):
    if lang in ALL_LANGS:
        return Resource(
            library, 'js/i18n/defaults-%s.js' % lang,
            minified='js/i18n/defaults-%s.min.js' % lang,
            depends=[bootstrap_select_js,])
    else:
        all_langs = [
            Resource(
                library, 'js/i18n/defaults-%s.js' % l,
                minified='js/i18n/defaults-%s.min.js' % l,
                depends=[bootstrap_select_js, ]) for l in ALL_LANGS
        ]
        return Group(all_langs)


bootstrap_select_i18n_all_js = bootstrap_select_i18n_js()