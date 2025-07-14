# Database Choice: PostgreSQL

## Why PostgreSQL was chosen

### 1. Leader Election

- PostgreSQL supports built-in advisory locks, which make it simple to implement per-region leader election.
- Advisory locks are atomic, reliable, and require minimal custom logic.
- In contrast, MongoDB does not have native lock mechanisms. Implementing leader election in MongoDB would require additional logic using timestamps and TTL-based leasing, which introduces complexity and potential for race conditions.

### 2. Central Coordination

- PostgreSQL provides strong ACID guarantees, which are crucial for coordination between agents, especially for deduplication and consistency under failure.
- Deduplication can be enforced using a unique constraint on fields like `(execution_id, region)`.
- Transactions in PostgreSQL ensure that task assignment and result submission are atomic and safe across failures.
- MongoDB, being eventually consistent by default, makes these guarantees harder to achieve without additional effort.

### 3. Schema and Relational Modeling

- The data model for targets, results, agents, and task assignments is naturally relational.
- PostgreSQL handles this cleanly with foreign keys and joins.
- MongoDB would require either denormalization or more complex aggregation queries to achieve the same relationships.

### 4. Testing and Tooling

- PostgreSQL works well with test frameworks like pytest and testcontainers, making it easier to write reliable integration tests.
- Schema changes and migrations are well-supported through tools like Alembic or raw SQL migration scripts.
- Familiar SQL query capabilities make debugging and local testing easier.

### 5. Familiarity and Maintainability

- You have existing experience with PostgreSQL, which allows you to move faster and reason about edge cases with more confidence.
- PostgreSQL is widely adopted in production systems, making the design more transferable to real-world or SaaS use cases later.

## Summary

PostgreSQL was chosen over MongoDB primarily for its built-in support for leader election, strong consistency guarantees, and better fit for relational coordination logic. While MongoDB could be used with sufficient custom logic, PostgreSQL simplifies many of the core challenges of building a fault-tolerant, distributed uptime monitoring system.