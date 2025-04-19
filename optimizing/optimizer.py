import json
def optimize(file_path: str, key: str):
    with open(file_path, "r+") as file:
        with open('langs.json') as langs:
            keys: dict[str, str] = json.load(langs)[keys]
            def get_lang(type: str):
                type = type.casefold()
                return keys[type]
            try:
                from google import genai
                client = genai.Client(api_key=key)
                response = client.models.generate_content(
                    model="gemini-2.5-pro-exp-03-25",
                    contents = ['optimize my code and output raw code', file.read()]
                )
                filetype = file.name.split('.')[-1]
                filetype = get_lang(filetype)
                code = response.text.split(f'```')[1].split('```')[0].split(filetype)[1].strip()
                file.writelines(["\n", "\n", code])
            except Exception as error:
                raise error