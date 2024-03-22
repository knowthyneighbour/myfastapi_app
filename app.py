# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:49:24 2024

@author: SG041720
"""
#Type the below on the browser search bar
#http://localhost:8000/api/test

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/test")
async def test():
    return "Hello World!"
