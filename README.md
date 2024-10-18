# MiSans-Module-for-Magisk
本项目旨在使不被支持的MIUI系统使用MiSans，已在A10、A11、A12测试可正常启动。~~已知问题：MIUI刷入后无法在设置中调整字体粗细。~~(主分支为通用版本，MIUI专用版本已修正此问题)

> **重要提醒：**
>
> 刷机、刷入 Magisk 模块可能会导致系统无法正常启动，请在操作前审慎考虑，并建议备份重要数据。因操作不当导致的系统故障（包括卡开机动画、功能异常等）或效果异常与模块模板作者无关。

## 字重测试
[点击此处进入字重测试](https://font.yukonga.top/) （酷安 [@YuKongA / 原名「余空_YuK」](https://www.coolapk.com/u/680367) 制作提供）

## 注意事项
1. `/system/fonts` 目录内的 **EmptyFont** 为空字体文件，为 Android 默认西文字体 Roboto 的掏空字体，主要提供度量和字重信息，**请勿轻易删除。**
2. `/system/product` 文件夹内的内容用以覆盖类原生 Android 系统内置的 Google Sans 字体，实现所替换字体在类原生 ROM 上的全局覆盖。若想保留原生 ROM 内置的 Google Sans 字体，请将模块内的 `/system/product` 文件夹删除。
3. `/system/etc/fonts.xml` 为字体配置文件，已经过调整以调用空字体及自定义字体。**理论上**可兼容 Android 12 和 Android 11，**但不保证所有 ROM 均能正常使用**。不同 ROM 调用字体的配置文件可能不同，请参阅下面的 **「兼容性调整」** 。
4. 添加字体时注意各种语言字体的字重对应。若有些 CJK 字体里既包含中文也包含韩文，则不必加韩文字体。若想使用中文字体自带的西文，则不必加英文字体。
5. **本模块模板最低支持 Magisk 20.4。**
6. ~~在用过 Magisk Hide 或者 Zygisk 之后的 Android 12 系统刷入本字体模块导致被选中的应用闪退，请参考[这里](https://github.com/lxgw/advanced-cjk-font-magisk-module-template/issues/1#issuecomment-1003711583)；如果不想对 system 分区作改动，可改用 [这个](https://github.com/lxgw/cjk-only-font-magisk-module-template/) ，仅替换 CJK 部分字体，保留 Roboto 字体首先调用，防止 Android 12 中 Magisk Hide 或 Zygisk 勾选的应用闪退。~~ Android 12 需要使用 24.0 及以上版本的 Magisk，开启 Zygisk，配合 Shamiko 0.2.0 及以上版本，并在 Magisk 中取消「遵守排除列表」勾选，隐藏 ROOT 同时防止排除列表内的应用闪退。

## 兼容性调整 <sub>仅供参考</sub>
为了使该模块模板更加适合您的手机，需要对模块模板内的配置文件进行调整：
- **OPPO/一加 ColorOS：** 将 `/system/etc/fonts.xml` 复制到 `/system/system_ext/etc/` 目录并重命名为 `fonts_base.xml`。
- **一加 HydrogenOS 11 及以上版本：** 将 `/system/etc/fonts.xml` 复制到相同文件夹，并重命名为 `fonts_base.xml。`
- **魅族 Flyme：** 将 `/system/etc/fonts.xml` 复制 3 份到相同文件夹，并重命名为以下 3 个文件： `fonts_flyme.xml`、`fonts_inter.xml` 和 `fonts_slate.xml`。
- **小米 MIUI 12.5：** 需刷入 [空字体模块](https://www.coolapk.com/feed/29518682?shareKey=NGU4ODM5Yjk3YjZmNjE4OTNiOTQ~&shareUid=633884&shareFrom=com.coolapk.market_11.4.3)。
