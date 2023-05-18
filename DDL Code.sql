use librarySystem;

create table library.book(
  bookID int primary key identity,
  title nvarchar(500) not null ,
  pageCount int check (pageCount > 0),
  ISBN nvarchar(50) unique,
  language nvarchar(500),
  description nvarchar(3500),
  publisher nvarchar(500),
  minimumAgeToRead int check (minimumAgeToRead >= 1),
  publicationYear smallint
);

create table library.bookGenre(
    bookID int not null ,
    genre nvarchar(50) not null ,
    primary key (bookID, genre),
    foreign key (bookID) references library.book(bookID)
)

create table library.author(
    authorID int primary key identity,
    firstName nvarchar(500) not null ,
    thirdName nvarchar(500) not null ,
)

create table library.authorsOfBook(
    bookID int not null ,
    authorID int not null ,
    primary key (bookID,authorID),
    foreign key (bookID) references library.book(bookID),
    foreign key (authorID) references library.author(authorID)
)

create table library.location(
    locationID int primary key identity,
    floor smallint,
    section nvarchar(500),
    shelfNumber int check (shelfNumber > 0)
)

create table library.account(
    email nvarchar(200) primary key not null,
    passwordHash nvarchar(500),
)

create table library.person(
    personID int primary key identity,
    firstName nvarchar(500) not null ,
    thirdName nvarchar(500) not null,
    phoneNumber nvarchar(15) unique,
    dateOfBirth date,
    sex smallint,
    isAdmin smallint
)

create table library.emailOf(
    personID int not null,
    email nvarchar(200) not null,
    primary key (personID,email),
    foreign key (email) references library.account (email),
    foreign key (personID) references library.person (personID),
)

create table library.bookCopy(
    copyID int not null,
    bookID int not null,
    borrowerID int,
    locationID int,
    Condition nvarchar(500),
    isReturned smallint,
    borrowedDate date,
    periodInDays smallint,

    primary key (copyID, bookID),
    foreign key (borrowerID) references library.person (personID),
    foreign key (locationID) references library.location (locationID)
)
