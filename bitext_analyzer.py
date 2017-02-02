''' Search a bilingual corpus for lines where both user-selected terms appear
and create a new document composed only of those lines'''

import re
import codecs

# Get bitext file to analyze
input_file = codecs.open(input('Enter filename: '), 'r', encoding='UTF-8')

# Set first language in bt file and search term
first_lang = input('Enter first language: ')
first_word = input('Enter first word: ')
first_letter = first_word[0].upper()+first_word[0].lower()
fw_alt_endings = input('Allow alternate endings? (y/n) ')
if fw_alt_endings == 'y' :
    fw_alt_endings = ''
else :
    fw_alt_endings = '[\W\s]'
first_word = '[^A-Za-z]['+first_letter+']'+first_word[1:]+fw_alt_endings

# Set second language in bt file and search term
second_lang = input('Enter second language: ')
second_word = input('Enter second word: ')
second_letter = second_word[0].upper()+second_word[0].lower()
sw_alt_endings = input('Allow alternate endings? (y/n) ')
if sw_alt_endings == 'y' :
    sw_alt_endings = ''
else :
    sw_alt_endings = '[\W\s]'
second_word = '[^A-Za-z]['+second_letter+']'+second_word[1:]+sw_alt_endings

lines_searched = 0
count = 0

print('Scanning text...')

# make list w/ all possible instances of translation
# still need to check if the presence of the words is due to a translation
# or is just a coincidence
# original file does not include information re: which sentence(fragment) is original and which is translated
lines_by_lang = list()
for line in input_file:
    lines_searched += 1
    if re.search(first_word, line): # if one of the search words in a line, we check the line
        split_line = re.split(r'\t+', line) # split line at the tab so we can check each translation independently—important if a word is used in both languages, like 'actual' in EN/ES/FR
        if re.search(first_word, split_line[0]) and \
           re.search(second_word, split_line[1]): # do a closer examination to see if there might be a translation in the sentence pair
            lines_by_lang.append({'line_nr': lines_searched, first_lang: split_line[0], second_lang: split_line[1]})
            count += 1

for i in lines_by_lang:
    print('%s: %s' % (first_lang, i[first_lang]))
    print('%s: %s' % (second_lang, i[second_lang]))
    print()

print('Lines searched: ' + str(lines_searched))
print('Potential issues found: ' + str(count))