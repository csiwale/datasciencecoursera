SELECT count(*) FROM (
	SELECT * 
	FROM ( 
			SELECT * 	 
			FROM frequency
			WHERE term="transaction" 
		  ) f1, 
		  ( 
			SELECT * 	 
			FROM frequency
			WHERE term="world" 
		  ) f2
	WHERE f1.docid = f2.docid


) x;

