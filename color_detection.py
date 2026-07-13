import cv2
import numpy as np
import pandas as pd

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]

csv = pd.read_csv(
    r"C:\Users\Dell\VS_CODE_PROJECT\Colour Detection Project\colors.csv",
    names=index,
    header=None
)

# Function to calculate minimum distance from all colors and get the most matching color
def getColorName(R, G, B):
    minimum = 10000
    cname = ""

    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + \
            abs(G - int(csv.loc[i, "G"])) + \
            abs(B - int(csv.loc[i, "B"]))

        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]

    return cname


# Function to get x, y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked

    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos = x
        ypos = y

        b, g, r = img[y, x]

        b = int(b)
        g = int(g)
        r = int(r)


# Specify image path
img_path = r"C:\Users\Dell\VS_CODE_PROJECT\Colour Detection Project\colorpic.jpg"

# Reading image
img = cv2.imread(img_path)

print("Program Started")
print(img)

# Check whether image is loaded successfully
if img is None:
    print("Image not found!")
    print("Check whether colorpic.jpg exists in:")
    print(img_path)
    exit()

# Declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

print("Opening Window...")

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

    cv2.imshow("image", img)

    if clicked:

        # Draw rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Create text string
        text = getColorName(r, g, b) + \
               ' R=' + str(r) + \
               ' G=' + str(g) + \
               ' B=' + str(b)

        # White text
        text_color = (255, 255, 255)

        # Black text for light colors
        if r + g + b >= 600:
            text_color = (0, 0, 0)

        cv2.putText(
            img,
            text,
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            text_color,
            2,
            cv2.LINE_AA
        )

        clicked = False

    # Press ESC key to exit
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()