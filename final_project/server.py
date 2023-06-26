from machinetranslation import translator
from flask import Flask, render_template, request
import json
from deep_translator import MyMemoryTranslator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext = MyMemoryTranslator("en", 'fr').translate(textToTranslate)
    return frenchtext
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishtext = MyMemoryTranslator("fr","en").translate(textToTranslate)
    return englishtext
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
