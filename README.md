# Cookies API

You are tasked with creating a minimal REST API which provides endpoints to enable CRUD operations on cookies . . . no, not browser cookies, actual cookies (chocolate chip, peanut butter, sugar, etc).

You will develop the endpoints and methods for the API so a user can manage their cookie (object) stash via HTTP requests. You will also provide documentation in this README about how to formulate those calls to the endpoints
so the user can clearly understand how to manage their cookies. Data about the cookie objects will persist in an instance of MongoDB under a database called, interestingly enough, `cookies`.

The user should be able to use the API to create new cookies, edit their properties (you get to decide which properties they have), delete (eat) cookies, and get information about all their cookies. For example, how many chocolate chip cookies do I have right now?

As an example, a `cookie` object could look like this in the db:

```
{
    'user_id': 'dood',
    'flavor': 'snicker doodle',
    'temp': 113,
    'radius': 3.4,
    'deliciousness': 10,
    'toppings': false,
    'date_baked': 10790343458,
    'fresh': true
}
```

An interesting endpoint might be something like `http://localhost/cookie_api/top_delicious/?number=10&user=me`, which returns the top 10 most delicious cookies belonging to the user `me`. The sky and your creativity are the only limits to what you can accomplish, but don't spend too much time on it for your own sake :)

You will be using Python 3 with the `Flask` framework and `pymongo` package to communicate with MongoDB. Set up a development environment on your machine, and when you submit the project you can provide us with a dump of the data in your `cookies` db.

We'll be looking at the following criteria:

- How intuitive it is to use
- Object-oriented approach
- Logical consistency of HTTP methods and their resulting actions and responses
- Conciseness and clarity
- Error handling
- Use of git to manage development flow
- Extra points for creativity and interesting features
- Extra points for test cases

Don't worry about security--authentication, authorization, etc--but a user should have to provide their `user_id` or similar identifier with every call to the API to ensure they're only working with their cookies.

We have provided you with a barebones file to start from: `runserver.py`

Contact ______________ with any questions. Good luck!
