

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

	def get_query_result_row(self, query, params=()):
		return get_item(self.get_query_results(), 0);


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


	def get_query_results_seq(self, query, callback, chunk_size=1000, params=()):
		offset = 0;
		while True:
			partial_results = self.get_query_results(query+" LIMIT {chunk_size} OFFSET {offset}".format(chunk_size=chunk_size, offset=offset), params);
			if len(partial_results) == 0:
				break;
			callback(partial_results);
			offset += chunk_size;







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


	def insert_rows_seq(self, table_name, fields, rows, callback=None, chunk_size=1000):
		for i in range(0, len(rows), chunk_size):
			self.insert_rows(table_name, fields, rows[i:i+chunk_size]);
			if callback != None:
				callback(i+chunk_size);


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




Sqlary = Sqlary_v1;





