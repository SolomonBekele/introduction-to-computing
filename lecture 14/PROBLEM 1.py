from cs1media import *
white = (255, 255, 255)
black = (0, 0, 0)

def convert_to_bw(statue, threshold):
    w, h = statue.size()
    for y in range(h):
        for x in range(w):
            r, g, b = statue.get(x, y)
            intensity = int(0.213 * r + 0.715 * g + 0.072 * b)
            if intensity > threshold:
                statue.set(x, y, white)
            else:
                statue.set(x, y, black)
    statue.show()
    return statue

def make_even(campus):
    w, h = campus.size()
    for y in range(h):
        for x in range(w):
            r, g, b = campus.get(x, y)
            if r % 2 != 0:
                r -= 1
            campus.set(x, y, (r, g, b))
    campus.show()
    return campus

def hide_statue(campus, statue, x1, y1):
    w, h = statue.size()
    for y in range(h):
        for x in range(w):
            p = statue.get(x, y)
            if p == black:
                r1, g1, b1 = campus.get(x1 + x, y1 + y)
                r1 += 1
                campus.set(x1 + x, y1 + y, (r1, g1, b1))
    campus.show()
    return campus

def extract_picture(campus, statue, x1, y1):
    w, h = statue.size()
    for y in range(h):
        for x in range(w):
            r, g, b = campus.get(x1 + x, y1 + y)
            if r % 2 == 0:
                statue.set(x, y, white)
            else:
                statue.set(x, y, black)
    statue.show()
    return statue

def hide_picture(campus, statue, x1, y1):
    campus = make_even(campus)
    hide_statue(campus, statue, x1, y1)
    return campus

campus = load_picture("photos/trees1.jpg")
statue = load_picture("photos/statue1.jpg")

statue = convert_to_bw(statue, 128)
campus = hide_picture(campus, statue, 200, 50)
statue = extract_picture(campus, statue, 200, 50)

