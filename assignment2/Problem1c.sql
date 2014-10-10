SELECT count(*) FROM (
	SELECT term FROM 
		(SELECT * FROM frequency f1
			WHERE docid="10398_txt_earn" and f1.count=1
		)
	UNION
	SELECT term FROM
		(SELECT * FROM frequency f2
			WHERE docid="925_txt_trade" and f2.count=1
		)
	
) x;

