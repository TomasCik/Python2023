
#
# import json
#
# with open('json_colors.json') as file:
#     data = json.load(file)
#
# for color in data['colors']:
#     color_name = color['color']
#     color['code']['rgb'] = color['code']['rgba'][:3]
#     del color['code']['rgba']
#     del color['category']
#     hex_code = color['code']['hex']
#
#
#
# with open('updated_json_colors.json', 'w') as file:
#     json.dump(data, file, indent=2)


import json

with open('json_colors.json') as file:
    data = json.load(file)

for color in data['colors']:
    color['rgb'] = ', '.join(map(str, color['code']['rgba'][:3]))
    color['hex'] = color['code']['hex']
    del color['category']
    del color['code']
    if 'type' in color:
        del color['type']

with open('updated_json_colors.json', 'w') as file:
    json.dump(data, file, indent=2)





