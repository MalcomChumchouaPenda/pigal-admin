
from dash import html
from core.utils import create_dash


ui = create_dash('dashboard')
ui.layout = html.Div("My Dash app")

