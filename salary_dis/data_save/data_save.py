
#二进制流的保存
def save_content(file_name,content):
    try:
        with open(file_name,"wb") as f:
            f.write(content)
    except:
        print("二进制流保存错误")