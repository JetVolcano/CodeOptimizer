def optimize_code(file_path: str):
    try:
        def get_type(type):
            if type == 'py':
                return 'python'
            elif type == 'js':
                return 'javascript'
            elif type == 'ts':
                type = 'typescript'
            elif type == 'cpp':
                type = 'c++'
            return type
        from google import genai
        client = genai.Client(api_key='')
        file = open(file_path, 'r+')
        response = client.models.generate_content(
            model="gemini-2.5-pro-exp-03-25",
            contents = [f'optimize my code and output raw code', file.read()]
        )
        filetype = file.name.split('.')[-1]
        filetype = get_type(filetype)
        code = response.text.split(f'```')[1].split('```')[0].split(filetype)[1].strip()
        file.writelines(["\n", "\n", code])
    except Exception as e:
        print(e)