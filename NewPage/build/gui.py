
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kapil\Documents\GitHub\RealTimeDashboard\NewPage\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1244x720")
window.configure(bg = "#EDEDED")

canvas = Canvas(
    window,
    bg = "#EDEDED",
    height = 1503,
    width = 1244,
    scrollregion=(0, 0, 1244, 1503),
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.pack(expand=True, fill = 'both')
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta/60), "units"))
scrollbar = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

canvas.create_text(
    489.0,
    93.0,
    anchor="nw",
    text="Average Response Times (1D)",
    fill="#000000",
    font=("Poppins Regular", 18 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    113.0,
    202.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    281.0,
    202.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    449.0,
    202.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    785.0,
    202.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    618.0,
    202.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    953.0,
    202.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1122.0,
    204.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    618.0,
    497.0,
    image=image_image_8
)

canvas.create_text(
    58.4000244140625,
    154.89999389648438,
    anchor="nw",
    text="enableDevices",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    226.4000244140625,
    154.89999389648438,
    anchor="nw",
    text="disableDevices",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    394.4000244140625,
    154.89999389648438,
    anchor="nw",
    text="addEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    724.39990234375,
    153.89999389648438,
    anchor="nw",
    text="removeAllEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    556.4000244140625,
    152.89999389648438,
    anchor="nw",
    text="removeEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    891.39990234375,
    154.89999389648438,
    anchor="nw",
    text="getDeviceEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    1060.39990234375,
    156.89999389648438,
    anchor="nw",
    text="getDeviceEntitlements",
    fill="#000000",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    58.0,
    170.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    226.0,
    169.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    394.0,
    169.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    730.0,
    169.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    562.0,
    169.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    898.0,
    170.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    1067.0,
    172.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Poppins Bold", 75 * -1)
)

canvas.create_text(
    118.0,
    209.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    284.0,
    209.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    455.0,
    209.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    791.0,
    209.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    622.0,
    209.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    957.0,
    209.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_text(
    1126.0,
    211.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins Bold", 29 * -1)
)

canvas.create_rectangle(
    167.5999755859375,
    244.5,
    180.89997577667236,
    257.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    335.5999755859375,
    244.5,
    348.89997577667236,
    257.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    503.5999755859375,
    244.5,
    516.8999757766724,
    257.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    839.60009765625,
    246.5,
    852.9000978469849,
    259.80000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1007.0,
    243.0,
    1020.3000001907349,
    256.30000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1176.0,
    245.0,
    1189.3000001907349,
    258.30000019073486,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    671.60009765625,
    244.5,
    684.9000978469849,
    257.80000019073486,
    fill="#000000",
    outline="")

canvas.create_text(
    36.0,
    24.0,
    anchor="nw",
    text="Dashboard",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_rectangle(
    37.0,
    72.0,
    1199.0,
    79.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    37.0,
    811.0,
    1202.0,
    1426.0,
    fill="#EDEDED",
    outline="")

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    619.0,
    1118.0,
    image=image_image_9
)

canvas.create_text(
    137.0,
    1306.0,
    anchor="nw",
    text="Request Wise Frequency",
    fill="#000000",
    font=("Poppins Bold", 14 * -1)
)

canvas.create_rectangle(
    338.0,
    1315.0,
    1176.0,
    1318.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    76.0,
    1317.0,
    120.0,
    1320.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    273.0,
    1353.0,
    313.0,
    1355.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    273.0,
    1383.0,
    313.0,
    1385.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    76.0,
    1341.0,
    anchor="nw",
    text="Enable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    76.0,
    1371.0,
    anchor="nw",
    text="Add Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    332.0,
    1341.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    332.0,
    1371.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    1084.0,
    1353.0,
    1124.0,
    1355.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1084.0,
    1383.0,
    1124.0,
    1385.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    887.0,
    1341.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    887.0,
    1371.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1142.0,
    1341.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1142.0,
    1371.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    679.0,
    1353.0,
    719.0,
    1355.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    679.0,
    1383.0,
    719.0,
    1385.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    482.0,
    1341.0,
    anchor="nw",
    text="Disable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    482.0,
    1371.0,
    anchor="nw",
    text="Get Device Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    737.0,
    1341.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    737.0,
    1371.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    48.0,
    740.0,
    anchor="nw",
    text="Analytics",
    fill="#000000",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    76.0,
    836.0,
    anchor="nw",
    text="Weekly Analytics",
    fill="#000000",
    font=("Poppins Bold", 24 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    962.0,
    944.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    962.0,
    1229.0,
    image=image_image_11
)

canvas.create_rectangle(
    49.0,
    790.0,
    1202.0,
    797.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    307.0,
    854.0,
    1176.0,
    859.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    76.0,
    880.0,
    anchor="nw",
    text="2131",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    76.0,
    963.0,
    anchor="nw",
    text="Requests This Week",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    137.0,
    1021.0,
    anchor="nw",
    text="Request Wise Frequency",
    fill="#000000",
    font=("Poppins Bold", 14 * -1)
)

canvas.create_rectangle(
    338.0,
    1030.0,
    1176.0,
    1033.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    76.0,
    1032.0,
    120.0,
    1035.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    273.0,
    1068.0,
    313.0,
    1070.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    273.0,
    1098.0,
    313.0,
    1100.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    76.0,
    1056.0,
    anchor="nw",
    text="Enable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    76.0,
    1086.0,
    anchor="nw",
    text="Add Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    332.0,
    1056.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    332.0,
    1086.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    1084.0,
    1068.0,
    1124.0,
    1070.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1084.0,
    1098.0,
    1124.0,
    1100.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    887.0,
    1056.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    887.0,
    1086.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1142.0,
    1056.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1142.0,
    1086.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    1084.0,
    897.0,
    1124.0,
    899.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1084.0,
    927.0,
    1124.0,
    929.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    887.0,
    885.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    887.0,
    915.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1142.0,
    885.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1142.0,
    915.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    1084.0,
    1182.0,
    1124.0,
    1184.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1084.0,
    1212.0,
    1124.0,
    1214.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    887.0,
    1170.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    887.0,
    1200.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1142.0,
    1170.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1142.0,
    1200.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    1084.0,
    956.0,
    1124.0,
    958.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1084.0,
    986.0,
    1124.0,
    988.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    887.0,
    944.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    887.0,
    974.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1142.0,
    944.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1142.0,
    974.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    1084.0,
    1241.0,
    1124.0,
    1243.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1084.0,
    1271.0,
    1124.0,
    1273.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    887.0,
    1229.0,
    anchor="nw",
    text="Remove Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    887.0,
    1259.0,
    anchor="nw",
    text="Remove All Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    1142.0,
    1229.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    1142.0,
    1259.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_rectangle(
    679.0,
    1068.0,
    719.0,
    1070.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    679.0,
    1098.0,
    719.0,
    1100.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    482.0,
    1056.0,
    anchor="nw",
    text="Disable Devices",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    482.0,
    1086.0,
    anchor="nw",
    text="Get Device Entitlements",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    737.0,
    1056.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    737.0,
    1086.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    323.58984375,
    881.0,
    anchor="nw",
    text="4.2 ",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    440.1025390625,
    908.0,
    anchor="nw",
    text="%",
    fill="#000000",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    323.58984375,
    963.0,
    anchor="nw",
    text="Failure Rate",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    581.26220703125,
    881.0,
    anchor="nw",
    text="36",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    581.26220703125,
    963.0,
    anchor="nw",
    text="Requests Failed",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    763.0,
    917.0,
    anchor="nw",
    text="Failed\nRequests",
    fill="#000000",
    font=("Poppins Bold", 20 * -1)
)

canvas.create_text(
    763.0,
    1202.0,
    anchor="nw",
    text="Failed\nRequests",
    fill="#000000",
    font=("Poppins Bold", 20 * -1)
)

canvas.create_text(
    69.0,
    1124.0,
    anchor="nw",
    text="Daily Analytics",
    fill="#000000",
    font=("Poppins Bold", 24 * -1)
)

canvas.create_rectangle(
    276.0,
    1139.0,
    1173.0,
    1144.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    69.0,
    1168.0,
    anchor="nw",
    text="392",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    69.0,
    1257.0,
    anchor="nw",
    text="Requests Today",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    316.58984375,
    1169.0,
    anchor="nw",
    text="3.4 ",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    433.1025390625,
    1196.0,
    anchor="nw",
    text="%",
    fill="#000000",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    316.58984375,
    1251.0,
    anchor="nw",
    text="Failure Rate",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    574.26220703125,
    1169.0,
    anchor="nw",
    text="12",
    fill="#000000",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    574.26220703125,
    1251.0,
    anchor="nw",
    text="Requests Failed",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)
window.resizable(True, True)
window.mainloop()
