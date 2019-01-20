from msl import *
import psycopg2


class Sqlary_v1:#need = [psycopg2]
	def __init__(self, db_credentials, log=print):
		self.log = log;
		self.db_credentials = db_credentials;
		self.auto_commit = True;
		self.init();

	def init(self):
		self.conn = psycopg2.connect(**self.db_credentials);
		self.cur = self.conn.cursor();

	def _exec_query_internal(self, query, params=()):
		if(type(query) == tuple):
			(query, params) = query;
		if(type(params) == dict):
			keys = list(params.keys());
			query = query.format(**dict.fromkeys(keys, "%s"));
			params = tuple(params[i] for i in keys);
		if(params == ()):
			return self.cur.execute(query);
		else:
			return self.cur.execute(query, params);

	def get_query_results(self, query, params=(), commit=False):
		try:
			self._exec_query_internal(query, params);
			titles = [desc[0] for desc in self.cur.description];
			output = list(dict(zip(titles, list(row))) for row in self.cur.fetchall());
			if(commit and self.auto_commit):
				self.conn.commit();
			return output;
		except psycopg2.Error as e:
			self.log("Error in get_query({0}, {1}) - \n".format(query, params), traceback.format_exc());
			self.init();
			raise e;

	def exec_query(self, query, params=()):
		try:
			output = self._exec_query_internal(query, params);
			if(self.auto_commit):
				self.conn.commit();
			return output;
		except psycopg2.Error as e:
			self.log("Error in exec_query({0}, {1}) - \n".format(query, params), traceback.format_exc());
			self.init();
			raise e;

	def get_query_results_seq(self, query, callback, chunk_size=1000):
		if type(query) == tuple:
			(query, params) = query;
		else:
			params = ();
		offset = 0;
		while True:
			partial_results = self.get_query_results(query+(" LIMIT {chunk_size} OFFSET {offset}".format(chunk_size=chunk_size, offset=offset)), params);
			if len(partial_results) == 0:
				break;
			callback(partial_results);
			offset += chunk_size;

	def get_query_result_row(self, query, params=(), commit=False):
		return get_item(self.get_query_results(query, params, commit), 0);

	def insert_rows_seq(self, table_name, rows, chunk_size=1000, callback=None):
		for i in range(0, len(rows), chunk_size):
			self.insert_rows(table_name, rows[i:i+chunk_size]);
			if callback != None:
				callback(i+chunk_size);

	def insert_rows(self, table_name, rows):
		fields = list(rows[0].keys());
		rows = list(list(row[column] for column in fields) for row in rows);
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

	def insert_row(self, table_name, row, return_inserted_id=False):
		fields = row.keys();
		row = list(row[i] for i in fields);
		query = "INSERT INTO {table_name} ({fields}) VALUES ({values}) {suffix}".format(
			table_name = table_name,
			fields = ','.join(fields),
			values = ",".join(["%s"]*len(fields)),
			suffix = "RETURNING id" if return_inserted_id else ""
		);
		if return_inserted_id:
			return self.get_query_result_row(query, row, True)["id"];
		else:
			return self.exec_query(query, row);

	def get_table(self, table_name):
		return self.get_query_results("SELECT * FROM "+table_name);




Sqlary = Sqlary_v1;





