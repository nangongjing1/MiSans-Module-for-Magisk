# MiSans Module for MIUI
本分支旨在使 MIUI12.5 及以下 ROM 使用 MiSans，已在 A10、A11、A12 测试可正常启动。~~已知问题：MIUI 刷入后无法在设置中调整字体粗细。~~(此分支为 MIUI 专用版本，已修复通用版本中存在的这个问题)

> **重要提醒：**
>
> 刷机、刷入 Magisk 模块可能会导致系统无法正常启动，请在操作前审慎考虑，并建议备份重要数据。因操作不当导致的系统故障（包括卡开机动画、功能异常等）或效果异常与模块作者无关。

## 字重测试
[点击此处进入字重测试](https://font.yukonga.top/) （酷安 [@YuKongA / 原名「余空_YuK」](https://www.coolapk.com/u/680367) 制作提供）

## 兼容性提醒
 - 专用版本需要逆向分析各ROM的字体实现以达到最佳效果。
 - 本模块最低支持 Magisk 20.4。
 - MIUI 之外的 ROM 未经测试，真诚地建议使用通用版本。
 - A7以上版本无需修改`/system/etc/fonts.xml`内容，由于A5-A6 的字体配置文件包括`fonts.xml`和`fallback_fonts.xml`，所以二者需要同时修改[具体参照这里](https://www.daogebangong.com/zh/articles/detail/Tutorial%20deeply%20interprets%20the%20Android%20font%20mechanism%20and%20handles%20font%20replacement%20and%20thickness%20classification%20for%20Android%20phones.html)
