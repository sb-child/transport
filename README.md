# 神圣跨性别帝国护照生成器

![img](example.png)

<sub>对了，我们永远怀念逝去的 [starmoe](https://github.com/Bro-Xun) 姐姐...</sub>

## 准备您的头像

请提前将自己的头像剪切为`4:5`格式，如需上方留有空白请提前预留。

![image](https://user-images.githubusercontent.com/96931510/191689366-ff74e9d0-d097-4eac-a535-7877eb1f93dd.png)

## 安装依赖

```bash
pip3 install pillow qrcode
```

## 生成属于您的护照

```bash
python3 main.py
```

您的护照将会保存在`out.png`中

## todo

+ [x] 自定义头像(直接更改`head.png`) https://github.com/sb-child/transport/pull/1

## license

`main.py` 使用 MIT 协议

`*.ttf`, `*.otf` 归原作者管

`background.png`, `head.png`, `mask.png`, `EXAMPLE_STI.krz` 归原作者管
