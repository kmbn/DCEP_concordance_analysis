import re
import codecs
import json


def grade_concordance():
    concordance = load_concordance()
    print()
    settings = get_settings(concordance)
    print()
    results = grade(concordance, settings)
    filename = save_results(concordance, results)
    print()
    print('Grading completed.')
    print('%s translations found' % (results['trans_count']))
    print('%s false positives found' % (results['false_count']))
    print()
    print('Results saved in %s' % (filename))


def load_concordance():
    file = input('Enter filename: ')
    while True:
        try:
            open(file, 'r')
            break
        except IOError:
            error = 'No such file.'
            print(error)
    with open(file, 'r', encoding='UTF-8') as f:
        concordance = json.load(f)
    return concordance


def get_settings(concordance):
    setup = ('Concordance of %s(%s) and %s(%s).' % \
        (concordance['params']['first_word'], \
        concordance['params']['first_lang'], \
        concordance['params']['second_word'], \
        concordance['params']['second_lang']))
    print(setup)
    print()
    settings = input('Return only general context? (y/n) ')
    return settings


def grade(concordance, settings):
    translations = list()
    false_positives = list()
    trans_count = 0
    false_count = 0
    grade_count = 0
    for i in concordance['results']['poss_lines']:
        split_line = re.split(r'\t+', i)
        grade_count += 1
        print()
        print('Grading %s of %s:' % (grade_count, \
            concordance['results']['poss_matches']))
        print()
        if settings == 'n':
            print(split_line[3])
            print()
            print(split_line[5].rstrip('\n'))
            print()
        elif settings == 'y':
            ind = re.search(concordance['params']['first_regex'], split_line[3]).start()
            if ind < 40:
                ind = 40
            print(split_line[3][ind-40:ind+40])
            print()
            ind = re.search(concordance['params']['first_regex'], split_line[5]).start()
            if ind < 40:
                ind = 40
            print(split_line[5][ind-40:ind+40])
            print()
        answer = input('Is %s a translation of %s (or vice versa)? (y/n/u) ' % \
            (concordance['params']['first_word'], \
            concordance['params']['second_word']))
        if answer == 'y':
            translations.append(i)
            trans_count += 1
        elif answer == 'n':
            false_positives.append(i)
            false_count += 1
        elif answer == 'u':
            print()
            print(split_line[3])
            print()
            print(split_line[5])
            print()
            answer = input('Is %s a translation of %s (or vice versa)? (y/n/u) ' % \
            (concordance['params']['first_word'], \
            concordance['params']['second_word']))
            if answer == 'y':
                translations.append(i)
                trans_count += 1
            if answer == 'n':
                false_positives.append(i)
                false_count += 1
    results = {'false_count': false_count, 'trans_count': trans_count, \
        'translations': translations, 'false_positives': false_positives}
    return results

def save_results(concordance, results):
    filename = str('graded_concordance_' + concordance['params']['lang_pair'] \
        + '_' + concordance['params']['word_pair'] + '.json')
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(results, f)
    return filename


grade_concordance()