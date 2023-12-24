from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__, template_folder='Views')

# Eğitilmiş modeli yükle
model = joblib.load(r"C:\Software\PyCharm\pythonProjects\webFlask\GradientBoostingRegressor_model.pkl")


@app.route('/', methods=['GET', 'POST'])
def index():
    tahmin = None

    if request.method == 'POST':
        # Form verilerini al
        form_verileri = {
            "marka_Nike": [request.form.get("marka_Nike") == "Nike"],
            "marka_Puma": [request.form.get("marka_Puma") == "Puma"],
            "marka_Skechers": [request.form.get("marka_Skechers") == "Skechers"],
            "marka_adidas": [request.form.get("marka_adidas") == "Adidas"],
            "taban_EVA": [request.form.get("taban_EVA") == "EVA"],
            "taban_Kauçuk": [request.form.get("taban_Kauçuk") == "Kauçuk"],
            "taban_Kuaçuk": [request.form.get("taban_Kuaçuk") == "Kuaçuk"],
            "taban_Köpük": [request.form.get("taban_Köpük") == "Köpük"],
            "taban_Poliüretan": [request.form.get("taban_Poliüretan") == "Poliüretan"],
            "taban_Sentetik": [request.form.get("taban_Sentetik") == "Sentetik"],
            "taban_TPU": [request.form.get("taban_TPU") == "TPU"],
            "taban_Tekstil": [request.form.get("taban_Tekstil") == "Tekstil"],
            "taban_Termo": [request.form.get("taban_Termo") == "Termo"],
            "taban_Termoplastik": [request.form.get("taban_Termoplastik") == "Termoplastik"],
            "taban_kauçuk": [request.form.get("taban_kauçuk") == "kauçuk"],

            "dış_materyal_Deri": [request.form.get("dış_materyal_Deri") == "Deri"],
            "dış_materyal_File": [request.form.get("dış_materyal_File") == "File"],
            "dış_materyal_Microfiber": [request.form.get("dış_materyal_Microfiber") == "Microfiber"],
            "dış_materyal_PU": [request.form.get("dış_materyal_PU") == "PU"],
            "dış_materyal_Polyester": [request.form.get("dış_materyal_Polyester") == "Polyester"],
            "dış_materyal_Sentetik": [request.form.get("dış_materyal_Sentetik") == "Sentetik"],
            "dış_materyal_Süet": [request.form.get("dış_materyal_Süet") == "Süet"],
            "dış_materyal_Tekstil": [request.form.get("dış_materyal_Tekstil") == "Tekstil"],
            "dış_materyal_deri": [request.form.get("dış_materyal_Deri") == "Deri"],
            "menşei_Andorra": [request.form.get("menşei_Andorra") == "Andorra"],
            "menşei_Endonezya": [request.form.get("menşei_Endonezya") == "Endonezya"],
            "menşei_Hindistan": [request.form.get("menşei_Hindistan") == "Hindistan"],
            "menşei_Kamboçya": [request.form.get("menşei_Kamboçya") == "Kamboçya"],
            "menşei_Myanmar": [request.form.get("menşei_Myanmar") == "Myanmar"],
            "menşei_Tayvan": [request.form.get("menşei_Tayvan") == "Tayvan"],
            "menşei_Türkiye": [request.form.get("menşei_Türkiye") == "Türkiye"],
            "menşei_Vietnam": [request.form.get("menşei_Vietnam") == "Vietnam"],
            "menşei_Çin": [request.form.get("menşei_Çin") == "Çin"],
            "cinsiyet_erkek": [request.form.get("cinsiyet_Erkek") == "Erkek"],
            "cinsiyet_kadın": [request.form.get("cinsiyet_Kadın") == "Kadın"],
            "tip_ayakkabı": [request.form.get("tip_ayakkabı") == "Ayakkabı"],
            "tip_bot": [request.form.get("tip_bot") == "Bot"]
        }

        # Form verilerinden bir DataFrame oluştur
        girdi_verisi = pd.DataFrame(form_verileri)

        print(girdi_verisi)

        # Tahmin yap
        tahmin = model.predict(girdi_verisi)

    return render_template('index.html', tahmin=tahmin)


if __name__ == '__main__':
    app.run(debug=True)
