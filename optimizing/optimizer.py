def optimize(file_path: str, key: str):
    try:
        def get_lang(type: str):
            type_lower = type.lower()
            if type_lower == 'py':
                type = 'python'
            elif type_lower == 'js':
                type = 'javascript'
            elif type_lower == 'ts':
                type = 'typescript'
            elif type_lower == 'cpp':
                type = 'c++'
            elif type_lower == 'c':
                type = 'c'
            elif type_lower == 'h':
                type = 'c/c++ header'
            elif type_lower == 'cs':
                type = 'c#'
            elif type_lower == 'java':
                type = 'java'
            elif type_lower == 'html':
                type = 'html'
            elif type_lower == 'css':
                type = 'css'
            elif type_lower == 'json':
                type = 'json'
            elif type_lower == 'xml':
                type = 'xml'
            elif type_lower == 'rb':
                type = 'ruby'
            elif type_lower == 'php':
                type = 'php'
            elif type_lower == 'go':
                type = 'go'
            elif type_lower == 'swift':
                type = 'swift'
            elif type_lower == 'kt':
                type = 'kotlin'
            elif type_lower == 'rs':
                type = 'rust'
            elif type_lower == 'md':
                type = 'markdown'
            elif type_lower in ['yaml', 'yml']:
                type = 'yaml'
            elif type_lower == 'sql':
                type = 'sql'
            elif type_lower == 'sh':
                type = 'shell script'
            elif type_lower == 'bat':
                type = 'batch script'
            elif type_lower == 'txt':
                type = 'text'
            return type
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
    except Exception as e:
        print(e)