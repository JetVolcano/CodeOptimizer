def optimize(file_path: str, key: str):
    try:
        def get_lang(type: str):
            type = type.lower()
            keys: dict[str, str] = {
                'py': 'python',
                'js': 'javascript',
                'ts': 'typescript',
                'cpp': 'c++',
                'c': 'c',
                'h': 'c/c++ header',
                'cs': 'c#',
                'java': 'java',
                'html': 'html',
                'htm': 'html',
                'css': 'css',
                'json': 'json',
                'xml': 'xml',
                'rb': 'ruby',
                'php': 'php',
                'go': 'go',
                'swift': 'swift',
                'kt': 'kotlin',
                'rs': 'rust',
                'md': 'markdown',
                'yaml': 'yaml',
                'yml': 'yaml',
                'sql': 'sql',
                'sh': 'shell script',
                'bat': 'batch script',
                'txt': 'text'
            }
            if type in keys:
                return keys[type]
            else:
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