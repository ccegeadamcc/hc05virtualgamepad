# hc05virtualgamepad
I've used this to add an analog stick to my PS Move controller. If you are planning to use it for Ps Move too, please don't disassemble your controller. I have tried all of the VCC points I could find on board, and none of them works. Sometimes it doesn't give enough current, sometimes the controller shuts itself because of the overdrive I suppose. 
Maybe it is because my buck converter not efficient enough. Also, there is too much rev. for this board, so pins are not the same on all controllers.
 
I've connected Charging Dock pins to TP4056 with a 300mAh battery as a power solution. It's a dirty solution but It should be more than enough; It's small, not heavy, and I don't need to kill my board while tinkering.

I've used the Arduino Pro Mini because of its small size and pin count. However, you could use any Arduino supported board. 

You can check the PYXInput Github page for additional buttons.

I know I could just hack HC-05 to make it HID Gamepad. But I need two of them, and they will show up as different gamepads. Using a virtual gamepad, I can make one of them as the left axis and the other one as the right axis.


This project depends on:
https://pypi.org/project/pyserial/
https://pypi.org/project/PYXInput/

Please install these modules as described on their GitHub page before using this script since It won't work without them.
