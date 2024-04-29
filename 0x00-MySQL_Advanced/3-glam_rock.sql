-- List all bands with Glam rock as their main style, ranked by longevity
-- Compute lifespan using the "formed" and "split" attributes, and ensure the script is compatible with any database

SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
