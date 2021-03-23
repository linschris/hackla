from PIL import Image
import io
import base64


def get_barcode_data(string):
    # This receives a raw image data url. Look to Pillow documentation for specific parsing instructions.
    base64String = base64.b64decode(string)
    print(base64String)
    # img = Image.open(requests.get(imgurl, stream=True).raw)
    image_file = io.BytesIO(base64String)
    img = Image.open(image_file)
    img.show()
    # product_info = get_barcode_info(img)
    # return jsonify(product_info)

"data:/base64,"
get_barcode_data("iVBORw0KGgoAAAANSUhEUgAAAAUAAAAGCAYAAAAL+1RLAAAACXBIWXMAABnWAAAZ1gEY0crtAAAAO0lEQVQYV2N4dfrGfxB+efr6/5engPjk9f8Mr85ABMEScEGwKqDgKRBGFoQKYAiCtcIEQVpRBE9d/w8AIU5qMBmlubIAAAAASUVORK5CYII=")