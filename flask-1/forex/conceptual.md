### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
Javascript runs in the browser, Python is on server.  JS uses blocks, python uses indentations.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
use .get()  
use 'in'

- What is a unit test?  
tests a single function

- What is an integration test?  
tests how things work together

- What is the role of web application framework, like Flask?  
handles requests to server:  what to respond to and how.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
route url is better if "pretzel" is the focus of the page.  query is better if it is additional information.  often query would be used when getting info from form.

- How do you collect data from a URL placeholder parameter using Flask?  
like a url variable?  put the variable inside <> in the url string, and pass it in when creating the function.

- How do you collect data from the query string using Flask?  
import request  
request.args()

- How do you collect data from the body of the request using Flask?  
request.json

- What is a cookie and what kinds of things are they commonly used for?  
a name/value pair stored in the browser and sent to the server with each request.  
used for all kinds of things, such as sign in status, shopping cart, site preferences, etc.

- What is the session object in Flask?  
very similar to cookies.  basically like a dictionary that is stored in the browser.

- What does Flask's `jsonify()` do?  
tells the browser that the object in the () is JSON