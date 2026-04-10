# dr

Windows-focused helper for installing **oh-my-opencode** from the upstream guide.

- Guide: `docs/oh-my-opencode-windows.md`
- Script: `scripts/install-oh-my-opencode-windows.ps1`

## 经典扫雷（Web）

新增了一个可直接运行的经典扫雷网页版本：

- 入口脚本：`minesweeper/run_minesweeper.py`
- 页面文件：`minesweeper/index.html`

### 运行方式

```bash
python minesweeper/run_minesweeper.py
```

> Windows 下建议优先使用 `python` 或 `py`，不要强依赖 `python3` 命令。

运行后会在终端打印访问地址（例如 `http://127.0.0.1:8000/index.html`），并尝试自动打开浏览器。
如果浏览器没有自动弹出，请手动复制终端里的地址打开。

支持功能：

