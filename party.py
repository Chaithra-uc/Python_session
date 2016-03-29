
#!/usr/bin/env python

import MySQLdb
import csv
import itertools


def main():
        connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
        mysql_cursor=connection.cursor()

	offset=0

	while True:
	
		mysql_cursor.execute("select p.id,p.fullname,up.unresolved_party_type_name,m.id from party as p inner join party_unresolved_party_type_map as m on p.id=m.party_id inner join unresolved_party_type as up on m.unresolved_party_type_id=up.id order by p.id limit 1000")
       		result_set = mysql_cursor.fetchall()
		
		f = open("file_%s.csv"%offset,"wb")
		fwriter = csv.writer(f,quoting=csv.QUOTE_ALL)

		for i in result_set:
			fwriter.writerow(i)
		f.close()
		offset += 1000
#	if offset!=len(result_set):
#				break

#		if f is None:
#			f.close()
#	#	en=enumerate(result_set)
#		en1=list(en)
#		if len(en1)<1000:
#			break;

		

#	my_len=len(result_set)

#	i=0
#        fwriter.writerow(['ID','Full name','party type','map id'])


	
	
#	for i in result_set:
#		fwriter.writerow(i)

#		result_set[i]=result_set[i]+1
#		if i== 20:
#			break	



#		f.close()

#		result_set[i]=result_set[i]+1
#		if i==20:
#			break


	
#       	f.close()
        return 0


if __name__ == '__main__':
        main()


