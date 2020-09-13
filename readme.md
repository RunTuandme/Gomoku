![](https://img.shields.io/badge/build-passing-brightgreen)
![](https://img.shields.io/badge/version-0.0.1-green)
![](https://img.shields.io/badge/lang-python-blue)


# 五子棋
---

一个简易的五子棋界面和引擎的实现，搜索算法为alpha-beta剪枝算法 
<img src='./picture/man.ico' width='4%'>

---

## 界面
<img src='./picture/boardshow.png' width='50%'>

---------------
## 文档结构

```
├── Gomuku
│  ├── picture
│  ├── support              ：辅助脚本
│  │  ├── buildcor_grid.py  ：生成棋盘网格
│  │  └── test.txt
│  ├── ABengine.py          ：αβ剪枝算法引擎
│  ├── easyengine.py        ：随机走子引擎（测试）
├──└── windows.py           ：界面
```

---------------

# To Do list
+ 极大极小搜索 <img src='./picture/completed.ico' width='4%'>
+ ab算法 <img src='./picture/completed.ico' width='4%'>
+ bug：解决局面胜利后（电脑）继续走棋的问题
+ bug：点击电脑执黑/白后取消引擎
+ bug：ab算法搜索反向