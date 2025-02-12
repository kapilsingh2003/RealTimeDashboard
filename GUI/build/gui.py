
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
    y=98.0,
    width=149.10000610351562,
    height=39.900001525878906
)

canvas.create_text(
    587.0,
    84.0,
    anchor="nw",
    text="Average Response Times (1D)",
    fill="#000000",
    font=("Poppins Regular", 18 * -1)
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
    x=20.0,
    y=153.0,
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
    x=20.0,
    y=207.0,
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
    x=20.0,
    y=644.0999755859375,
    width=149.10000610351562,
    height=39.900001525878906
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    304.0,
    195.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    472.0,
    195.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    640.0,
    195.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    976.0,
    195.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    809.0,
    195.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1144.0,
    195.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    726.0,
    490.0,
    image=image_image_8
)

canvas.create_text(
    249.39999389648438,
    147.89999389648438,
    anchor="nw",
    text="enableDevices",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    417.4000244140625,
    147.89999389648438,
    anchor="nw",
    text="disableDevices",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    585.4000244140625,
    147.89999389648438,
    anchor="nw",
    text="addEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    915.4000244140625,
    146.89999389648438,
    anchor="nw",
    text="removeAllEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    747.4000244140625,
    145.89999389648438,
    anchor="nw",
    text="removeEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    1082.4000244140625,
    147.89999389648438,
    anchor="nw",
    text="getDeviceEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    249.0,
    163.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    417.0,
    162.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    585.0,
    162.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    921.0,
    162.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    753.0,
    162.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    1089.0,
    163.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    309.0,
    202.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    475.0,
    202.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    646.0,
    202.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    982.0,
    202.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    813.0,
    202.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    1148.0,
    202.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_rectangle(
    358.5999755859375,
    237.5,
    371.89997577667236,
    250.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    526.5999755859375,
    237.5,
    539.8999757766724,
    250.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    694.5999755859375,
    237.5,
    707.8999757766724,
    250.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1030.5999755859375,
    239.5,
    1043.8999757766724,
    252.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1198.0,
    236.0,
    1211.3000001907349,
    249.30000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    862.5999755859375,
    237.5,
    875.8999757766724,
    250.80000019073486,
    fill="#000000",
    outline="")

canvas.create_text(
    227.0,
    17.0,
    anchor="nw",
    text="Dashboard",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_rectangle(
    228.0,
    65.0,
    1221.0,
    72.0,
    fill="#D9D9D9",
    outline="")
window.resizable(False, False)
window.mainloop()
