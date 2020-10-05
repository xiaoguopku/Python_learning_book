#!/usr/bin/env python
# coding: utf-8

# % # Jupyter notebook 使用指南
# 
# ## Jupyter notebook 快捷键
# 
# 快捷键分为命令模式（Command Mode）和编辑模式(Edit Mode)。
# 
# - 当在**命令模式**的时候，单元格左侧的颜色是**蓝色**的。命令模式操作到对象是单元格（cell）。
# - 当切换到**编辑模式**到时候，单元格左侧的颜色会变成**绿色**。编辑模式操作的是单元格中的文本和代码。
# 
# 
# - 切换到**命令**模式：Esc。
# - 切换到**编辑**模式：Enter。

# ### 共同快捷键
# 
# - 运行本单元，在下方插入一单元：Alt + Enter
# - 运行本单元，选中下一单元：Shift + Enter
# - 运行本单元，选中本单元：Ctrl + Enter
# - 运行单行：无
# - 运行所有单元格：用工具按钮或菜单栏
# - 运行以上单元格：菜单栏：Cell|Run All Above 或 Run All Below
# - 保存：Ctrl + S

# ### 编辑模式快捷键
# 
# - 持续写代码状态
#     - 运行本单元，在下方插入一单元：Alt + Enter （下一单元自动为code 编辑模式）
#     - 转化为Markdown编辑模式：Esc（命令模式）+ M（Markdown命令模式）+ Enter（Markdown编辑模式）
# - 持续运行代码与调试状态
#     - 运行本单元，选中下一单元：Shift + Enter （下一单元自动为命令模式，要想编辑用Enter）
#     - 运行本单元，选中本单元：Ctrl + Enter （本单元自动为命令模式，要想编辑用Enter）
# - 持续编辑内部文本
#     - 跳转
#         - 跳到单元格开头：PgUp
#         - 跳到单元格结尾：PgDn
#         - 跳到本行开头：Alt + Left
#         - 跳到本行结尾：Alt + Right
#         - 跳到左边一个字首：Ctrl + Left
#         - 跳到右边一个字首：Ctrl + Right
#     - 撤销
#         - 撤销：Ctrl + Z
#         - 取消撤销：Ctrl + Shift + Z 或 Ctrl + Y
#     - 代码缩进
#         - 代码补全或缩进：Tab
#         - 提示：Shift + Tab
#         - 缩进：Ctrl + ]
#         - 解除缩进：Ctrl + \[
#     - 注释与撤销注释
#         - Ctrl + /
#     - 块状文本选中
#         - 持续按住Alt + /，同时鼠标拖拽选中文本块

# ### 命令模式快捷键
# 
# - 显示快捷键帮助：H或P
# - Markdown 模式与代码模式转换
#     - 切换到Markdown模式：M
#     - 切换到code模式：Y
#     - 切换到raw模式：R
# - 行号
#     - 显示本单元格行号：L
#     - 显示所有单元格行号：Shift + L
# - 单元格操纵
#     - 在上方插入新单元：A
#     - 在下方插入新单元：B
#     - 复制选中的单元：C
#     - 剪切选中的单元：X
#     - 粘贴到下方单元：V
#     - 粘贴到上方单元：Shift + V
#     - 删除选中的单元：D,D
#     - 恢复删除的最后一个单元：Z
#     - 选中多个单元格：Shift + J 或 Shift + Down 朝下选择cell Shift + K or Shift + Up朝上选择cell 一旦选中多个cell，就可以像对单单一cell一样进行删除/复制/剪切/粘贴/运行了
#     - 合并选中的单元格：Shift + M
#     - 拆分单元格：需在编辑模式下Ctrl + Shift + -，在按光标所在行一分为二，其作为上一单元的结尾
#     - 折叠输出：O
# - 查找替换：F  
# 
# - Markdown标题：仅在 markdown 状态下时建议使用标题相关快捷键，如果单元处于其他状态，则会强制切换到 markdown 状态,针对单元格首行，不针对下方的其他行
#     - 设定 1 级标题：1
#     - 设定 2 级标题：2
#     - 设定 3 级标题：3
#     - 设定 4 级标题：4
#     - 设定 5 级标题：5
#     - 设定 6 级标题：6

# 

# ## Jupyter notebook 拓展
# 

# - 增加目录：Table of Contents(2)
# - 专注模式：zenmode
# - 实时Markdown预览：Live Markdown Preview
# - 代码补全（实时）：Hinterland（不好用）
# - 并排放置单元格：Split Cells Notebook
# - 代码格式整理：Autopep8 或 Code prettify 注意都需要安装对应的库，Code prettify 似乎比Autopep8效果略好。
# - 数据查看：Variable Inspector
# - 命令窗口：scratchpad 
# - 执行时间记录：ExecuteTime
# - 隐藏（指定单元格）代码：Hide input（导出文档时并不会隐藏）
# - 隐藏（所有单元格）代码：Hide input all（导出文档时并不会隐藏）
# - 高亮注释：highlighter（可能导致单元格无法编辑，不好用，未采用）
# - 高亮选中单词：Highlight selected word

# - 代码折叠：Codefolding in Editor
# - 文档折叠：Collapsible Headings
# - 公式增加序号：Equation Auto Numbering
# - 运行结束通知：Notify
# - Markdown中添加行内Python输出：Python Markdown
# - 代码模板：Snippets Menu
# - 文件查找过滤：Tree Filter
# - 代码注释：Comment/Uncomment Hotkey（系统本身有，未使用）
# - 代码运行拓展：Runtools（太复杂，未采用）
# - 限制输出：Limit Output（似乎是限制字数而非行数，没采用）
# - 移动单元格：Move selected cells（未采用）

# ## 结果输出
# 
# 当代码结尾无分号时，结尾处的常量、变量结果可以直接作为输出结果显示，但是各单元格只显示最后的结果。如下面只显示变量b

# In[1]:


a=1
b=2

a
b


# 如果结尾有分号，则结果不显示

# In[2]:


a=1
b=2
c=3

a
b;


# 如果想显示多个变量结果，用`print`函数。`print`函数不受分号影响。

# In[3]:


a=1
b=2

print(a);
print(b);
b


# 如果想在一个cell中输出多行，可以在代码最上方cell添加以下代码

# In[4]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 


# 如果要回复默认，改为如下即可：

# In[5]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "none" 


# 设置所有的Jupyter实例，参考https://blog.csdn.net/enter89/article/details/90633718、https://blog.csdn.net/linecho/article/details/82858728 和 https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
