"""Render the current studio scene using the previously approved LuxCore pipeline.

Run with the existing python39-luxcore runtime after export-tetherxyz-studio.py.
"""
from pathlib import Path
import sys
from types import SimpleNamespace

sys.path.insert(0, str(Path.home()/'Portfolio Renders/2026-09-14'))
import render_turntables as renderer
renderer.ROOT=Path.home()/'Portfolio Renders/tetherxyz-current-studio'
renderer.render('xyz-machine',SimpleNamespace(
    folder='portfolio',width=720,height=480,samples=32,frames=48,
    count=int(sys.argv[1]) if len(sys.argv)>1 else 0,engine='PATHCPU'))
