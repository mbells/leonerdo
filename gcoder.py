'''
Hacked up code to draw g-code for Makelangelo.

It takes paths from OpenCV.

Limitations:
* size: not settable and almost certainly wrong
* feed rate not settable

See https://en.wikipedia.org/wiki/G-code
---
    Leonerdo: Interactive art drawing robot
    Copyright (C) 2016  Matthew Bells

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
---

M101 T32.5 B-32.5 L-32.5 R32.5 I1 J-1;
D1 L1.4840 R1.4840;
G92 X0.0 Y10.798999786376953;
M06 T0;
G00 F3500.0 A20.0;    # feed rate, absolute position??
G90;                  # abs positioning
G00 G90;              # abs positioning
M06 T0;               # tool selection
G00 F3500.0 A20.0;

G00 Z50;              # pen up
G00 X-5.4 Y-58.865;
G00 Z90;              # pen down
G00 X-3.9 Y-60.276;
G00 X-2.4 Y-58.612;
G00 X-0.9 Y-60.394;
G00 X0.6 Y-58.406;
G00 X2.1 Y-60.659;
G00 X3.6 Y-58.282;
G00 X5.1 Y-60.718;
G00 X6.6 Y-58.282;
G00 X8.1 Y-60.718;
G00 X9.6 Y-58.282;
G00 X11.1 Y-60.718;
G00 X12.6 Y-58.276;
G00 X14.1 Y-60.724;
G00 X15.6 Y-58.182;
G00 X17.1 Y-60.859;
G00 X18.6 Y-58.135;
G00 X20.1 Y-60.841;
G00 X21.6 Y-58.3;
G00 X23.1 Y-60.671;
G00 X24.6 Y-58.594;
G00 X26.1 Y-60.271;
G00 X27.6 Y-58.965;
G00 X29.1 Y-59.982;
G00 Z50;
'''

class GCoder:
    contours = []

    def __init__(self):
        pass

    def add_lines(self, contours):
        self.contours.extend(contours)

    def write(self, filename):
        with open(filename, 'w') as f:
            self._write_header(f)
            self._write_lines(f, self.contours)

    def _write_header(self, file):
        # bounds top, bottom, left, right, ??, ??
        file.write('M101 T32.5 B-32.5 L-32.5 R32.5 I1 J-1;\n')
        file.write('D1 L1.4840 R1.4840;\n')   # tool diameter
        # position register??
        file.write('G92 X0.0 Y10.798999786376953;\n')
        file.write('M06 T0;\n')               # tool selection
        file.write('G00 F3500.0 A20.0;\n')    # feed rate, absolute position??
        file.write('G90;\n')                  # abs positioning
        file.write('G00 G90;\n')              # abs positioning
        file.write('M06 T0;\n')               # tool selection??
        file.write('G00 F3500.0 A20.0;\n')    # feed rate, absolute position??
        
    def _write_lines(self, file, contours):
        for shape in contours:
            pa = shape[0]
            point = map(tuple, pa)[0]
            file.write('G00 Z50;\n')
            print('point=', point)
            file.write('G00 X{0} Y{1};\n'.format(*point))
            file.write('G00 Z90;\n')
            for pa in shape[1:]:
                point = map(tuple, pa)[0]
                print('point=', point)
                file.write('G00 X{0} Y{1};\n'.format(*point))

