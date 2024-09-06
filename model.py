from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Book(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    Tittle = db.Column(db.String(100), nullable = False)
    Author = db.Column(db.String(100), nullable = False)
    DateCreated = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Book { self.Tittle, self.Author }>"

class Student(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    FullNames = db.Column(db.String(100), nullable = False)
    EmailAddress = db.Column(db.String(255), nullable = False)
    Phone = db.Column(db.String(15), nullable = False)
    Address = db.Column(db.String(50), nullable = False)
    County = db.Column(db.String(30), nullable = False)
    CreatedOn = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Student { self.FullNames, self.EmailAddress, self.Phone }>"

class Recipe(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    Tittle = db.Column(db.String(100), nullable = False)
    Details = db.Column(db.String(200), nullable = False)
    Review = db.Column(db.String(20), nullable = False)
    Status = db.Column(db.String(30), nullable = False)
    Category = db.Column(db.String(30), nullable = False)
    CreatedOn = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Recipe { self.Tittle, self.Details, self.Review, self.Status, self.Category }>"


class Post(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    Tittle = db.Column(db.String(100), nullable = False)
    Description = db.Column(db.Text, nullable = False)
    CreatedOn = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.Tittle, self.Description[:20], self.CreatedOn}>"
    
class Comment(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    Contents = db.Column(db.Text, nullable = False)
    PostId = db.Column(db.Integer(), nullable = False)
    CreatedOn = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Comment {self.Contents[:20], self.PostId, self.CreatedOn}>"

class Supplier(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    SupplierName = db.Column(db.String(100), nullable = False)
    EmailAddress = db.Column(db.String(255), nullable = False)
    PhoneNumber = db.Column(db.String(15), nullable = False)
    DateOfBirth = db.Column(db.DateTime, nullable = False)
    PostalAddress = db.Column(db.String(150), nullable = False)
    Address = db.Column(db.String(150), nullable = False)
    County = db.Column(db.String(100), nullable = False)
    SubCounty = db.Column(db.String(100), nullable = False)
    CreatedOn = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Supplier {self.SupplierName, self.EmailAddress, self.PhoneNumber, self.DateOfBirth, self.PostalAddress, self.Address, self.County, self.SubCounty} >"


class Users(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    FullNames = db.Column(db.String(100), nullable = False)
    Username = db.Column(db.String(100), nullable = False)
    Password = db.Column(db.String(255), nullable = False)
    EmailAddress = db.Column(db.String(255), nullable = False)
    PhoneNumber = db.Column(db.String(15), nullable = False)
    DateOfBirth = db.Column(db.DateTime, nullable = False)
    ProfilePicture = db.Column(db.String(255), nullable = True)
    Address = db.Column(db.String(200), nullable = False)
    CreatedOn = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Users {self.FullNames, self.Username, self.EmailAddress, self.Address}>"

class Accounts(db.Model):
    Id = db.Column(db.Integer(), primary_key = True)
    Name = db.Column(db.String(100), nullable = False)
    Group = db.Column(db.String(100), nullable = False)
    Currency = db.Column(db.String(100), nullable = False)
    StartBalance = db.Column(db.Numeric(24,2), nullable = False)
    CreatedOn = db.Column(db.DateTime(), default = datetime.utcnow)

    def __repr__(self):
        return f"<Accounts {self.Name, self.Group, self.Currency, self.StartBalance}>"
