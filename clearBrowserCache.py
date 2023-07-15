import os
import platform
import shutil

def clear_browser_cache():
    system = platform.system()
    if system == 'Windows':
        clear_windows_cache()
    elif system == 'Darwin':
        clear_mac_cache()
    elif system == 'Linux':
        clear_linux_cache()
    else:
        print("Unsupported operating system.")

def clear_windows_cache():
    chrome_cache = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'Cache')
    firefox_cache = os.path.join(os.environ['LOCALAPPDATA'], 'Mozilla', 'Firefox', 'Profiles')
    edge_cache = os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Edge', 'User Data', 'Default', 'Cache')
    
    clear_directory(chrome_cache)
    clear_directory(firefox_cache)
    clear_directory(edge_cache)

def clear_mac_cache():
    chrome_cache = os.path.join(os.path.expanduser("~"), 'Library', 'Caches', 'Google', 'Chrome', 'Default', 'Cache')
    firefox_cache = os.path.join(os.path.expanduser("~"), 'Library', 'Caches', 'Firefox', 'Profiles')
    edge_cache = os.path.join(os.path.expanduser("~"), 'Library', 'Caches', 'Microsoft', 'Edge', 'Default', 'Cache')
    
    clear_directory(chrome_cache)
    clear_directory(firefox_cache)
    clear_directory(edge_cache)

def clear_linux_cache():
    chrome_cache = os.path.join(os.path.expanduser("~"), '.cache', 'google-chrome', 'Default', 'Cache')
    firefox_cache = os.path.join(os.path.expanduser("~"), '.cache', 'mozilla', 'firefox')
    edge_cache = os.path.join(os.path.expanduser("~"), '.cache', 'microsoftedge', 'Default', 'Cache')
    
    clear_directory(chrome_cache)
    clear_directory(firefox_cache)
    clear_directory(edge_cache)

def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Cleared cache: {directory}")
    else:
        print(f"Cache directory not found: {directory}")

if __name__ == '__main__':
    clear_browser_cache()
