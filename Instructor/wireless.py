import pygetwindow as gw
import ctypes

def detect_mouse_devices():
    windows = gw.getWindowsWithTitle("")
    mouse_devices = []

    for window in windows:
        title = window.title.lower()
        if 'mouse' in title:
            mouse_devices.append(window.title)

    if not mouse_devices:
        # If no mouse devices detected based on window titles, try low-level input
        mouse_devices = get_connected_mice()

    if mouse_devices:
        print("Mouse devices detected:")
        for device in mouse_devices:
            print(f"Device Name: {device}")
    else:
        print("No mouse devices detected.")

def get_connected_mice():
    mouse_devices = []

    # Define the RawInputDevice structure
    class RAWINPUTDEVICE(ctypes.Structure):
        _fields_ = [("usUsagePage", ctypes.c_ushort),
                    ("usUsage", ctypes.c_ushort),
                    ("dwFlags", ctypes.c_ulong),
                    ("hwndTarget", ctypes.c_void_p)]

    # Constants
    RIDEV_INPUTSINK = 0x00000100
    RID_INPUT = 0x10000003

    # Register for mouse input
    rid = RAWINPUTDEVICE()
    rid.usUsagePage = 0x01  # HID_USAGE_PAGE_GENERIC
    rid.usUsage = 0x02  # HID_USAGE_GENERIC_MOUSE
    rid.dwFlags = RIDEV_INPUTSINK
    rid.hwndTarget = ctypes.c_void_p()

    if ctypes.windll.user32.RegisterRawInputDevices(ctypes.byref(rid), 1, ctypes.sizeof(RAWINPUTDEVICE)):

        # Process raw input messages to identify connected mice
        while True:
            msg = ctypes.wintypes.MSG()
            ctypes.windll.user32.GetMessageW(ctypes.byref(msg), None, 0, 0)

            if msg.message == RID_INPUT:
                mouse_devices.append(f"RawInputDevice: {msg.hDevice}")

            ctypes.windll.user32.DefRawInputProc(ctypes.byref(msg), 1, ctypes.sizeof(RAWINPUTDEVICE))

    return mouse_devices

if __name__ == "__main__":
    detect_mouse_devices()
