site_presets = [
    {
        'source': 'Ведомости Бизнес',
        'url': 'https://www.vedomosti.ru/rubrics/business/',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   8,
        'filter_pattern': r'https://www\.vedomosti\.ru/business(/.*)?',
        'update_frequency': '7-15'
    },
    {
        'source': 'Ведомости Экономика',
        'url': 'https://www.vedomosti.ru/rubrics/economics/',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   8,
        'filter_pattern': r'https://www\.vedomosti\.ru/economics(/.*)?',
        'update_frequency': '7-15'
    },
    {
        'source': 'Ведомости Финансы',
        'url': 'https://www.vedomosti.ru/rubrics/finance',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   8,
        'filter_pattern': r'https://www\.vedomosti\.ru/finance(/.*)?',
        'update_frequency': '7-15'
    },
    {
        'source': 'Ведомости Инвестиции',
        'url': 'https://www.vedomosti.ru/rubrics/investments',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   8,
        'filter_pattern': r'https://www\.vedomosti\.ru/investments(/.*)?',
        'update_frequency': '20-40'
    },
    {
        'source': 'Ведомости Капитал',
        'url': 'https://www.vedomosti.ru/kapital',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   8,
        'filter_pattern': r'https://www\.vedomosti\.ru/kapital(/.*)?',
        'update_frequency': '20-40'
    },
    {
        'source': 'Ведомости Промышленность',
        'url': 'https://www.vedomosti.ru/industry',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   8,
        'filter_pattern': r'https://www\.vedomosti\.ru/industry(/.*)?',
        'update_frequency': '20-40'
    },
    {
        'source': 'Интерфакс Бизнес',
        'url': 'https://www.interfax.ru/business/',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   4,
        'filter_pattern': r'https://www\.interfax\.ru/.+',
        'update_frequency': '7-15'
    },
    {
        'source': 'BCS Россия',
        'url': 'https://bcs-express.ru/category/rossiyskiy-rynok',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'https://bcs-express.ru/novosti-i-analitika(/.*)?',
        'update_frequency': '20-40'
    },
    {
        'source': 'BCS Валюты',
        'url': 'https://bcs-express.ru/category/valyutnyy-rynok',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'https://bcs-express.ru/novosti-i-analitika(/.*)?',
        'update_frequency': '20-40'
    },
    {
        'source': 'Forbes Бизнес',
        'url': 'https://www.forbes.ru/biznes',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'^https://www\.forbes\.ru/[^/]+/[^/]+(?!.*lnews$)',
        'update_frequency': '20-40'
    },
    {
        'source': 'Forbes Технологии',
        'url': 'https://www.forbes.ru/tekhnologii',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'^https://www\.forbes\.ru/[^/]+/[^/]+(?!.*lnews$)',
        'update_frequency': '20-40'
    },
    {
        'source': 'Forbes Финансы',
        'url': 'https://www.forbes.ru/finansy',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'^https://www\.forbes\.ru/[^/]+/[^/]+(?!.*lnews$)',
        'update_frequency': '20-40'
    },
    {
        'source': 'Forbes Инвестиции',
        'url': 'https://www.forbes.ru/investicii',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'^https://www\.forbes\.ru/[^/]+/[^/]+(?!.*lnews$)',
        'update_frequency': '20-40'
    },
    {
        'source': 'Forbes Компании',
        'url': 'https://www.forbes.ru/novosti-kompaniy',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'^https://www\.forbes\.ru/[^/]+/[^/]+(?!.*lnews$)',
        'update_frequency': '20-40'
    },
    {
        'source': 'РБК Инвестиции',
        'url': 'https://www.quote.ru',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'^https://quote.ru/news/article(/.*)',
        'update_frequency': '20-40'
    },
    {
        'source': 'MFD',
        'url': 'https://mfd.ru/news/',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   3,
        'filter_pattern': r'https://mfd.ru/news/view(/.*)?',
        'update_frequency': '20-40'
    },
    {
        'source': 'Gazeta Business',
        'url': 'https://www.gazeta.ru/business/news/',
        'navigation_steps': [],
        'data_extraction_pattern': {
            'links': {
                'selector': 'a',
                'attributes': ['href', 'innerText']
            }
        },
        'scroll_depth':   7,
        'filter_pattern': r'https://www.gazeta.ru/business/news(/.*)?',
        'update_frequency': '20-40'
    },
    {
    'source': 'КоммерсантЪ Бизнес',
    'url': 'https://www.kommersant.ru/rubric/4',
    'navigation_steps': [],
    'data_extraction_pattern': {
        'links': {
            'selector': 'a',
            'attributes': ['href', 'innerText']
        }
    },
    'scroll_depth':   7,
    'filter_pattern': r'^https://www\.kommersant\.ru/doc/.*(?<!\?from=vertical_lenta)$',
    'update_frequency': '7-15'
    },
    {
    'source': 'КоммерсантЪ Экономика',
    'url': 'https://www.kommersant.ru/rubric/3',
    'navigation_steps': [],
    'data_extraction_pattern': {
        'links': {
            'selector': 'a',
            'attributes': ['href', 'innerText']
        }
    },
    'scroll_depth':   7,
    'filter_pattern': r'^https://www\.kommersant\.ru/doc/.*(?<!\?from=vertical_lenta)$',
    'update_frequency': '7-15'
    },
    {
    'source': 'КоммерсантЪ Финансы',
    'url': 'https://www.kommersant.ru/finance',
    'navigation_steps': [],
    'data_extraction_pattern': {
        'links': {
            'selector': 'a',
            'attributes': ['href', 'innerText']
        }
    },
    'scroll_depth':   7,
    'filter_pattern': r'^https://www\.kommersant\.ru/doc/.*(?<!\?from=vertical_lenta)$',
    'update_frequency': '7-15'
    },
    {
    'source': 'КоммерсантЪ ПотребРынки',
    'url': 'https://www.kommersant.ru/rubric/41',
    'navigation_steps': [],
    'data_extraction_pattern': {
        'links': {
            'selector': 'a',
            'attributes': ['href', 'innerText']
        }
    },
    'scroll_depth':   7,
    'filter_pattern': r'^https://www\.kommersant\.ru/doc/.*(?<!\?from=vertical_lenta)$',
    'update_frequency': '7-15'
    }
    # пресеты сюда
]
