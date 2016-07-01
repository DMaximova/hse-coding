
def mentions():
    allnames = getNames()
    surname_init = '[А-ЯЁ]\. ([А-ЯЁ][а-яё]+)'
    surname_full = '[А-ЯЁ]\.[А-ЯЁ]\. ([А-ЯЁ][а-яё]+)'
    surname_reverse = '([А-ЯЁ][а-яё]+ )[А-ЯЁ]\.(?:[А-ЯЁ]\.)'
    for name in names:
        res = re.search(surname_init, name)
        if res:
            f = open('Михайловский_замок.html', 'r', encoding='utf-8')
            for lines in f.readlines():
                res.group(1)
        
