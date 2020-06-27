#!/usr/bin/env python3

import requests as req

resp = req.get("https://uqu.edu.sa/")

print(resp.text)

