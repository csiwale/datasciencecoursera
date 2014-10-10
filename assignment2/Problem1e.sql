SELECT count(*) FROM (
	SELECT docid, (term)
	FROM (
		SELECT docid, term, count(DISTINCT term) FROM frequency GROUP BY docid HAVING count(term) > 300
	) x
	GROUP BY 
	HAVING count(term) > 300
) y;

SELECT docid, term, count(DISTINCT term) FROM frequency GROUP BY docid HAVING count(term) > 300;

SELECT COUNT(*) FROM (SELECT docid, sum(term) FROM frequency GROUP BY docid HAVING sum(term) > 300); 1652

SELECT COUNT(*) FROM (SELECT docid, sum(term) FROM frequency GROUP BY docid HAVING sum(term) > 300); 107



