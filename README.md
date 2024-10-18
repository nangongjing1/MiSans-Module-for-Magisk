# MiSans-Module-for-Magisk
本项目旨在使不被支持的AOSP发行版使用MiSans，已在A10、A11、A12测试可正常启动。~~已知问题：MIUI刷入后无法在设置中调整字体粗细。~~(主分支为通用版本，MIUI专用版本已修正此问题)

> **重要提醒：**
>
> 刷机、刷入 Magisk 模块可能会导致系统无法正常启动，请在操作前审慎考虑，并建议备份重要数据。因操作不当导致的系统故障（包括卡开机动画、功能异常等）或效果异常与模块作者无关。

## 字重测试
[点击此处进入字重测试](https://font.yukonga.top/) （酷安 [@YuKongA / 原名「余空_YuK」](https://www.coolapk.com/u/680367) 制作提供）

## 注意事项
1. `/system/fonts` 目录内的 **EmptyFont** 为空字体文件，主要提供度量和字重信息，**请勿轻易删除。**
2. `/system/product` 文件夹内的内容用以覆盖类原生 Android 系统内置的 Google Sans 字体，实现所替换字体在类原生 ROM 上的全局覆盖。若想保留原生 ROM 内置的 Google Sans 字体，请将模块内的 `/system/product` 文件夹删除。
3. `/system/etc/fonts.xml` 为字体配置文件，已经过调整以调用空字体及自定义字体。**理论上**可兼容 Android 12 和 Android 11，**但不保证所有 ROM 均能正常使用**，具体请参阅下面的 **「兼容性调整」** 。A7以上版本无需修改`/system/etc/fonts.xml`内容，由于A5-A6 的字体配置文件包括`fonts.xml`和`fallback_fonts.xml`，所以二者需要同时修改[具体参照这里](https://www.daogebangong.com/zh/articles/detail/Tutorial%20deeply%20interprets%20the%20Android%20font%20mechanism%20and%20handles%20font%20replacement%20and%20thickness%20classification%20for%20Android%20phones.html)。
4. **本模块最低支持 Magisk 20.4。**

## 兼容性调整 <sub>仅供参考</sub>
由于不同OEM对字体的实现方式不同，所以需要对模块内的配置文件进行调整：
- **OPPO/一加 ColorOS：** 将 `/system/etc/fonts.xml` 复制到 `/system/system_ext/etc/` 目录并重命名为 `fonts_base.xml`。
- **一加 HydrogenOS 11 及以上版本：** 将 `/system/etc/fonts.xml` 复制到相同文件夹，并重命名为 `fonts_base.xml。`
- **魅族 Flyme：** 将 `/system/etc/fonts.xml` 复制 3 份到相同文件夹，并重命名为以下 3 个文件： `fonts_flyme.xml`、`fonts_inter.xml` 和 `fonts_slate.xml`。
