from flask import Flask, url_for, request, abort, redirect, jsonify

app = Flask(__name__, static_url_path='', static_folder='static')

#array in memory (replaced by database later)
books=[
    {"id":1, "Title":"Harry Potter", "Author":"JK","Price":1000},
    {"id":2, "Title":"Cooking Book", "Author":"Mr Angry Man","Price":2000},
    {"id":3, "Title":"Python Made Easy", "Author":"Some Liar","Price":1500}
]
nextId=4

@app.route('/')
def index():
    return "Hello World"

#GET ALL
# curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
    return jsonify(books)

#GET by id
# curl http://127.0.0.1:5000/books/123213
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter(lambda t : t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 204
    return jsonify(foundBooks[0])

#CREATE (POST)
#curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId #utilize global variable for incrementing id.
    #error handling, if no json in request, abort
    if not request.json:
        abort(400)
    
    #fills out new book object with json that is sent.
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book) #adds to book array
    nextId += 1 #increment
    return jsonify(book)

#UPDATE
#curl -X PUT -H "content-type:application/json" -d "{\"Title\":\"New Title\", \"Price\":999}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t : t["id"] == id, books)) #find all books with same id
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0] #current book = first found book with same id
    #if a title/author/price is received, update the current book.
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)

#DELETE
#curl -X "DELETE" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t : t["id"] == id, books)) #find all books with same id
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    print("in if")
    app.run(debug=True) #allows for realtime editing