from googletrans import Translator
text="Hi, how are you doing today?"
translator=Translator()
translated=translator.translate(text,src='en',dest='ta')
print("Tamil Translation:",translated.text)
