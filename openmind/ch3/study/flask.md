
Quickstart¶

Eager to get started?  This page gives a good introduction to Flask.  Itassumes you already have Flask installed.  If you do not, head over to theInstallation section.

A Minimal Application¶

A minimal Flask application looks something like this:

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
So what did that code do?

1. First we imported the Flask class.  An instance of thisclass will be our WSGI application.
2. Next we create an instance of this class. The first argument is the name ofthe application’s module or package.  If you are using a single module (asin this example), you should use __name__ because depending on if it’sstarted as application or imported as module the name will be different('__main__' versus the actual import name). This is needed so thatFlask knows where to look for templates, static files, and so on. For moreinformation have a look at the Flask documentation.
3. We then use the route() decorator to tell Flask what URLshould trigger our function.
4. The function is given a name which is also used to generate URLs for thatparticular function, and returns the message we want to display in theuser’s browser.
Just save it as hello.py or something similar. Make sure to not callyour application flask.py because this would conflict with Flaskitself.

To run the application you can either use the flask command orpython’s -m switch with Flask.  Before you can do that you needto tell your terminal the application to work with by exporting theFLASK_APP environment variable:

$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
If you are on Windows you need to use set instead of export.

Alternatively you can use python -m flask:

$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
This launches a very simple builtin server, which is good enough for testingbut probably not what you want to use in production. For deployment options seeDeployment Options.

Now head over to http://127.0.0.1:5000/, and youshould see your hello world greeting.

Externally Visible Server

If you run the server you will notice that the server is only accessiblefrom your own computer, not from any other in the network.  This is thedefault because in debugging mode a user of the application can executearbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network,you can make the server publicly available simply by adding--host=0.0.0.0 to the command line:

flask run --host=0.0.0.0
This tells your operating system to listen on all public IPs.

What to do if the Server does not Start¶

In case the python -m flask fails or flask does not exist,there are multiple reasons this might be the case.  First of all you needto look at the error message.

Old Version of Flask¶

Versions of Flask older than 0.11 use to have different ways to start theapplication.  In short, the flask command did not exist, andneither did python -m flask.  In that case you have two options:either upgrade to newer Flask versions or have a look at the Development Serverdocs to see the alternative method for running a server.

Invalid Import Name¶

The FLASK_APP environment variable is the name of the module to import atflask run. In case that module is incorrectly named you will get animport error upon start (or if debug is enabled when you navigate to theapplication). It will tell you what it tried to import and why it failed.

The most common reason is a typo or because you did not actually create anapp object.

Debug Mode¶

(Want to just log errors and stack traces? See Application Errors)

The flask script is nice to start a local development server, butyou would have to restart it manually after each change to your code.That is not very nice and Flask can do better.  If you enable debugsupport the server will reload itself on code changes, and it will alsoprovide you with a helpful debugger if things go wrong.

To enable debug mode you can export the FLASK_DEBUG environment variablebefore running the server:

$ export FLASK_DEBUG=1
$ flask run
(On Windows you need to use set instead of export).

This does the following things:

1. it activates the debugger
2. it activates the automatic reloader
3. it enables the debug mode on the Flask application.
There are more parameters that are explained in the Development Server docs.
