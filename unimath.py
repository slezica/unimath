#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys    
from collections import defaultdict
from optparse import OptionParser

modes = {
    '$' : {
        'a' : 'α',
        'b' : 'β',
        'd' : 'δ', 'D' : 'Δ',
        'e' : 'ε',
        'f' : 'φ', 
        'g' : 'γ',
        'l' : 'λ', 'L' : 'Λ',
        'm' : 'μ', 'n' : 'ν',
        'p' : 'π', 'P' : 'Π',
        'r' : 'ρ', 
        's' : 'σ', 'S' : 'Σ',
        't' : 'θ',
        'u' : 'υ', 
        'w' : 'ω',
    },

    '^' : {
        '0' : '⁰',
        '1' : '¹',
        '2' : '²',
        '3' : '³',
        '4' : '⁴',
        '5' : '⁵',
        '6' : '⁶',
        '7' : '⁷', 
        '8' : '⁸',
        '9' : '⁹',
        '+' : '⁺', '-' : '⁻',
        '=' : '⁼',
        '(' : '⁽', ')' : '⁾',
        'n' : 'ⁿ',
        'i' : 'ⁱ'
    },

    '_' : {
        '0' : '₀',
        '1' : '₁',
        '2' : '₂',
        '3' : '₃',
        '4' : '₄',
        '5' : '₅',
        '6' : '₆',
        '7' : '₇',
        '8' : '₈',
        '9' : '₉',
        '+' : '₊',
        '-' : '₋',
        '=' : '₌',
        '(' : '₍',
        ')' : '₎',
        'a' : 'ₐ',
        'e' : 'ₑ',
        'h' : 'ₕ',
        'i' : 'ᵢ',
        'j' : 'ⱼ',
        'k' : 'ₖ',
        'l' : 'ₗ',
        'm' : 'ₘ',
        'n' : 'ₙ',
        'o' : 'ₒ',
        'p' : 'ₚ',
        'r' : 'ᵣ',
        's' : 'ₛ',
        't' : 'ₜ',
        'u' : 'ᵤ',
        'v' : 'ᵥ',
        'x' : 'ₓ',
    },

    '#' : {
        'A' : '∀',
        'E' : '∃', '!E': '∄',

        'i' : '∊', '!i' : '⋷',

        'N' : 'ℕ',
        'Z' : 'ℤ',
        'Q' : 'ℚ',
        'R' : 'ℝ',
        'C' : 'ℂ',

        'e' : 'ℯ',

        '8' : '∞',

    }
}

def translate(what):
    mode, escape, negate = None, False, False

    for ch in what:
        # Before anything else happens:
        if escape: escape = False; yield ch

        # Is this a flag?
        if ch == '\\': escape = True; yield ' '; continue
        if ch == '!' : negate = True; yield ' '; continue

        # Is this a mode switch?
        if ch in modes: mode = modes[ch]; yield ' '; continue

        # No switches. Time to yield. Are we in normal mode?
        if mode is None: yield ch; continue

        # Special mode! Is the character available in this mode?
        key = ch if not negate else '!'+ch
        if key in mode: yield mode[key]; continue

        # Not available. Mhh. We'll output it and revert to normal mode.
        mode = None
        yield ch

def stdin():
    for line in sys.stdin:
        for ch in line:
            yield ch

def cli():
    parser = OptionParser()

    parser.add_option('-i', '--stdin', action='store_true', default=False,
                      help="Process stdin instead of argument line")

    options, args = parser.parse_args()

    stream = stdin() if options.stdin else " ".join(args)

    print "".join(translate(stream)),

if __name__ == '__main__':
    cli();
