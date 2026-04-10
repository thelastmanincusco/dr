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
python3 minesweeper/run_minesweeper.py
```

运行后会自动打开浏览器并进入扫雷页面，支持：

- 右键插旗
- 左键点击数字格时，如果已标记雷数满足数字，会自动展开周围非雷格
- 「自动标雷」开关：开启后会自动标记无需推理即可确定的雷
