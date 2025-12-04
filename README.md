# MCP Server + NeonDB + n8n Integration

A small experimental project to learn and demonstrate how a Model Context Protocol (MCP) server can bridge an AI client, a database, and workflow automation.

🎯 What this project does

Provides a Python-based MCP server that exposes tools for interacting with a PostgreSQL database hosted on NeonDB.

Through the server, an MCP-aware client (e.g. Claude Desktop) can run SQL queries via natural-language tool calls.

Using ngrok, the local MCP server can be exposed via a public URL, enabling external access.

Allows integration with n8n — workflows can call the MCP server to interact with the database, enabling AI-driven automations.

Together: AI (Claude Desktop) ⇄ MCP Server ⇄ NeonDB — plus the option to have n8n workflows connected to the same server.

✅ Features

🐍 Python MCP server — minimal dependencies, easy to run.

Use of NeonDB as cloud PostgreSQL, so no need for local DB setup.

Natural-language driven database queries via MCP tools.

Public exposure via ngrok for remote workflows / integrations.

Workflow automation support via n8n + MCP — enabling complex pipelines or triggered jobs.

📦 Setup & Usage

1. Prerequisites

Python (version as specified in .python-version or your environment)

A NeonDB (PostgreSQL) database — credentials and connection details

ngrok (optional, for public exposure)

n8n (optional, for workflow automation)

An MCP-capable client (e.g. Claude Desktop)

2. Getting Started

# Clone the repository
```
git clone https://github.com/SachdevaVansh/MCP_Server_n8n_.git
cd MCP_Server_n8n_
```
# Install dependencies (if using a dependency manager / virtual env)
```
pip install -r requirements.txt   # or equivalent
```
# Run the MCP server
```
python postgresql.py
```
3. Configure Connection to NeonDB

Update configuration (or environment variables) with your NeonDB credentials/connection string so that the server can connect to the database.

4. (Optional) Expose Server using ngrok
```
ngrok http 8000   # or whichever port your MCP server listens on
```

Take note of the generated public URL — you can use this URL to connect from remote clients or from n8n workflows.

5. Connect with Claude Desktop as MCP Client

Open Claude Desktop → Add MCP server in settings

Provide command/config to run your server (or point to the public ngrok URL)

Then you can issue natural-language queries like:

“List the users created in the last 7 days.”

“Fetch sales records where amount > 1000.”

“Add a new row to the orders table with …”

6. Integrate with n8n (Optional)

Use the ngrok public URL (or local server URL if within same network) as the endpoint for MCP calls from n8n

Create n8n workflows to trigger database queries, data retrieval, updates — driven by events, schedules, webhooks or by AI instructions

🧠 What you learn / Why it matters

Understanding the mechanics of how an MCP server exposes tools and handles requests.

How an MCP client (like Claude Desktop) communicates with the server, and how tool-calling works in structured schema rather than raw code.

How AI models can be granted database access (PostgreSQL via NeonDB) in a controlled and safe manner.

How local servers can be safely exposed externally (via ngrok) for automation or remote access.

How AI, database, and automation tools (n8n) can be bridged together — a practical foundation for building “agentic AI + automation” workflows.

⚠️ Security & Usage Considerations

Be careful when exposing your MCP server publicly via ngrok — restrict access, validate inputs, avoid running on production databases without safeguards.

Do not allow arbitrary SQL queries from untrusted users/agents — consider sanitizing inputs or limiting schema/tools exposed.

If you expand the project (e.g. to handle inserts/updates), ensure you implement proper schema validation and permissions.

Treat any credentials (database, n8n API keys) securely — do not hard-code them; use environment variables or secure config management.

✨ Future Improvements / Ideas

Add tool-level abstractions (e.g. “get_user_by_email”, “create_order”) instead of raw SQL — safer and more robust.

Add support for parameterized queries to prevent SQL injection.

Add logging / audit trail of tool calls and database changes.

Extend the server to handle more complex workflows — joins, transactions, batch operations, etc.

Provide example n8n workflows to illustrate common use-cases (reporting, alerts, data sync).

Add automated tests.
