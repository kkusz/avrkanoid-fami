# AVRkanoid-Fami
AVRkanoid-Fami is a DYI Arkanoid paddle clone for Nintendo Famicom and famiclones using Digispark ATtiny85 as a base.

## Component list
* 1 x Digispark ATtiny85 (or compatible clone)
* 1 x 10kΩ 1/8W linear potentiometer
* 1 x 1kΩ 1/8W pull-up resistor
* 1 x Push button (momentary ON-OFF switch)
* 1 x DA-15 female cable (Famicom or Neo-Geo extension cord)
* 1 x Plastic box

## Firmware programming
Download newest [Arduino IDE](https://www.arduino.cc/en/software), add new [board manager](https://github.com/SpenceKonde/ATTinyCore/blob/v2.0.0-devThis-is-the-head-submit-PRs-against-this/Installation.md) and program your firmware with [avrkanoid-fami.ino](avrkanoid-fami.ino).

Note: If you've already soldered the cables and components to your board and cannot upload new program, try to adjust your potentiometer to around 50% to reduce USB interference coming from P3 input.
Alternatively you can use P5 instead of P3 if you're certain your Digispark is a legitimate one and not a Chinese clone (which in 2024 is more likely than ever). To check that, simply short P5 with GND to see if your board resets itself.

## Schematic
<img width="468" alt="DA15" src="https://github.com/kkusz/avrkanoid-fami/assets/61786451/c8e22cc5-8d10-47bf-b03e-164176049523">
<img width="995" alt="Schematic" src="https://github.com/kkusz/avrkanoid-fami/assets/61786451/298cf306-1edf-4bab-ae01-b3f25421aed6">

## Gallery
![20240120_231258](https://github.com/kkusz/avrkanoid-fami/assets/61786451/b409b472-ece0-444b-8fa2-f0d4fcac7646)

## Linearity compensation of knob
If your paddle goes really fast of really slow if you approach both edges of your knob, it might be that your potentiometer in not so linear as advertised.
From my experience the difference is significant as showed in the figure below:

![Knob_ADC_relation](https://github.com/kkusz/avrkanoid-fami/assets/61786451/1509e33b-1968-49ea-8cf7-a8507f99f549)

If you experiance similar issue, you might want to uncomment line 223 and comment out line 225 to turn on lookup table that compensates non linearity as in figure below:

![Linearity_figure](https://github.com/kkusz/avrkanoid-fami/assets/61786451/7453decd-58fc-46cb-8283-086da3da9680)

Of course, your potentiometer can have different kind of linearity error, so you can build your own LUT by measuring your knob position with a protractor and read raw value using one of the [test ROMs](https://forums.nesdev.org/viewtopic.php?t=23801), provided you have a flashcart like PowerPak/Everdrive/Krzysiocart.

Once you have your measurements in place, you can use script [vaus-linear.py](vaus-linear.py) to build LUT using linear interpolation between points and paste it into code.

## TODO
* Check compatibility with Arkanoid II.

## References
* https://www.msx.org/wiki/Digi::Arka
* https://www.nesdev.org/wiki/Arkanoid_controller
* https://www.nesdev.org/wiki/Input_devices
* https://hackaday.io/project/166068-vaus-arkanoid-paddle-clone


