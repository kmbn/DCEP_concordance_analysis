''' Search a bilingual corpus for lines where both user-selected terms appear
and create a new document composed only of those lines'''

import re
import codecs


input_file = codecs.open(input('Enter filename: '), 'r', encoding='UTF-8')

first_word = input('Enter first word: ')
first_letter = first_word[0].upper()+first_word[0].lower()
fw_alt_endings = input('Allow alternate endings? (y/n) ')
if fw_alt_endings == 'y' :
    fw_alt_endings = ''
else :
    fw_alt_endings = '[\W\s]'
first_word = '[^A-Za-z]['+first_letter+']'+first_word[1:]+fw_alt_endings

second_word = input('Enter second word: ')
second_letter = second_word[0].upper()+second_word[0].lower()
sw_alt_endings = input('Allow alternate endings? (y/n) ')
if sw_alt_endings == 'y' :
    sw_alt_endings = ''
else :
    sw_alt_endings = '[\W\s]'
second_word = '[^A-Za-z]['+second_letter+']'+second_word[1:]+sw_alt_endings

filename = 'test_results.txt'
count = 0
output = codecs.open(filename, 'w', 'UTF-8')

print('Scanning text...')

for line in input_file :
    if re.search(first_word, line) :
        if re.search(second_word, line) :
            output.write('%s\n' % line)
            count += 1
output.close()

print('Potential issues found: ' + str(count))
print('Issues saved in: ' + filename)