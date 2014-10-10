--CREATE VIEW TransD (docid, term, count) AS SELECT term, docid, count FROM frequency;
SELECT a.docid, b.term, SUM(a.count*b.count)
FROM frequency a, frequencyD b
WHERE a.term = b.docid
GROUP BY a.docid, b.term;
