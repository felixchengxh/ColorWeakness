import cv2
import numpy as np

colors = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'PURPLE': (128, 0, 128),
    'ORANGE': (255, 165, 0),
    'WHITE': (255, 255, 255),
    'GREY': (128, 128, 128),
    'BLACK': (0, 0, 0),
    'CHARTREUSE': (210, 229, 109),
    'FLESHTONE': (237, 218, 188),
    'OLIVE GREEN': (57, 69, 31),
    'OLIVE GREEN': (117, 132, 91),
    'LIME GREEN': (125, 150, 60),
    'ORANGE': (178, 93, 38),
    'BROWN': (96, 56, 77),
    'DARK GREY': (103, 93, 82),
    'CREAM': (247, 246, 216),
    'GREY': (181, 177, 176),
    'LIGHT GREY': (222, 218, 215),
    'LIGHT BROWN': (208, 181, 153),
    'LIGHT YELLOW': (186, 166, 89),	
    'DARK BROWN': (56, 40, 28),		
    'DARK BROWN': (61, 49, 32),
    'BROWN': (136, 104, 65),
    
    # 添加更多颜色...
}

def draw_patch(img, h, w, height, width, size):
    
    if h + size <= height and w + size <= width:
        b, g, r = mean_color_in_patch(img[h: h + size, w: w + size])
        # img[h: h + size, w: w + size] = b, g, r
        
    elif h + size <= height and w + size > width:
        b, g, r = mean_color_in_patch(img[h: h + size, w:])
        # img[h: h + size, w:] = b, g, r

    elif h + size > height and w + size <= width:
        b, g, r = mean_color_in_patch(img[h:, w:w + size])
        # img[h:, w:w + size] = b, g, r

    elif h + size > height and w + size > width:
        b, g, r = mean_color_in_patch(img[h:, w:])
        # img[h:, w:] = b, g, r
    return b, g, r
    
def color_block_square(img, size):
    height, width, c = img.shape
    i, j = 0, 0
    index_bgr = []
    for h in range(height):
        if h % size == 0:
            i += 1
            j = 0
        for w in range(width):
            if w % size == 0:
                j += 1
            if h % size == 0 and w % size == 0:
                b, g, r = draw_patch(img, h, w, height, width, size)
                index_bgr.append((i, j, (b, g, r)))

    return index_bgr

def find_closest_color(rgb):
    min_distance = float('inf')
    closest_color = None

    for color, value in colors.items():
        distance = np.linalg.norm(np.array(rgb) - np.array(value))
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    
    return closest_color

def mean_color_in_patch(patch):
    b, g, r = np.mean(np.mean(patch, axis=0), axis=0)
    return b, g, r

def convert_bgr2color(index_bgr):
    index_color = []
    for data in index_bgr:
        b, g, r = data[-1]
        text_color = find_closest_color((r, g, b))
        index_color.append((data[0], data[1], text_color))

    d1 = []
    d2 = []
    count = 0
    for i in range(len(index_bgr)):
        if i == 0:
            index_tmp = index_bgr[i][0]
            continue
        if index_tmp != index_bgr[i][0]:
            col = i
            break
    for i in range(len(index_color)):
        if i % col == 0 and i != 0:
            d1.append(d2)
            d2 = []
        if i == len(index_color)-1:
            d1.append(d2)
        d2.append(index_color[i][-1])
        count += 1
    return d1

def group_color(index_color):
    list_to_delete = np.ones((len(index_color), len(index_color[0])))
    grouped_color = []
    for i in range(len(index_color)):
        for j in range(len(index_color[0])):
            list_same_color = []
            if list_to_delete[i][j] == 0:
                continue
            elif i+1 < len(index_color) and j+1 < len(index_color[0]):
                list_same_color.append((i, j, index_color[i][j]))
                list_to_delete[i][j] = 0
                if index_color[i][j] == index_color[i+1][j]:
                    list_to_delete[i+1][j] = 0
                    list_same_color.append((i+1, j, index_color[i+1][j]))
                if index_color[i][j] == index_color[i][j+1]:
                    list_to_delete[i][j+1] = 0
                    list_same_color.append((i, j+1, index_color[i][j+1]))
                if index_color[i][j] == index_color[i+1][j+1]:
                    list_to_delete[i+1][j+1] = 0
                    list_same_color.append((i+1, j+1, index_color[i+1][j+1]))
                grouped_color.append(list_same_color)

    return grouped_color

def put_text_by_groups(img, grouped_color, size):
    thresh = int(0.5 * min(img.shape[0], img.shape[1]) / size)
    for i in range(len(grouped_color)):
        h = 0
        w = 0
        for j in range(len(grouped_color[i])):
            if len(grouped_color[i]) < thresh:
                continue
            h += (grouped_color[i][j][0] + 1)
            w += (grouped_color[i][j][1] + 1)
        # import pdb; pdb.set_trace()
        h /= len(grouped_color[i])
        w /= len(grouped_color[i])
        text_color = grouped_color[i][0][2]
        cv2.putText(img, '{}'.format(text_color), (int(w*size-size/2), int(h*size-size/2)), \
                    cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 0, 0))
    return img
