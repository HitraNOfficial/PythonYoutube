import pyttsx3
import PyPDF2
import json
import time

book = open('Meditations Marcus Aurelius.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

preferences = json.load(open('shared_preferences.json'))

oldtime = time.time()

speaker = pyttsx3.init()
speaker.setProperty('rate', 170)

for num in range(preferences['currentPage'], pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

    if time.time() - oldtime >= preferences['sleep'] * 60:
        preferences['currentPage'] = num + 1

        j = json.dumps(preferences)
        with open('shared_preferences.json', 'w') as f:
            f.write(j)
            f.close()
        
        break
