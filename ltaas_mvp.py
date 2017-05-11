#!/bin/python
VU = ''
URL = ''

while not URL:
        print('Enter your load destination including http')
        URL = raw_input()

print('Emter the number of virtual users? (100 or fewer)')
VU = raw_input()
if int(VU) > 100:
        VU = 1
VU=str(VU)
F = open('test.yml','w')
F.write(
"execution:" +"\n"
"- concurrency: " + VU + "\n"
"  ramp-up: 1m" + "\n"
"  hold-for: 5m" + "\n"
"  scenario: quick-test" + "\n"
"\n"
"scenarios:" + "\n"
"  quick-test:" + "\n"
"    requests:" + "\n"
"    - " + URL + "\n"
)
F.close()
