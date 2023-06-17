import qrcode
import qrcode.image.svg

method = "path"

data = "example.com"

if __name__ == "__main__":
    if method == "basic":
        # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
    elif method == "fragment":
        # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
    elif method == "path":
        # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(data, image_factory=factory)

    img.save("qr.svg")
    print("QR Code saved as qr.svg")
