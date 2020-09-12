<!--
 * @Author: linzuxin
 * @Date: 2020-07-10 00:42:10
 * @LastEditTime: 2020-07-10 00:43:57
 * @LastEditors: Do not edit
 * @Description: 
--> 
# 回溯

> 任何算法的核心都是穷举，回溯算法就是一个暴力穷举算法

## 解题框架

```python
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```