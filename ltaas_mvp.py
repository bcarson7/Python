#!/bin/python
VU = str(100)
URL = "http://blazedemo.com"

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
