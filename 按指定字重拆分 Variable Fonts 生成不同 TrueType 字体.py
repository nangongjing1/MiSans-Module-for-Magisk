"""按指定字重拆分 Variable Fonts 生成不同 TrueType 字体"""

from fontTools.ttLib import TTFont, newTable

def generate_ttf_from_weight(variable_font_path, output_path, weight):
    try:
        font = TTFont(variable_font_path)
    except Exception as e:
        print(f"读取字体文件时出错: {e}")
        return

    fvar = font.get('fvar')
    wght_axis = next((axis for axis in fvar.axes if axis.axisTag == 'wght'), None)
    if not wght_axis:
        print("未发现字重轴，请检查输入是否为 Variable Fonts 或字体文件是否损坏")
        return

    if weight < wght_axis.minValue or weight > wght_axis.maxValue:
        print(f"设定的 Weight {weight} 超出 Variable Fonts 字重范围 ({wght_axis.minValue} ~ {wght_axis.maxValue}).")
        return

    new_font = TTFont()
    new_font.setGlyphOrder(font.getGlyphOrder())

    # 复制其他表格
    for table_tag in font.keys():
        if table_tag not in ['fvar', 'gvar']:
            new_font[table_tag] = font[table_tag]

    # 设置新的 'fvar' 表
    new_fvar = newTable('fvar')
    new_fvar.axes = fvar.axes[:]
    
    for axis in new_fvar.axes:
        if axis.axisTag == 'wght':
            axis.defaultValue = weight
            axis.minValue = weight
            axis.maxValue = weight

    new_font['fvar'] = new_fvar

    # 处理 'gvar' 表
    if 'gvar' in font:
        new_gvar = newTable('gvar')
        new_gvar.variations = {}

        for glyph_name, variations in font['gvar'].variations.items():
            new_variations = []
            for variation in variations:
                # 直接使用原变体，省略 delta
                new_variation = variation.__class__(variation.axes, variation.coordinates)
                new_variations.append(new_variation)

            new_gvar.variations[glyph_name] = new_variations

        new_font['gvar'] = new_gvar

    try:
        new_font.save(output_path)
        print(f"字重为 {weight} 的字体已生成在 {output_path}")
    except Exception as e:
        print(f"保存字体文件时出错: {e}")

# 自定义部分，使用绝对路径
variable_font_path = r"D:\Project\Python\20241020\MiSansVF.ttf"
output_path = r"D:\Project\Python\20241020\MiSans Light.ttf"
weight = 300

generate_ttf_from_weight(variable_font_path, output_path, weight)
