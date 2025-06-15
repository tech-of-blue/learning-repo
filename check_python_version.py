import sys
import platform

def check_python_version():
    """
    Pythonのバージョン情報を表示する関数
    
    Returns:
        None
    """
    print("=== sysモジュールを使用 ===")
    print(f"sys.version: {sys.version}")
    print(f"sys.version_info: {sys.version_info}")
    
    print("\n=== platformモジュールを使用 ===")
    print(f"platform.python_version(): {platform.python_version()}")

if __name__ == "__main__":
    check_python_version() 