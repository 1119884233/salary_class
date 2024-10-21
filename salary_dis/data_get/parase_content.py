import re

def parse_html(regular, content):
    try:
        pattern = re.compile(regular, re.S)
        return re.findall(pattern, content)
    except re.error as e:
        print(f"正则表达式错误: {e}")
        return []