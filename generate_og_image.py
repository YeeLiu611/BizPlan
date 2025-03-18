from PIL import Image, ImageDraw, ImageFont
import os

def create_og_image():
    # 创建图片尺寸
    width = 1200
    height = 630
    
    # 创建新图片，使用渐变背景
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # 创建渐变背景
    for y in range(height):
        # 计算渐变颜色
        r1, g1, b1 = 106, 48, 147  # #6a3093
        r2, g2, b2 = 160, 68, 255  # #a044ff
        r = int(r1 + (r2 - r1) * y / height)
        g = int(g1 + (g2 - g1) * y / height)
        b = int(b1 + (b2 - b1) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 添加文字
    try:
        # 尝试加载 Arial 字体，如果没有则使用默认字体
        title_font = ImageFont.truetype("Arial", 80)
        subtitle_font = ImageFont.truetype("Arial", 40)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # 添加标题
    title = "Worthy Space"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    title_x = (width - title_width) // 2
    title_y = height // 3
    draw.text((title_x, title_y), title, font=title_font, fill=(255, 255, 255))
    
    # 添加副标题
    subtitle = "All are worthy of love, respect, and dignity"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = title_y + title_height + 20
    draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill=(255, 255, 255))
    
    # 确保 images 目录存在
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # 保存图片
    image.save('images/og-image.png')
    print("预览图片已生成：images/og-image.png")

if __name__ == "__main__":
    create_og_image() 