from bottle import get, run, error, request, abort
import random
import linecache

def getNumberOfLinesInFile(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getRandomWord():
	numLines = getNumberOfLinesInFile('words_list.txt')
	lineNum = random.randrange(numLines)
	word = linecache.getline('words_list.txt', lineNum).strip()
	return word

def applyCasing(word, casing):
	if casing == 'LowerCase':
		return word.lower()
	elif casing == 'UpperCase':
		return word.upper()
	else:
		return word.capitalize()

def generatePassword(num_words, separator, casing):
	word = getRandomWord()
	password = applyCasing(word, casing)
	for i in range(num_words - 1):
		word = getRandomWord()
		password += separator + applyCasing(word, casing)
	return password

@get('/GeneratePassword')
@get('/GeneratePassword/<casing:re:(Capitalize|UpperCase|LowerCase)>') # check the re
def generatePasswordRoute(casing='LowerCase'):
	# Get the number of words.
	numWords = request.query.words or 4;
	try:
		numWords = int(numWords)
	except ValueError:
		abort(400, 'Invalid value for "words" in query string.')
	if numWords < 1:
		abort(400, 'Invalid value for "words" in query string.')

	# Get the seperator character.
	asciiSeparator = request.query.separator;

	if not asciiSeparator:
		separator = ' '
	else:
		try:
			asciiSeparator = int(asciiSeparator)
		except ValueError:
			abort(400, 'Invalid value for "separator" in query string.')
		try:
			separator = chr(asciiSeparator)
		except ValueError:
			abort(400, 'Invalid value for "separator" in query string.')

	# Generate the password.
	password = generatePassword(numWords, separator, casing)

	return password

run(host='localhost', port=8080, debug=True)