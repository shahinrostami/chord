"""
Chord - Python wrapper around d3-chord

This package enables the generation of Chord diagrams. They can be saved 
directly to HTML files or displayed in a Jupyter Notebook output cell.

Copyright 2020, Dr. Shahin Rostami
http://shahinrostami.com
https://github.com/shahinrostami/chord
https://pypi.org/project/chord/
"""
""" LICENSE
Chord (https://github.com/shahinrostami/chord) generates interactive chord diagrams.
Copyright (C) 2020  Dr. Shahin Rostami

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import urllib.request
import json

class Chord(object):
    user = "free"
    key = "free"

    def __init__(
        self,
        matrix,
        names,
        colors="d3.schemeSet1",
        opacity=0.8,
        padding=0.01,
        width=700,
        label_color="#454545",
        wrap_labels=True,
        margin=100,
        credit=False,
        font_size="16px",
        font_size_large="20px",
        details=[],
        details_thumbs=[],
        thumbs_width=85,
        thumbs_margin=5,
        thumbs_font_size=14,
        popup_width=350,
        noun="instances",
        details_separator=", ",
        divide=False,
        divide_idx=0,
        divide_size=0.5,
        instances=0,
        verb="occur together in",
        symmetric=True,
        title="",
        arc_numbers=False,
        divide_left_label="",
        divide_right_label="",
        inner_radius_scale=0.45,
        outer_radius_scale=1.1,
        allow_download=False,
        conjunction="and",
        reverse_gradients=False,
        curved_labels=True,
        rotate=0,

    ):
        self.html = ""
        self.matrix = matrix
        self.names = names
        self.colors = colors
        self.opacity = opacity
        self.padding = padding
        self.width = width
        self.label_color = label_color
        self.wrap_labels = wrap_labels
        self.margin = margin
        self.credit = credit
        self.font_size = font_size
        self.font_size_large = font_size_large
        self.details = details
        self.details_thumbs = details_thumbs
        self.thumbs_width = thumbs_width
        self.thumbs_margin = thumbs_margin
        self.thumbs_font_size = thumbs_font_size
        self.popup_width = popup_width
        self.noun = noun
        self.details_separator = details_separator
        self.divide = divide
        self.divide_idx = divide_idx
        self.divide_size = divide_size
        self.instances = instances
        self.verb = verb
        self.symmetric = symmetric
        self.title = title
        self.arc_numbers = arc_numbers
        self.divide_left_label = divide_left_label
        self.divide_right_label = divide_right_label
        self.inner_radius_scale = inner_radius_scale
        self.outer_radius_scale = outer_radius_scale
        self.allow_download = allow_download
        self.conjunction = conjunction
        self.reverse_gradients = reverse_gradients
        self.curved_labels = curved_labels
        self.rotate = rotate

    def __str__(self):
        return self.html

    def get_payload(self):
        """Returns the payload as a dictionary of Chord diagram customisations."""
        payload = {
            "colors": self.colors,
            "opacity": self.opacity,
            "matrix": self.matrix,
            "names": self.names,
            "padding": self.padding,
            "width": self.width,
            "label_color": self.label_color,
            "wrap_labels": "true" if self.wrap_labels else "false",
            "credit": "true" if self.credit else "false",
            "margin": self.margin,
            "font_size": self.font_size,
            "font_size_large": self.font_size_large,
            "details": self.details,
            "details_thumbs": self.details_thumbs,
            "thumbs_font_size": self.thumbs_font_size,
            "thumbs_width": self.thumbs_width,
            "thumbs_margin": self.thumbs_margin,
            "popup_width": self.popup_width,
            "noun": self.noun,
            "details_separator": self.details_separator,
            "divide": "true" if self.divide else "false",
            "divide_idx": self.divide_idx,
            "divide_size": self.divide_size,
            "instances": self.instances,
            "verb": self.verb,
            "symmetric": "true" if self.symmetric else "false",
            "title": self.title,
            "arc_numbers": "true" if self.arc_numbers else "false",
            "divide_left_label": self.divide_left_label,
            "divide_right_label": self.divide_right_label,
            "inner_radius_scale": self.inner_radius_scale,
            "outer_radius_scale": self.outer_radius_scale,
            "allow_download": "true" if self.allow_download else "false",
            "conjunction": self.conjunction,
            "reverse_gradients": "true" if self.reverse_gradients else "false",
            "rotate": self.rotate,
        }

        return payload

    def render_html(self):
        """Generates the HTML using the Chord service."""
        if(Chord.user == "free" and Chord.key == "free"):
            url = "https://api.shahin.dev/chordfree"
        else:
            url = "https://api.shahin.dev/chord"

        import requests

        payload = self.get_payload()

        result = requests.post(url, json=payload, auth=(Chord.user, Chord.key))

        if result.status_code == 200:
            self.html = result.text
        elif result.status_code == 401:
            detail = json.loads(result.content.decode('utf8'))['detail']
            raise Exception(detail)
        else:
            raise Exception("API error.")

    def render_png(self):
        """Generates the PNG using the Chord service."""
        url = "https://api.shahin.dev/chord_png"

        import requests

        payload = self.get_payload()

        result = requests.post(url, json=payload, auth=(Chord.user, Chord.key))

        if result.status_code == 200:
            return result.content
        elif result.status_code == 401:
            detail = json.loads(result.content.decode('utf8'))['detail']
            raise Exception(detail)
        else:
            raise Exception("API error.")

    def to_html(self, filename="out.html"):
        """Outputs the generated HTML to a HTML file. """
        self.render_html()
        file = open(filename, "w")
        file.write(self.html)
        file.close()
    
    def to_string(self):
        """Returns the generated HTML as a string."""
        return self.html

    def to_png(self, filename="out.png"):
        """Outputs the generated PNG to a file. """
        image = self.render_png()
        file = open(filename,'wb')
        file.write(image)
        file.close()

    def show(self):
        """Outputs the generated HTML to a Jupyter Lab output cell."""
        self.render_html()
        from IPython.display import display, HTML

        display(HTML(self.html))
    
    def show_png(self):
        """Outputs the generated PNG to a Jupyter Lab output cell."""
        image = self.render_png()
        from IPython.core.display import Image, display
        display(Image(image))
