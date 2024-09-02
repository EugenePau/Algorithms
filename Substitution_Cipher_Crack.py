import re

alphabet = '''
abcde
fghij
klmno
pqrst
uvwxyz'''

ciphertext = '''livitcswpiyvewhevsriqmxleyveoiewhrxexipfemvewhkvstylxzixlikiixpijvsze
yperrgerimwqlmglmxqeriwgpsrihmxqerekietxmjtprgevekeitrewhexxlexxmzitwawsqwxswextvepmr
xrsjgstvrieyviexcvmuimwergmiwxmjmgcsmwxsjomiqxliviqivixqsvstwhkpegarcsxrwievswiibxviz
mxfsjxlikegaewhepswyswiwievxlisxlivxlirgepirqiviibgiihmwypflevhewhypsrrfqmxleppxliecc
ievewgisjktvwmrlihysphxliqimylxsjxlimwrigxqeroivfvizevaekpiewhxeamwyeppxlmwyrmwxsgswr
mhivexmswmgstphlevhpfkpezintcmxivjsvlmrscmwmswvircigxmwymx'''


key = '''
ekghi
jylmn
apzws
c.vrx
toqbfu'''

letter_list = alphabet + alphabet.upper()

## decipher

print('Deciphering...','\n')

decipher =''
progress_point = 0

for letter in ciphertext:
    if letter in key:
        decipher += alphabet[key.find(letter)]
        progress_point += 1
    else:
        decipher += letter.upper()

completion = progress_point / len(ciphertext) *100

print(decipher,'\n')
print(f'Decipher Completion: {completion}% \n')


## frequencies of a,e,i,o,u

print('Alphabetic Frequency Analysis:')

record = dict()

for letter in letter_list:
    freq = decipher.count(letter)
    record[letter] = freq

res = {key: val for key, val in sorted(record.items(), key = lambda ele: ele[1], reverse = True)}

for item in res.items():
    print(item)

## compile cipher for 'the', then search for freqeuncies > 0 from text

print('Three-letter Set Frequency Analysis:')


testing_counter = 0

target = 'the'
for i in letter_list:
    for j in letter_list:
        for k in letter_list:
            candidate = i+j+k
            freq = decipher.count(candidate)
            if freq >= 3:
                print(candidate,freq)

## compile cipher for 'the', then search for freqeuncies > 0 from text

print('Four-letter Set Frequency Analysis:')


testing_counter = 0

target = 'that'
for i in letter_list:
    for j in letter_list:
        for k in letter_list:
            for m in letter_list:
                candidate = i+j+k+m
                freq = decipher.count(candidate)
                if freq >= 3:
                    print(candidate,freq)




        
                    

## search
