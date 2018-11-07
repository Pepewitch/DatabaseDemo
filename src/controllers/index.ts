import mysql, { Connection, Pool } from 'mysql';
import { Doctor } from 'Doctor';

export default class Controller {
  public static getConnection() {
    if (!this.pool) {
      this.pool = mysql.createPool({
        host: process.env.DB_HOST,
        port: Number(process.env.DB_PORT),
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        connectionLimit: 20,
      });
    }
    return this.pool;
  }
  public static testConnection() {
    const connection = this.getConnection();
    connection.query('SELECT 1+1 AS solution', (error, results, fields) => {
      if (error) {
        throw error;
      }
      console.log('The solution is: ', results[0].solution);
    });
  }
  private static pool: Pool;
}
