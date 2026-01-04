#!/usr/bin/env python
# coding: UTF-8


import markdown


def sco_md2html(s_md: str) -> str:

    s_body: Final[str] = markdown.markdown(
        s_md, extensions=['extra', 'codehilite', 'sane_lists']
    )

    s_html: Final[str] = f"""\
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        /* General page styles */
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6; 
            padding: 20px; 
            max-width: 900px; 
            margin: auto; 
            background: #0d1117; 
            color: #c9d1d9;
        }}

        /* Headers */
        h1, h2, h3 {{ 
            color: #f0f6fc; 
            border-bottom: 1px solid #30363d; 
            padding-bottom: 8px; 
        }}

        /* Code blocks */
        pre {{ 
            background: #161b22; 
            padding: 16px; 
            border-radius: 6px; 
            overflow: auto; 
            border: 1px solid #30363d; 
        }}

        /* Inline code */
        code {{ 
            font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
            background: rgba(110, 118, 129, 0.4); 
            padding: 0.2em 0.4em; 
            border-radius: 6px; 
            color: #e6edf3;
            font-size: 85%;
        }}

        /* Table styles */
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #30363d; padding: 8px 13px; }}
        th {{ background-color: #161b22; color: #f0f6fc; }}
        tr:nth-child(2n) {{ background-color: #161b22; }}
        
        /* Links */
        a {{ color: #58a6ff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}

        /* Blockquotes */
        blockquote {{
            padding: 0 1em;
            color: #8b949e;
            border-left: 0.25em solid #30363d;
            margin: 0;
        }}
    </style>
</head>
<body>
    {s_body}
</body>
</html>
"""

    return s_html


