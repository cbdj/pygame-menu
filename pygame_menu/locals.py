"""
pygame-menu
https://github.com/ppizarror/pygame-menu

LOCALS
Local constants.

License:
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2017-2021 Pablo Pizarro R. @ppizarror

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------
"""

__all__ = [

    # Alignment
    'ALIGN_CENTER',
    'ALIGN_LEFT',
    'ALIGN_RIGHT',

    # Data types
    'INPUT_FLOAT',
    'INPUT_INT',
    'INPUT_TEXT',

    # Positioning
    'POSITION_CENTER',
    'POSITION_EAST',
    'POSITION_NORTH',
    'POSITION_NORTHEAST',
    'POSITION_SOUTHWEST',
    'POSITION_SOUTH',
    'POSITION_SOUTHEAST',
    'POSITION_NORTHWEST',
    'POSITION_WEST',

    # Scrollarea
    'SCROLLAREA_POSITION_BOTH_HORIZONTAL',
    'SCROLLAREA_POSITION_BOTH_VERTICAL',
    'SCROLLAREA_POSITION_FULL',

    # Cursors
    'CURSOR_HAND'

]

# Alignment
ALIGN_CENTER = 'align-center'
ALIGN_LEFT = 'align-left'
ALIGN_RIGHT = 'align-right'

# Input data type
INPUT_FLOAT = 'input-float'
INPUT_INT = 'input-int'
INPUT_TEXT = 'input-text'

# Position
POSITION_CENTER = 'position-center'
POSITION_EAST = 'position-east'
POSITION_NORTH = 'position-north'
POSITION_NORTHEAST = 'position-northeast'
POSITION_NORTHWEST = 'position-northwest'
POSITION_SOUTH = 'position-south'
POSITION_SOUTHEAST = 'position-southeast'
POSITION_SOUTHWEST = 'position-southwest'
POSITION_WEST = 'position-west'

# Menu scroll area position
SCROLLAREA_POSITION_BOTH_HORIZONTAL = 'scrollarea-position-both-horizontal'
SCROLLAREA_POSITION_BOTH_VERTICAL = 'scrollarea_position-both-vertical'
SCROLLAREA_POSITION_FULL = 'scrollarea-position-full'

# Orientation
ORIENTATION_HORIZONTAL = 'orientation-horizontal'
ORIENTATION_VERTICAL = 'orientation-vertical'

# Cursors
import pygame as _pygame

CURSOR_HAND = None
if hasattr(_pygame, 'SYSTEM_CURSOR_HAND'):
    CURSOR_HAND = _pygame.SYSTEM_CURSOR_HAND
