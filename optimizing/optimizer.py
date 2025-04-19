import json
from google import genai

def optimize(file_path: str, key: str):
    with open(file_path, encoding="r+") as file:
        with open('langs.json', encoding="r") as langs:
            keys: dict[str, str] = json.load(langs)[keys]
            def get_lang(lang: str):
                lang = lang.casefold()
                return keys[lang]
            
            client = genai.Client(api_key=key)
            response = client.models.generate_content(
                model="gemini-2.5-pro-exp-03-25",
                contents = ['optimize my code and output raw code', file.read()]
            )
            filetype = file.name.split('.')[-1]
            filetype = get_lang(filetype)
            code = response.text.split('```')[1].split('```')[0].split(filetype)[1].strip()
            file.writelines(["\n", "\n", code])