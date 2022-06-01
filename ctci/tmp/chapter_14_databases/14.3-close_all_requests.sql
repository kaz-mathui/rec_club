-- Closes all requests from apartments in building 11

UPDATE Requests
SET Status = 'Closed'
WHERE AptID IN (SELECT AptID
FROM Apartments
WHERE BuildingID = 11)