from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translator = MyMemoryTranslator(source='english', target='french')
    frenchText = translator.translate(englishText)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translator = MyMemoryTranslator(source='french', target='english')
    englishText = translator.translate(frenchText)
    return englishText
    
@app.route("/")
def renderIndexPage():
     return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
