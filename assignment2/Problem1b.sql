SELECT count(*) FROM (
	SELECT term FROM (
		SELECT * FROM frequency f
			WHERE docid="10398_txt_earn" and f.count=1
)) x;

