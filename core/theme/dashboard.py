
import dash
from dash import html, dcc


layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

# print('\n\t', 'looping registry')
# for key, value in dash.page_registry.items():
#     print('\t', key, '>', value)