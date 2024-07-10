-- Lists all bands with Glam rock as their style
-- ranked by their longevity
-- Column names must be band_name and lifespan

SELECT band_name, (IFNULL(split, '2002') - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rocks%'
    ORDER BY lifespan DESC;
