

from msl import *

import psycopg2



class Sqlary_v1:#need = [psycopg2]
	def __init__(self, db_credentials, log=print):
		self.log = log;
		self.db_credentials = db_credentials;
		self.init();


	def init(self):
		self.conn = psycopg2.connect(**self.db_credentials);
		self.cur = self.conn.cursor();


	def get_query_results(self, query, params=()):
		try:
			if(params == ()):
				self.cur.execute(query);
			else:
				self.cur.execute(query, params);
			titles = [desc[0] for desc in self.cur.description];
			return list(dict(zip(titles, list(row))) for row in self.cur.fetchall());
		except psycopg2.Error as e:
			self.log("Error in get_query({0}, {1}) - \n".format(query, params), traceback.format_exc());
			self.init();
			raise e;


	def exec_query(self, query, params=()):
		try:
			if(params == ()):
				self.cur.execute(query);
			else:
				self.cur.execute(query, params);
			self.conn.commit();
		except psycopg2.Error as e:
			self.log("Error in exec_query({0}, {1}) - \n".format(query, params), traceback.format_exc());
			self.init();
			raise e;


	def insert_rows(self, table_name, fields, rows):
		if(len(rows) > 0):
			self.exec_query("INSERT INTO {table_name} ({fields}) VALUES {values} ".format(
				table_name = table_name, 
				fields = ','.join(fields),
				values = ",".join(
					[
						"("
						 +
						",".join(["%s"]*len(fields))
						 +
						")"
					]*len(rows)
				)
			), mix_list(rows));


	def insert_row(self, table_name, fields, row):
		return self.insert_rows(table_name, fields, [row]);


	def get_table(self, table_name):
		return self.get_query_results("select * from "+table_name);







