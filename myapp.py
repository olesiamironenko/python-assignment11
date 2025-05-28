from dash import Dash, dcc, html, Input, Output # Dash components needded for this program
import plotly.express as px # Dash relies on Plotly to do the plotting.  Plotly creates an HTML page with JavaScript.
import plotly.data as pldata # Access Plotly built in datasets.

# Task 4: A Dashboard with Dash
# 4.1: Load Plotly built in gapminder dataset
df = pldata.gapminder(return_type='pandas', datetimes=True) 
# df.info()
# print(df.head(5))

# 4.2: Create a list of the unique country names from loaded dataset for a dropdown
countries = list(df["country"].drop_duplicates())
# print(countries)

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    # 4.2: Create a dropdown with list of the unique country names from loaded dataset created above
    # 4.3: Set dropdown id of 'country-dropdown' and a dcc.Graph id to 'gdp-growth'
    dcc.Dropdown(
        id="country-dropdown", 
        options=[{"label": country, "value": country} for country in countries], 
        value="Canada" # Initial value
    ),
    dcc.Graph(id="gdp-growth") # Must have attribute for HTML element
])

# 4.4: Decorator for the callback function
@app.callback( # Decorator for the update_graph() function
    Output("gdp-growth", "figure"), # Returns the graph back after passing in the value of the dropdown
    [Input("country-dropdown", "value")] # Passssess in the value of the dropdown.
)

# 4.5: Create a graph update function
def update_graph(country): # The function that does the plot, by calling Plotly
    # 4.5: Filter the dataset to get only the rows where the country column matches chosen country name.
    filtered_df = df[df["country"] == country]
    # 4.5: A line plot for 'year' vs. 'gdpPercap`
    fig = px.line(filtered_df, x="year", y="gdpPercap", title=f"{country} GDP per Capita", labels={"year": "Years", "gdpPercap": "GDP per Capita"}, markers=True)
    return fig



# 4.6-7: Run the app
if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
    app.run(debug=True) # start the Flask web server