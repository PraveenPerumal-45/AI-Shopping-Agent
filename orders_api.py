"""
Orders API — reads from the `orders` table and returns
order history for the shopping assistant.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")


def get_order_history(limit: int = 10) -> list[dict]:
    """
    Return recent orders.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
      SELECT
          order_id,
          product_id,
          product_name,
          quantity,
          unit_price,
          total_price,
          status,
          order_date
      FROM orders
      ORDER BY order_date DESC
      LIMIT ?
  """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return [
    {
        "order_id": row[0],
        "product_id": row[1],
        "product_name": row[2],
        "quantity": row[3],
        "unit_price": row[4],
        "total_price": row[5],
        "status": row[6],
        "order_date": row[7],
    }
    for row in rows
]


def get_order_summary():
    """
    Return shopping summary.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(total_price),0),
            COALESCE(AVG(total_price),0)
        FROM orders
    """)

    total_orders, total_spent, average_order = cursor.fetchone()

    cursor.execute("""
        SELECT
            product_name,
            COUNT(*) AS frequency
        FROM orders
        GROUP BY product_name
        ORDER BY frequency DESC
        LIMIT 5
    """)

    favorites = cursor.fetchall()

    conn.close()

    return {
        "total_orders": total_orders,
        "total_spent": round(total_spent, 2),
        "average_order_value": round(average_order, 2),
        "favorite_products": [
            {
                "product": p,
                "count": c
            }
            for p, c in favorites
        ]
    }


if __name__ == "__main__":

    print(get_order_history())

    print(get_order_summary())