def greet(name: str, lang: str = "en") -> str:
    """返回问候语, 支持中英文"""
    if lang == "zh":
        return f"你好, {name}!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
