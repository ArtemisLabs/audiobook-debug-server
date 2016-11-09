from flask import jsonify
from flask import Blueprint

API = Blueprint('api', __name__)

class Api:
    @API.route("/")
    def hello():
        """Returns Hello World."""
        return "Hello welcome to this API."
    @API.route("/bookdata")
    def bookjson():
        """Returns JSON bookdata."""
        bookdata = { \
                    'id': "507f191e810c19729de860ea",
                    'title': "50 Shades of Grey",
                    'author': "E.L. James",
                    'lastplayed':{'date':"2016-11-09T15:00:08+00:00", 'position':"00:23:53"},
                    'bookmarks': [{'title':"Bookmark 1", 'position':"00:05:37"},
                                {'title':"Bookmark 2", 'position':"00:50:23"}],
                    'chapters':  [{'title':"Bookmark 1", 'position':"00:05:37"}],
                    'file':       {'integrity': "", 'length': "01:32:00",
                                'location': "file:<{LOCATIONHERE}>"},
                    'available': "true"
                }
        return jsonify(**bookdata)
    @API.route("/userdata")
    def userjson():
        """Returns JSON user data."""
        userdata = { \
                    'id': "507f1f77bcf86cd799439011",
                    'username': "username",
                    'passsword': "$2a$04$Cdw08X96K87OPG9u1pxkE.5QSUeeXBWh4Q3m4LHx/U4JJ3hAP2JOq",
                    'name': "Joe Bloggs",
                    'premium': "true"
                }
        returndata = userdata.copy()
        del returndata['password']
        return jsonify(**returndata)
