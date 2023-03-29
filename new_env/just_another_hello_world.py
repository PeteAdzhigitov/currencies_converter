from gtts import gTTS
import pypdf

def extract_text_out_of_pdf(path):
    reader = pypdf.PdfReader(path)
    range_of_pages = len(reader.pages)
    text = []
    for i in range(range_of_pages):
        text.append(reader.pages[i].extract_text())
    return ''.join(text)

def convert_text_to_mp3(text, lang):
    tts = gTTS(text, lang=f'{lang}')
    tts.save('resultingfile.mp3')

def main():
    path = ('/Users/petradzigitov/PycharmProjects/currencies_converter/new_env/'
              'IOC recommends Russian and Belarusian individual athletes compete as neutrals.pdf')
    print('Process has been started')
    text = extract_text_out_of_pdf(path)
    convert_text_to_mp3(text,'en')
    print('Done')

if __name__ == '__main__':
    main()

#just some comment line here