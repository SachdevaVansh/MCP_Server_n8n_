from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import psycopg2
import sys

# Initialize FastMCP server
mcp = FastMCP("postgremcp", "PostgreSQL MCP Server")

psqlurl = "postgresql://neondb_owner:npg_wmx8RBrc0eLP@ep-little-math-a44xgwvr-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def query_db(sql, params=None):
    conn = psycopg2.connect(psqlurl)
    conn.autocommit = True
    try:
        cur = conn.cursor()
        cur.execute(sql, params or ())

        if cur.rowcount is not None and sql.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
            conn.commit()

        if cur.description:
            return cur.fetchall()

        return None

    finally:
        cur.close()
        conn.close()

@mcp.tool()
def insert_user(name, email, age):
    rows = query_db(
        """
        INSERT INTO users (name, email, age)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (name, email, age)
    )
    return rows[0][0]

@mcp.tool()
def get_user(id):
    rows = query_db(
        "SELECT id, name, email, age FROM users WHERE id = %s",
        (id,)
    )
    return rows[0] if rows else None

@mcp.tool()
def get_all_users():
    return query_db("SELECT * FROM users ORDER BY id ASC")

@mcp.tool()
def update_user(id, name=None, email=None, age=None):

    fields = []
    values = []

    if name:
        fields.append("name = %s")
        values.append(name)
    if email:
        fields.append("email = %s")
        values.append(email)
    if age:
        fields.append("age = %s")
        values.append(age)

    if not fields:
        return "No fields to update"

    sql = f"UPDATE users SET {', '.join(fields)} WHERE id = %s"
    values.append(id)

    query_db(sql, tuple(values))
    return "User updated"

@mcp.tool()
def delete_user(id):
    query_db("DELETE FROM users WHERE id = %s", (id,))
    return "User deleted"

def main():
    mode = "stdio"
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode == "http":
        print("Starting MCP server on http://127.0.0.1:8000")
        mcp.run(
            transport="streamable-http",
        )
    else:
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
