import unittest
from msl.utils.sqlary import Sqlary
import testing.postgresql

class SqlaryTest(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.psql_server = testing.postgresql.Postgresql();
    self.sql = sql = Sqlary(self.psql_server.dsn());
    sql.exec_query("CREATE TABLE data (id INT, content VARCHAR(20), size INT)");
    sql.insert_rows("data", list(dict(
                                    id = i+1,
                                    size = i*100,
                                    content = "Content"+str(i)
                                  ) for i in range(100)));

  @classmethod
  def tearDownClass(self):
    self.psql_server.stop();

  def test_basic(self):
    sql = self.sql;
    test1_output1 = sql.get_query_results("SELECT * FROM data WHERE id < 3 ORDER BY id ASC");
    test1_output2 = sql.get_query_results("SELECT * FROM data WHERE id < %s ORDER BY id ASC", (3,));
    test1_output3 = sql.get_query_results("SELECT * FROM data WHERE id < {xx} ORDER BY id ASC", {"xx": 3});
    test1_expected = [{"id": 1, "size": 0, "content": "Content0"}, {"id": 2, "size": 100, "content": "Content1"}];
    self.assertEqual(test1_output1, test1_expected);
    self.assertEqual(test1_output2, test1_expected);
    self.assertEqual(test1_output3, test1_expected);
    # Checks if all the rows were inserted well.
    test2_output = sql.get_query_result_row("SELECT COUNT(*) AS output FROM data");
    test2_expected = {"output": 100};
    self.assertEqual(test2_output, test2_expected);

  def test_get_query_results_seq(self):
    sql = self.sql;
    test1_output1 = [];
    sql.get_query_results_seq(
          "SELECT id FROM data WHERE id % 2 = 0 AND id < 16 ORDER BY id ASC",
          callback = lambda x: test1_output1.append(x),
          chunk_size=3
    );
    test1_output2 = [];
    sql.get_query_results_seq(
          ("SELECT id FROM data WHERE MOD(id, {xx}) = 0 AND id < 16 ORDER BY id ASC", {"xx": 2}),
          callback = lambda x: test1_output2.append(x),
          chunk_size = 3
    );
    test1_expected = [
      [{"id": 2}, {"id": 4}, {"id": 6}],
      [{"id": 8}, {"id": 10}, {"id": 12}],
      [{"id": 14}]
    ];
    self.assertEqual(test1_output1, test1_expected);
    self.assertEqual(test1_output2, test1_expected);
    test2_output = [];
    sql.get_query_results_seq(
      "SELECT id FROM data WHERE id % 2 = 0",
      callback = lambda x: test2_output.append(x),
      chunk_size = 19
    );
    self.assertEqual(list(len(x) for x in test2_output), [19, 19, 12]);
    test3_output = [];
    sql.get_query_results_seq(
      "SELECT id FROM data WHERE id % 2 = 0",
      callback = lambda x: test3_output.append(x),
      chunk_size = 10
    );
    self.assertEqual(list(len(x) for x in test3_output), [10, 10, 10, 10, 10]);

  def test_insert_row(self):
    sql = self.sql;
    sql.exec_query("CREATE TABLE sales (id SERIAL PRIMARY KEY, amount INT)");
    id1 = sql.insert_row("sales", {"amount": 101}, return_inserted_id=True);
    id2 = sql.insert_row("sales", {"amount": 102}, return_inserted_id=True);
    id3 = sql.insert_row("sales", {"amount": 103}, return_inserted_id=True);
    sql.exec_query("DELETE FROM sales where id >= 2");
    id4 = sql.insert_row("sales", {"amount": 104}, return_inserted_id=True);
    self.assertEqual((id1, id2, id3, id4), (1, 2, 3, 4));
    sql.insert_rows("sales", list({"amount": 105+i} for i in range(10)));
    test_output = sql.get_query_results("SELECT * FROM sales ORDER BY id ASC");
    test_expected = list({"id": i, "amount": 100+i} for i in range(1, 15) if not(2 <= i <= 3));
    self.assertEqual(test_output, test_expected);

  def test_insert_rows_seq(self):
    # ToDo(Mohit): Implement this test.
    pass

# unittest.main();

