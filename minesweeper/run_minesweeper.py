#!/usr/bin/env python3
"""启动本地扫雷网页并自动打开浏览器。"""

from __future__ import annotations

import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8000


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main() -> None:
    web_dir = Path(__file__).resolve().parent
    handler = http.server.SimpleHTTPRequestHandler

    # 使用脚本所在目录作为站点根目录
    import os
    os.chdir(web_dir)

    with ReusableTCPServer((HOST, PORT), handler) as server:
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()

        url = f"http://{HOST}:{PORT}/index.html"
        print(f"扫雷已启动: {url}")
        print("按 Ctrl+C 退出。")
        webbrowser.open(url)

        try:
            server_thread.join()
        except KeyboardInterrupt:
            print("\n正在关闭服务器...")
            server.shutdown()


if __name__ == "__main__":
    main()
