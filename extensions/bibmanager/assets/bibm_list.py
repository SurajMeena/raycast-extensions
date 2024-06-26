import bibmanager.bib_manager as bibm
import bibmanager.utils as u
import json
import sys

def get_keywords(bib):
    fields = u.get_fields(bib.content)
    key = next(fields)
    for k,v,n in fields:
        if k == "keywords":
            return v.replace(', ',',').split(',')
    return []

if __name__ == "__main__":
    bibs = bibm.load()
    output = {'items':[]}

    for bib in bibs:
        dict_of_bib = {'title':bib.title,
                       'uid':bib.key,
                       'link': bib.adsurl,
                       'year': bib.year,
                       'month': bib.month,
                       'keywords': get_keywords(bib),
                       'authors_tag': [u.purify(author.last) for author in bib.authors],
                       'authors_string': u.get_authors(bib.authors),
                       'tags': bib.tags,
                       'adscode': bib.bibcode,
                       'content': bib.content}
        if bib.pdf is not None:
            dict_of_bib['pdf'] = u.BM_PDF() + bib.pdf

        output['items'].append(dict_of_bib)

    json_dump = json.dumps(output)

    sys.stdout.write(json_dump)
    sys.stdout.flush()

