CREATE PROCEDURE [dbo].[test2_for_pyodbc] 
    @param1_in nvarchar(max),
    @param2_in nvarchar(max) 
AS
BEGIN
    SET NOCOUNT ON;

    -- also return a couple of result sets
    SELECT N'SP result set 1, row 1' AS foo
    UNION ALL
    SELECT N'SP result set 1, row 2' AS foo;
    
    SELECT N'SP result set 2, row 1' AS bar
    UNION ALL
    SELECT N'SP result set 2, row 2' AS bar;
END