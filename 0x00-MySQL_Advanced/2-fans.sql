-- Task 2: Rank the country origins of bands by the total number of fans, considering duplicates
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
