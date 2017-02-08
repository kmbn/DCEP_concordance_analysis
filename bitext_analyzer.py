''' Search a bilingual corpus for lines where both user-selected terms appear
and create a new document composed only of those lines'''

import re
import codecs
import json

'''
1. a function to estimate how many fragments might have relevant data and to optionally save those data to disk for later use
2. a function to view and evaluate the relevant fragments and mark them as relevant or irrelevant (and save that data)
3. a function to view and comment on the fragments that are relevant
4. a function to search for those fragments in context to determin which was source and which was translation
'''

def create_concordance():
    params = get_params()
    print('Scanning text...')
    results = search_for_matches(params)
    filename = save_results(params, results)
    print('Lines searched: %s' % (results['lines_searched']))
    print('Possible matches: %s' % (results['poss_matches']))
    print('File saved as: %s' % filename)


def get_params():
    # Get bitext file to analyze
    input_file = input('Enter filename: ')
    # Set first language in bt file and search term
    first_lang = input('Enter first language: ')
    first_word = input('Enter first word: ')
    first_alt_endings = input('Allow alternate endings? (y/n) ')
    first_regex = create_regex(first_word, first_alt_endings)
    # Set second language in bt file and search term
    second_lang = input('Enter second language: ')
    second_word = input('Enter second word: ')
    second_alt_endings = input('Allow alternate endings? (y/n) ')
    second_regex = create_regex(second_word, second_alt_endings)
    lang_pair = str(first_lang + '_' + second_lang)
    word_pair = str(first_word + '_' + second_word)
    params = {'input_file': input_file, 'first_lang': first_lang, 'first_word': first_word, 'first_alt_endings': first_alt_endings, 'first_regex': first_regex, 'second_lang': second_lang, 'second_word': second_word, 'second_alt_endings': second_alt_endings, 'second_regex': second_regex, 'lang_pair': lang_pair, 'word_pair': word_pair}
    return params


def create_regex(word, alt_endings):
    regex_begin = word[0].upper()+word[0].lower()
    if alt_endings == 'y' :
        regex_end = ''
    else :
        regex_end = '[\W\s]'
    regex = '[^A-Za-z]['+regex_begin+']'+word[1:]+regex_end
    return regex


def search_for_matches(params):
    f = codecs.open(params['input_file'], 'r', encoding='UTF-8')
    fre = params['first_regex']
    sre = params['second_regex']
    lines_searched = 0
    poss_matches = 0
    poss_lines = list()
    for line in f:
        lines_searched += 1
        if re.search(fre, line): # if one of the search words in a line, we check the line
            split_line = re.split(r'\t+', line) # split line at the tab so we can check each translation independently—important if a word is used in both languages, like 'actual' in EN/ES/FR
            if re.search(fre, split_line[0]) and \
               re.search(sre, split_line[1]): # do a closer examination to see if there might be a translation in the sentence pair
                poss_matches += 1
                poss_lines.append({'line_nr': lines_searched, \
                                 params['first_lang']:split_line[0], \
                                 params['second_lang']: split_line[1]})
    results = {'lines_searched': lines_searched, 'poss_matches': poss_matches, 'poss_lines': poss_lines}
    return results


def save_results(params, results):
    filename = str('concordance_' + params['lang_pair'] + '_' + params['word_pair'] + '.json')
    session = {'params': params, 'results': results}
    with open(filename, 'w') as f:
        json.dump(session, f)
    return filename


create_concordance()