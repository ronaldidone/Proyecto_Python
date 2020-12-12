CREATE PROCEDURE [dbo].[test_for_pyodbc] 
    @param_in nvarchar(max) = N'', 
    @param_out nvarchar(max) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    -- set output parameter
    SELECT @param_out = N'Output parameter value: You said "' + @param_in + N'".';
    
    -- also return a couple of result sets
    SELECT N'SP result set 1, row 1' AS foo
    UNION ALL
    SELECT N'SP result set 1, row 2' AS foo;
    
    SELECT N'SP result set 2, row 1' AS bar
    UNION ALL
    SELECT N'SP result set 2, row 2' AS bar;
END