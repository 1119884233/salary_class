import requests
import json
import pandas as pd


# 获取用户基本信息
def get_user_info(user_id):
    url = f'https://lf-douyin-pc-web.douyinstatic.com/obj/douyin-pc-web/ies/douyin_web/client-entry~6.a282aae3.js{user_id}/info'  # 假设API URL结构
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        user_info = data.get('user', {})
        if not user_info:
            print(f"没有找到用户 {user_id} 的信息")
        return user_info
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return None
    except json.JSONDecodeError:
        print("JSON解析失败")
        return None


# 获取用户粉丝信息
def get_user_fans(user_id):
    url = f'https://api.douyin.com/user/{user_id}/followers'  # 假设API URL结构
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        fans_list = data.get('followers', [])
        if not fans_list:
            print(f"没有找到用户 {user_id} 的粉丝数据")
        return fans_list
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return []
    except json.JSONDecodeError:
        print("JSON解析失败")
        return []


# 用户数据分析
def analyze_user_data(user_info):
    if not user_info:
        return

    # 将用户信息转为 DataFrame
    df = pd.DataFrame([user_info])  # 因为只有一个用户，所以要放入一个列表

    # 打印用户基本信息
    print("用户基本信息:")
    print(df[['user_id', 'nickname', 'follower_count', 'following_count']])

    # 统计用户的粉丝数和关注数
    print("\n粉丝数统计:")
    print(df['follower_count'].describe())
    print("\n关注数统计:")
    print(df['following_count'].describe())


# 粉丝数据分析
def analyze_user_fans(fans_list):
    if not fans_list:
        return

    # 将粉丝数据转为 DataFrame
    df = pd.DataFrame(fans_list)

    # 统计粉丝的性别分布
    print("\n粉丝性别分布:")
    print(df['gender'].value_counts())

    # 统计粉丝的地区分布
    print("\n粉丝地区分布:")
    print(df['location'].value_counts())


# 主程序
if __name__ == '__main__':
    user_id = '123456'  # 这里是你要查询的用户ID
    user_info = get_user_info(user_id)
    if user_info:
        analyze_user_data(user_info)

    fans_list = get_user_fans(user_id)
    if fans_list:
        analyze_user_fans(fans_list)
