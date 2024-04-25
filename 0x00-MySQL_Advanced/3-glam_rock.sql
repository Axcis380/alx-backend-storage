-- Compute the lifespan in years until 2022
SELECT 
    band_name, 
    IFNULL(SPLIT[1] - SPLIT[0], 0) AS lifespan
FROM (
    -- Split the formed and split columns to get the start and end years
    SELECT 
        band_name,
        SPLIT(formed, '-') AS SPLIT
    FROM 
        bands
    WHERE 
        style LIKE '%Glam rock%'
) AS subquery
ORDER BY 
    lifespan DESC;
