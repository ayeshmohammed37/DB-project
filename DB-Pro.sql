CREATE DATABASE ExaminationSystem

use ExaminationSystem

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Phone VARCHAR(15),
    IntakeID INT,
    AccountID INT,
    ManagerID INT,
    BranchID INT,
    TrackID INT
); 

select * from Student

CREATE TABLE Track (
    TrackID INT  PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ManagerID INT,
	DepartmentID INT,
); 

select * from Track


CREATE TABLE Branch (
    BranchID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ManagerID INT,
); 

drop table Branch
select * from Branch


CREATE TABLE Intake (
    IntakeID INT PRIMARY KEY,
    IntakeName VARCHAR(100) NOT NULL,
    ManagerID INT,
); 

select * from Intake


CREATE TABLE LoginAccount (
    AccountID INT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Role VARCHAR(20) NOT NULL
); 

select * from LoginAccount


CREATE TABLE Manager (
    ManagerID INT  PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    AccountID INT,
    FOREIGN KEY (AccountID) REFERENCES LoginAccount(AccountID)
); 

select * from Manager


alter table Student
   add FOREIGN KEY (TrackID) REFERENCES Track(TrackID)

alter table Student
   add FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)

 alter table Student
   add FOREIGN KEY (IntakeID) REFERENCES Intake(IntakeID)

select * from LoginAccount

alter table Student
   add FOREIGN KEY (AccountID) REFERENCES LoginAccount(AccountID)

alter table Student
   add FOREIGN KEY (ManagerID) REFERENCES Manager(ManagerID)


alter table Track
   add  FOREIGN KEY (ManagerID) REFERENCES Manager(ManagerID)


----------------------------------------------------------------------

CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    ManagerID INT,
    FOREIGN KEY (ManagerID) REFERENCES Manager(ManagerID),
); 

alter table Intake
   add  FOREIGN KEY (ManagerID) REFERENCES Manager(ManagerID)
   

alter table Branch
   add  FOREIGN KEY (ManagerID) REFERENCES Manager(ManagerID)




CREATE TABLE ST_Intake (
	Student_ID int PRIMARY KEY,
	Intake_ID int
);

select * from ST_Intake


Alter Table ST_Intake 
	add FOREIGN KEY (Intake_ID) REFERENCES Intake(IntakeID)

Alter Table ST_Intake 
	add	FOREIGN KEY (Student_ID) REFERENCES Student(StudentID)

------------------------------------------------------------------------------------------------------

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Description varchar(max)	,
    MaxDegree INT,
    MinDegree INT,
    ExamID INT
); 


CREATE TABLE Exam (
    ExamID INT PRIMARY KEY,
    StartTime DATETIME NOT NULL,
    EndTime DATETIME NOT NULL,
    TotalTime INT,
    Year INT,
	ex_Type VARCHAR(30), --Exam or Corrective
); 

alter table Course
  add   FOREIGN KEY (ExamID) REFERENCES Exam(ExamID)



CREATE TABLE StudentCourse (
    StudentID INT,
    CourseID INT,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);



CREATE TABLE St_Exam (
	ExamID INT,
	StudentID INT,
	PRIMARY KEY (ExamID, StudentID),
	FOREIGN KEY (ExamID) REFERENCES Exam(ExamID),
	FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
);

CREATE TABLE Instructor (
    InstructorID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Phone VARCHAR(15),
    AccountID INT,
);


alter table Instructor
   add FOREIGN KEY (AccountID) REFERENCES LoginAccount(AccountID)



CREATE TABLE InstructorCourse (
    InstructorID INT,
    CourseID INT,
    PRIMARY KEY (InstructorID, CourseID),
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

select * from Question


CREATE TABLE InstructorExam (
	InstructorID INT,
	ExamID INT,
	PRIMARY KEY (InstructorID, ExamID),
	FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID),
    FOREIGN KEY (ExamID) REFERENCES Exam(ExamID)
);





CREATE TABLE Question (
    QuestionID INT  PRIMARY KEY,
    QuestionText varchar(max)	 NOT NULL,
    CorrectAnswer varchar(max)	,
    BestAnswer varchar(max)	,
    MultipleChoice varchar(max) ,
    TrueFalse varchar(max),
    Text varchar(max)	,
    ExamID INT,
	CourseID INT
);


alter table Question
   add FOREIGN KEY (ExamID) REFERENCES Exam(ExamID)
