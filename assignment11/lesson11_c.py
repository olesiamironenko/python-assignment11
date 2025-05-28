from dash import Dash, dcc, html, Input, Output # Dash components needded for this program
import plotly.express as px # Dash relies on Plotly to do the plotting.  Plotly creates an HTML page with JavaScript.
import plotly.data as pldata # Access Plotly built in datasets.

df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True) # Loads specified Plotly built in dataset.

# Initialize Dash app
app = Dash(__name__)
# Creates the app object, to wich various things are added below. 
# __name__ is the name of the running Python module.

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="stock-dropdown", # Must have attribute for HTML element
        options=[{"label": symbol, "value": symbol} for symbol in df.columns], # Populates the dropdown with the list of stocks
        value="GOOG" # Initial value
    ),
    dcc.Graph(id="stock-price") # Must have attribute for HTML element
])

# Callback for dynamic updates
@app.callback( # Decorator for the update_graph() function
# Because of the decorator, the update_graph() will be called when the stock-dropdown changes, passing the value selected in the dropdown.
    Output("stock-price", "figure"), # Returns the graph back after passing in the value of the dropdown
    [Input("stock-dropdown", "value")] # Passssess in the value of the dropdown.
)
def update_graph(symbol): # The function that does the plot, by calling Plotly
    fig = px.line(df, x="date", y=symbol, title=f"{symbol} Price") # Line chart of date (which is the index) vs. the chosen stock price
    return fig

# Run the app
if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
    app.run(debug=True) # start the Flask web server