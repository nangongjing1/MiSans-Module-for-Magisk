"""读取 Variable Fonts 字重轴"""

from fontTools.ttLib import TTFont

def extract_weights(variable_font_path):
    try:
        font = TTFont(variable_font_path)
        fvar = font['fvar']
        
        for axis in fvar.axes:
            if axis.axisTag == 'wght':
                min_weight = axis.minValue
                max_weight = axis.maxValue
                return min_weight, max_weight
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# 将字体的绝对路径粘贴至 #19
font_path = r"D:\Project\Python\20241020\MiSansVF.ttf"
weights = extract_weights(font_path)

if weights:
    print(f"权重范围: {weights[0]} to {weights[1]}")
else:
    print("未发现字重轴,请检查输入是否为 Variable Fonts 或字体文件是否损坏")
