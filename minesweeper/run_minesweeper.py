#!/usr/bin/env python3
"""启动本地扫雷网页并自动打开浏览器。"""

from __future__ import annotations

import http.server
import os
import socket
import threading
import time
import webbrowser
from pathlib import Path

HOST = "127.0.0.1"
DEFAULT_PORT = 8000


def find_available_port(host: str, preferred: int) -> int:
    """优先使用指定端口，不可用则自动分配可用端口。"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if s.connect_ex((host, preferred)) != 0:
            return preferred

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 0))
        return int(s.getsockname()[1])


def open_browser_later(url: str, delay_seconds: float = 0.8) -> None:
    """延迟打开浏览器，避免服务器尚未监听时打开失败。"""
    time.sleep(delay_seconds)
    ok = webbrowser.open(url)
    if not ok:
        print("[提示] 未能自动唤起浏览器，请手动打开：", url, flush=True)


def main() -> None:
    web_dir = Path(__file__).resolve().parent
    os.chdir(web_dir)

    port = find_available_port(HOST, DEFAULT_PORT)
    url = f"http://{HOST}:{port}/index.html"

    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.ThreadingHTTPServer((HOST, port), handler)

    print(f"扫雷已启动: {url}", flush=True)
    print("按 Ctrl+C 退出。", flush=True)

    opener = threading.Thread(target=open_browser_later, args=(url,), daemon=True)
    opener.start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n正在关闭服务器...", flush=True)
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
