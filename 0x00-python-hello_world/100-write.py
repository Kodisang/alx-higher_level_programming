#!/usr/bin/python3
import os

message = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
os.write(2, message.encode())
exit(1)
