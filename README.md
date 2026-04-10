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

- 顶部可切换扫雷规模（初级/中级/高级/地狱200雷）
- 右键插旗，双击已打开数字格且“已标雷数=数字”时可快速展开周围未打开格
- 单击按住数字格时，周围未打开格会出现“预按下”视觉效果
- 「自动标雷」开关：自动标记无需推理即可确定的雷
- 「终局无猜」开关：终局会按已开数字约束重建雷分布，尽量避免二选一/四选二纯猜失败
