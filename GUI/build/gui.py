
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kapil\Documents\GitHub\RealTimeDashboard\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1244x720")
window.configure(bg = "#EDEDED")


canvas = Canvas(
    window,
    bg = "#EDEDED",
    height = 720,
    width = 1244,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    187.0,
    720.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    93.0,
    46.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=20.0,
    y=644.0999755859375,
    width=149.10000610351562,
    height=39.900001525878906
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    719.0,
    395.0,
    image=image_image_2
)

canvas.create_text(
    227.0,
    17.0,
    anchor="nw",
    text="Analytics",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    255.0,
    113.0,
    anchor="nw",
    text="Weekly Analytics",
    fill="#000000",
    font=("Poppins Bold", 24 * -1)
)

canvas.create_rectangle(
    228.0,
    67.0,
    1223.0,
    74.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    486.0,
    131.0,
    1193.0,
    136.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    255.0,
    157.0,
    anchor="nw",
    text="2131",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    255.0,
    240.0,
    anchor="nw",
    text="Requests This Week",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    309.0,
    580.0,
    anchor="nw",
    text="Request Wise Frequency",
    fill="#000000",
    font=("Poppins Bold", 14 * -1)
)

canvas.create_rectangle(
    510.0,
    589.0,
    1193.0,
    592.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    248.0,
    591.0,
    292.0,
    594.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    445.0,
    627.0,
    485.0,
    629.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1034.0,
    627.0,
    1074.0,
    629.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    445.0,
    657.0,
    485.0,
    659.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    741.0,
    627.0,
    781.0,
    629.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1034.0,
    657.0,
    1074.0,
    659.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    741.0,
    657.0,
    781.0,
    659.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    248.0,
    615.0,
    anchor="nw",
    text="Enable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    837.0,
    615.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    248.0,
    645.0,
    anchor="nw",
    text="Add Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    544.0,
    615.0,
    anchor="nw",
    text="Disable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    837.0,
    645.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    544.0,
    645.0,
    anchor="nw",
    text="Get Device Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    491.0,
    615.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1080.0,
    615.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    491.0,
    645.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    787.0,
    615.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1080.0,
    645.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    787.0,
    645.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    316.0,
    289.0,
    anchor="nw",
    text="Request Wise Frequency",
    fill="#000000",
    font=("Poppins Bold", 14 * -1)
)

canvas.create_rectangle(
    517.0,
    298.0,
    1193.0,
    301.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    255.0,
    300.0,
    299.0,
    303.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    452.0,
    336.0,
    492.0,
    338.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1041.0,
    336.0,
    1081.0,
    338.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    452.0,
    366.0,
    492.0,
    368.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    748.0,
    336.0,
    788.0,
    338.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1041.0,
    366.0,
    1081.0,
    368.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    748.0,
    366.0,
    788.0,
    368.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    255.0,
    324.0,
    anchor="nw",
    text="Enable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    844.0,
    324.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    255.0,
    354.0,
    anchor="nw",
    text="Add Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    551.0,
    324.0,
    anchor="nw",
    text="Disable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    844.0,
    354.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    551.0,
    354.0,
    anchor="nw",
    text="Get Device Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    498.0,
    324.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1087.0,
    324.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    498.0,
    354.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    794.0,
    324.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1087.0,
    354.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    794.0,
    354.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    502.58984375,
    158.0,
    anchor="nw",
    text="4.2 ",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    619.1025390625,
    185.0,
    anchor="nw",
    text="%",
    fill="#000000",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    502.58984375,
    240.0,
    anchor="nw",
    text="Failure Rate",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    760.26220703125,
    158.0,
    anchor="nw",
    text="36",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    760.26220703125,
    240.0,
    anchor="nw",
    text="Requests Failed",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1005.611328125,
    157.0,
    anchor="nw",
    text="36",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    1005.611328125,
    240.0,
    anchor="nw",
    text="Requests Failed",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    248.0,
    401.0,
    anchor="nw",
    text="Daily Analytics",
    fill="#000000",
    font=("Poppins Bold", 24 * -1)
)

canvas.create_rectangle(
    455.0,
    416.0,
    1193.0,
    421.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    248.0,
    445.0,
    anchor="nw",
    text="392",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    248.0,
    534.0,
    anchor="nw",
    text="Requests Today",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    495.58984375,
    446.0,
    anchor="nw",
    text="3.4 ",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    612.1025390625,
    473.0,
    anchor="nw",
    text="%",
    fill="#000000",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    495.58984375,
    528.0,
    anchor="nw",
    text="Failure Rate",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    753.26220703125,
    446.0,
    anchor="nw",
    text="12",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    753.26220703125,
    528.0,
    anchor="nw",
    text="Requests Failed",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    998.611328125,
    445.0,
    anchor="nw",
    text="36",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    998.611328125,
    528.0,
    anchor="nw",
    text="Requests Failed",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=19.0,
    y=100.0,
    width=149.10000610351562,
    height=39.900001525878906
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=19.0,
    y=155.0,
    width=149.10000610351562,
    height=39.900001525878906
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=19.0,
    y=209.0,
    width=149.10000610351562,
    height=39.900001525878906
)
window.resizable(False, False)
window.mainloop()
