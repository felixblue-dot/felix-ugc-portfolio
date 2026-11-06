#!/usr/bin/env python3
"""Builds de.html from index.html: same page, German <html lang>, title, description and
link-preview tags, so WhatsApp / Slack / LinkedIn show German text for unstuck.social/de.
Run after every change to index.html:  python3 make-de.py"""
import re
src = open('index.html', encoding='utf-8').read()
TITLE = 'Felix | UGC-Ads für Apps, Tech- und Travel-Marken'
DESC = 'Short-Form-Ads für Apps, Tech- und Travel-Marken, gebaut auf Hook Rate und Link-CTR. Starte mit einem Testvideo.'
def sub(pattern, repl):
    global src
    out, n = re.subn(pattern, repl, src, count=1)
    assert n == 1, pattern
    src = out
sub(r'<html lang="en">', '<html lang="de">')
sub(r'<title>.*?</title>', f'<title>{TITLE}</title>')
sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">')
sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://www.unstuck.social/de">')
sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://www.unstuck.social/de">')
sub(r'<meta property="og:locale" content="en_US">', '<meta property="og:locale" content="de_DE">')
sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{TITLE}">')
sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{DESC}">')
sub(r'<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="{TITLE}">\n<meta name="twitter:description" content="{DESC}">')
open('de.html', 'w', encoding='utf-8').write(src)
print('de.html written')
