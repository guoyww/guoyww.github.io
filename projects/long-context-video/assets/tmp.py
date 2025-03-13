import os
from PIL import Image

def convert_png_to_jpg_with_black_bg():
    # 获取当前目录下所有文件
    files = os.listdir('.')
    
    # 筛选出PNG文件
    png_files = [f for f in files if f.lower().endswith('.png')]
    
    print(f"找到 {len(png_files)} 个PNG文件")
    
    for png_file in png_files:
        try:
            # 打开PNG图片
            img = Image.open(png_file)
            
            # 检查图片是否有alpha通道（RGBA或带透明的调色板模式）
            has_transparency = False
            
            if img.mode == 'RGBA':
                has_transparency = True
            elif img.mode == 'P':
                # 检查调色板模式的图像是否有透明度
                if img.info.get('transparency', None) is not None or 'transparency' in img.info:
                    has_transparency = True
                    # 转换为RGBA以便正确处理透明度
                    img = img.convert('RGBA')
            
            if has_transparency:
                print(f"处理: {png_file}")
                
                # 创建一个新的黑色背景图像
                black_bg = Image.new('RGB', img.size, (0, 0, 0))
                
                # 将原图合成到黑色背景上
                black_bg.paste(img, (0, 0), img)
                
                # 生成输出文件名（替换.png为.jpg）
                jpg_filename = os.path.splitext(png_file)[0] + '.jpg'
                
                # 保存为JPG
                black_bg.save(jpg_filename, 'JPEG', quality=95)
                
                print(f"已保存: {jpg_filename}")
            else:
                print(f"跳过: {png_file} (无透明通道)")
                
        except Exception as e:
            print(f"处理 {png_file} 时出错: {str(e)}")
    
    print("处理完成")

if __name__ == "__main__":
    convert_png_to_jpg_with_black_bg()