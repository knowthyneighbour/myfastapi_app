# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:48:48 2024

@author: SG041720
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
