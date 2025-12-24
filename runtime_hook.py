"""
PyInstaller runtime hook for TruthScript - Windows
Sets up paths for bundled ffmpeg and Tcl/Tk libraries
"""
import sys
import os

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
    
    # Add bundled ffmpeg to PATH (Windows)
    ffmpeg_path = os.path.join(bundle_dir, 'ffmpeg_bin')
    if os.path.isdir(ffmpeg_path):
        current_path = os.environ.get('PATH', '')
        if ffmpeg_path not in current_path:
            os.environ['PATH'] = ffmpeg_path + os.pathsep + current_path
    
    # Set Tcl/Tk library paths (for tkinter)
    tcl_path = os.path.join(bundle_dir, 'tcl')
    tk_path = os.path.join(bundle_dir, 'tk')
    
    if os.path.isdir(tcl_path):
        os.environ['TCL_LIBRARY'] = tcl_path
    if os.path.isdir(tk_path):
        os.environ['TK_LIBRARY'] = tk_path
    
    # Add bundle dir to Python path
    if bundle_dir not in sys.path:
        sys.path.insert(0, bundle_dir)
