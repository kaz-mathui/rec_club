-- Gets a list of all buildings and the number of open requests

SELECT BuildingName, ISNULL(Count, 0) as 'COUNT'
FROM Buildings
    LEFT JOIN
    (SELECT Apartments.BuildingID, count(*) as 'Count'
    FROM Requests INNER JOIN Apartments
        ON Requests.AptID = Apartments.AptID
    WHERE Requests.Status = 'Open'
    GROUP BY Apartments.BuildingID) ReqCounts
    ON ReqCounts.BuildingID = Buildings.BuildingID