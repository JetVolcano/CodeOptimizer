def optimize(file_path: str, key: str):
    try:
        def get_lang(type: str):
            type = type.casefold()
            from langs import keys
            return keys[type]
        from google import genai
        client = genai.Client(api_key=key)
        file = open(file_path, 'r+')
        response = client.models.generate_content(
            model="gemini-2.5-pro-exp-03-25",
            contents = ['optimize my code and output raw code', file.read()]
        )
        filetype = file.name.split('.')[-1]
        filetype = get_lang(filetype)
        code = response.text.split(f'```')[1].split('```')[0].split(filetype)[1].strip()
        file.writelines(["\n", "\n", code])
        file.close()
    except Exception as error:
        print(error)