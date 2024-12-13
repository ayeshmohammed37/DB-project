INSERT INTO Department (DepartmentID, DepartmentName, ManagerID)
VALUES
    (1, 'Human Resources', FLOOR(RAND() * 10) + 1),
    (2, 'Information Technology', FLOOR(RAND() * 10) + 1),
    (3, 'Finance', FLOOR(RAND() * 10) + 1),
    (4, 'Marketing', FLOOR(RAND() * 10) + 1);
