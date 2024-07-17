import os
from PIL import Image, ImageDraw
import cairosvg
import io


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def convert_svg_to_png(input_folder, output_folder, size=(144, 144), corner_radius=20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.svg'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)

            # Convert SVG to PNG in memory
            png_data = cairosvg.svg2png(url=input_path, output_width=size[0], output_height=size[1])

            # Open the PNG data with Pillow
            with Image.open(io.BytesIO(png_data)) as img:
                # Convert to RGBA if it's not already
                img = img.convert("RGBA")

                # Add rounded corners
                img = add_corners(img, corner_radius)

                # Save the image
                img.save(output_path)

            print(f"已转换 {filename} 为 {output_filename} (带圆角)")


# 使用示例
input_folder = 'flags'
output_folder = 'flags_png'
convert_svg_to_png(input_folder, output_folder)