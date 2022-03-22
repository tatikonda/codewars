def count_checkerboard(width, height, resolution):
    p = resolution * 2
    sw = width // p * resolution + min(width % p, resolution)
    print(sw)
    sh = height // p * resolution + min(height % p, resolution)
    print(sh)
    return (width - sw) * sh + sw * (height - sh)

print(count_checkerboard(9, 5, 2))