purpose="new_think learning"

"""
step-1 : we need  to create MCP object
similar to flask and FastAPI object
app=Flask(__name__)===> app.run
app=FastAPI()      ===> aap.run
mcp=FastMCP()      ===> mcp.run
"""

from mcp.server.fastmcp import FastMCP
mcp=FastMCP("whether server")

"""Step-2: create the first tool"""

@mcp.tool()
def get_weather(city):
    return(f'the weather in {city} is 35 degrees C')

"""step-3: Run the server"""

if __name__=="__main__":
    mcp.run()