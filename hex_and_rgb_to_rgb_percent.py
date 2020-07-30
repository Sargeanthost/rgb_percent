def hex_to_rgb(hex):
    """Takes in hex tag and returns string of rgb percents

    Args:
        hex (string): hexcode

    Returns:
        string : rgb percents
    """
    hex = hex.lstrip('#')
    hlen = len(hex)
    return list(int(hex[i:i + hlen // 3], 16) /255  for i in range(0, hlen, hlen // 3))

hexOrRGB = input("Hex or RGB? ")
if hexOrRGB.lower() == "rgb":
    r = int(input("Enter R: "))
    g = int(input("Enter G: "))
    b = int(input("Enter B: "))
    print("R percent is {r:.3f}. G percent is {g:.3f}. B percent is {b:.3f}".format(r = r/255, g = g/255, b = b/255 ))
elif hexOrRGB.lower() == "hex":
    
    hexInput = input('Enter hex code: ')
    print(', '.join(f"{elem:.3f}" for elem in hex_to_rgb(hexInput)))
else:
    print("Please re-check your input")

